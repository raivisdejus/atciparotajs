## Notes for the AI
- In tests, always define all constants (test case lists, lookup tables, etc.) before any `def` or `class` block. Never interleave constants with functions.

## Latvian plural forms (CLDR Rule #3 — 3 forms)

CLDR and the Mozilla Firefox localization guide define three plural categories for Latvian:

| CLDR form | Condition | Examples |
|-----------|-----------|---------|
| **zero**  | n = 0 | 0 |
| **one**   | n % 10 == 1 AND n % 100 != 11 | 1, 21, 31, 41, 101 … |
| **other** | everything else | 2–20, 22–29, 30, 100 … |

Reference: https://www.unicode.org/cldr/charts/48/supplemental/language_plural_rules.html#lv

### How this codebase implements the rule

CLDR's **other** form maps to two distinct Latvian grammatical forms:

| Condition | Grammatical form | Bucket |
|-----------|-----------------|--------|
| `n % 10 in 2–9` AND `n % 100 NOT in 10–19` | nominative plural | 8 (masc) / 3 (fem) |
| `n % 10 == 0` OR `n % 100 in 10–19` | genitive plural | 6 |

CLDR's **zero** form (n = 0) also uses genitive plural (bucket 6).

The standard 3-way selection pattern used throughout the codebase:
```python
last2 = n % 100
last1 = n % 10
if last1 == 1 and last2 != 11:         # CLDR "one"  → nominative singular
    ...
elif 2 <= last1 <= 9 and not (10 <= last2 <= 19):  # CLDR "other", nom pl branch
    ...
else:                                   # CLDR "zero" + "other", gen pl branch
    ...
```

### Noun form tuples

When adding a new noun, always supply a 3-tuple:
```python
(nominative_singular, nominative_plural, genitive_plural)
# e.g. ("kilograms", "kilogrami", "kilogramu")
# e.g. ("lappuse",   "lappuses",  "lappušu")
```

### Where the plural logic lives

- `currency.py` — `_pick_form(n, forms, accusative)` — canonical implementation
- `core.py` — `_expand_unit`, `_expand_super_unit`, `_expand_lpp`, `_expand_pct` — same pattern inline