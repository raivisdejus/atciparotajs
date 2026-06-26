"""pytest plugin: generate TESTS.md after every test run."""

from __future__ import annotations

import pathlib
import pytest

ROOT = pathlib.Path(__file__).parent.parent

# Maps nodeid -> {"text": str, "expected": str, "outcome": str}
_results: dict[str, dict] = {}


def pytest_collection_finish(session):
    """Record the actual param values (with full Unicode) from each Item."""
    for item in session.items:
        if not hasattr(item, "callspec"):
            continue
        params = item.callspec.params
        expected = params.get("expected", "")
        if "text" in params:
            text = params["text"]
        elif "args" in params:
            text = str(params["args"])
        elif "amount" in params and "code" in params:
            text = f"{params['amount']} {params['code']}"
        else:
            text = ", ".join(f"{k}={v}" for k, v in params.items() if k != "expected")
        _results[item.nodeid] = {"text": text, "expected": expected, "outcome": "?"}


def pytest_runtest_logreport(report):
    if report.when != "call":
        return
    if report.nodeid in _results:
        _results[report.nodeid]["outcome"] = report.outcome
    else:
        # Non-parametrised test
        _results[report.nodeid] = {"text": report.nodeid.split("::")[-1], "expected": "", "outcome": report.outcome}


def pytest_sessionfinish(session, exitstatus):
    _write_md()


# ---------------------------------------------------------------------------

def _section_label(nodeid: str) -> str:
    part = nodeid.split("::")[-1]
    name = part.split("[")[0]
    return name.replace("test_", "").replace("_", " ").title()


def _write_md():
    if not _results:
        return

    sections: dict[str, list[dict]] = {}
    for nodeid, data in _results.items():
        label = _section_label(nodeid)
        sections.setdefault(label, []).append(data)

    lines = ["# Test Cases\n"]
    lines.append(
        "Auto-generated after each `pytest` run. "
        "Shows every parametrised case with its last recorded outcome.\n"
    )

    ICON = {"passed": "✅", "failed": "❌", "error": "⚠️", "?": "⏭️"}

    for section, rows in sections.items():
        lines.append(f"## {section}\n")
        lines.append("| Input | Expected | Result |")
        lines.append("|-------|----------|--------|")
        for r in rows:
            icon = ICON.get(r["outcome"], r["outcome"])
            inp = r["text"].replace("|", "\\|")
            exp = r["expected"].replace("|", "\\|")
            lines.append(f"| `{inp}` | `{exp}` | {icon} |")
        lines.append("")

    out = ROOT / "TESTS.md"
    out.write_text("\n".join(lines), encoding="utf-8")
