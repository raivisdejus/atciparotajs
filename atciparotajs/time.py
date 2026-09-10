import re

from atciparotajs.cardinals import ONES, _below_hundred

# Locative forms of clock hours 0-23 (24-hour format).
_HOUR_LOC = {
    0:  "nullē",
    1:  "vienos",
    2:  ONES[2][11],   # "divos"
    3:  ONES[3][11],   # "trijos"
    4:  ONES[4][11],   # "četros"
    5:  ONES[5][11],   # "piecos"
    6:  ONES[6][11],   # "sešos"
    7:  ONES[7][11],   # "septiņos"
    8:  ONES[8][11],   # "astoņos"
    9:  ONES[9][11],   # "deviņos"
    10: "desmitos",
    11: "vienpadsmitos",
    12: "divpadsmitos",
    13: "trīspadsmitos",
    14: "četrpadsmitos",
    15: "piecpadsmitos",
    16: "sešpadsmitos",
    17: "septiņpadsmitos",
    18: "astoņpadsmitos",
    19: "deviņpadsmitos",
    20: "divdesmitos",
    21: "divdesmit vienos",
    22: "divdesmit divos",
    23: "divdesmit trijos",
}


def clock_time(h: int, m: int) -> str:
    """Convert clock time to spoken Latvian (e.g. 10:45 → 'desmitos četrdesmit piecās')."""
    hour_str = _HOUR_LOC.get(h, str(h))
    if m == 0:
        return hour_str
    min_str = _below_hundred(m, 13)
    return f"{hour_str} {min_str}"


# Clock times written with a colon ("10:00") are unambiguous, but the dotted
# form "10.00" collides with dot decimals ("21.5 grami") and dotted dates
# ("01.09.2026").  A dotted "HH.MM" is read as a time only when the hour is
# 0-23, the minutes are exactly two digits 00-59, and in addition either
#   (a) a time cue word ("plkst.", "plkst", "plkst:", "pulksten") precedes it —
#       the cue also covers a "līdz HH.MM" continuation, or
#   (b) it is written as a range "HH.MM–HH.MM", where both halves are valid.
# A bare "10.00" therefore keeps its current reading as a decimal number.
_HH = r'(?:[01]?\d|2[0-3])'
_MM = r'[0-5]\d'
# Not part of a longer number/date, and not followed by more digits
_NOT_NUM_BEFORE = r'(?<![\d.,:])'
_NOT_NUM_AFTER = r'(?![\d]|[.,]\d)'
_CUE = r'(?:plkst[.:]?|pulksten)(?![^\W\d_])'

# Clock time "H:MM" must be expanded before the general pattern sees the digits
_TIME_PAT = re.compile(r'\b(\d{1,2}):(\d{2})\b')

# Time range "HH:MM–HH:MM" / "HH.MM–HH.MM" (dash with optional symmetric spaces)
_TIME_RANGE_PAT = re.compile(
    rf'{_NOT_NUM_BEFORE}(?P<h1>{_HH})[.:](?P<m1>{_MM})'
    rf'(?P<sp> ?)[–—-](?P=sp)'
    rf'(?P<h2>{_HH})[.:](?P<m2>{_MM}){_NOT_NUM_AFTER}'
)

# Dotted time after a cue word, optionally continued by "līdz HH.MM"
_CUED_TIME_PAT = re.compile(
    rf'(?P<cue>\b{_CUE}\s*)(?P<h1>{_HH})\.(?P<m1>{_MM}){_NOT_NUM_AFTER}'
    rf'(?:(?P<mid>\s+līdz\s+)(?P<h2>{_HH})\.(?P<m2>{_MM}){_NOT_NUM_AFTER})?',
    re.IGNORECASE,
)


def _expand_time_range(m: re.Match) -> str:
    first = clock_time(int(m.group("h1")), int(m.group("m1")))
    second = clock_time(int(m.group("h2")), int(m.group("m2")))
    return f"{first} līdz {second}"


def _expand_cued_time(m: re.Match) -> str:
    cue = m.group("cue")
    # "plkst.10.00" — the cue is glued to the time, so it needs its own space
    if cue and not cue[-1].isspace():
        cue += " "
    out = cue + clock_time(int(m.group("h1")), int(m.group("m1")))
    if m.group("h2") is not None:
        out += m.group("mid") + clock_time(int(m.group("h2")), int(m.group("m2")))
    return out


def expand_times(text: str) -> str:
    """Expand clock times and time ranges ("10:45", "plkst. 10.00–10.30")."""
    text = _TIME_RANGE_PAT.sub(_expand_time_range, text)
    text = _CUED_TIME_PAT.sub(_expand_cued_time, text)
    return _TIME_PAT.sub(lambda m: clock_time(int(m.group(1)), int(m.group(2))), text)
