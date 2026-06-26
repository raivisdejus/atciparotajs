from __future__ import annotations

import re
from atciparotajs.endings import detect_bucket
from atciparotajs.cardinals import cardinal
from atciparotajs.ordinals import ordinal
from atciparotajs.fractions import fraction
from atciparotajs.roman import roman_to_int, is_valid_roman
from atciparotajs.abbreviations import expand_abbreviations
from atciparotajs.time import clock_time
from atciparotajs.phone import expand_phones
from atciparotajs.currency import currency as _currency, CURRENCY_FORMS

# Groups: 1,2=decimal; 3=arabic ordinal; 4=roman ordinal; 5=roman cardinal; 6=arabic cardinal
PATTERN = re.compile(
    r'(\d+)[.,](\d+)'              # groups 1,2: decimal number
    r'|(\d+)\.(?=\s|$)'           # group 3: arabic ordinal (digit + dot + space/end)
    r'|([IVXLCDM]+)\.(?=\s|$)'   # group 4: roman ordinal
    r'|\b([IVXLCDM]+)\b'          # group 5: roman cardinal
    r'|(\d+)'                      # group 6: arabic cardinal
)

LAT_WORD = re.compile(r'[A-Za-zĀāČčĒēĢģĪīĶķĻļŅņŌōŖŗŠšŪūŽžāēīūčšžģķļņŗ]+')

# Clock time "H:MM" must be expanded before the general pattern sees the digits
_TIME_PAT = re.compile(r'\b(\d{1,2}):(\d{2})\b')

# Sports score "N:M" — single-digit second operand means it's not a clock time
_SCORE_PAT = re.compile(r'\b(\d+):(\d+)\b')

# Ordinal year range "N.–M." (e.g. "1941.–1945. gads")
_ORD_RANGE_PAT = re.compile(r'(\d+)\.[–\-—](\d+)\.(?=\s|$)')

# Undotted year range "NNNN–NNNN gad…" (e.g. "1941–1945 gads")
_YEAR_RANGE_PAT = re.compile(r'\b(\d{4})[–\-—](\d{4})(?=\s+gad)')

# Number range "N–M" or "N-M" (hyphen/en-dash not preceded by start-of-range digit already consumed)
_RANGE_PAT = re.compile(r'\b(\d+)[–\-—](\d+)\b')

# Percentage range "N–M%" or "N-M%"
_PCT_RANGE_PAT = re.compile(r'\b(\d+(?:[.,]\d+)?)[–\-—](\d+(?:[.,]\d+)?)\s*%')

# Space-separated thousands like "150 000" (collapse to plain number before any other processing)
_SPACE_THOU_PAT = re.compile(r'\b(\d{1,3}(?:[  ]\d{3})+)\b')

# Matches "N lpp." to handle noun inflection together with the number
_LPP_PAT = re.compile(r'(\d+)\s+lpp\.')

# Unit abbreviations that must be inflected based on the preceding number
_UNIT_MAP = {
    "km":  ("kilometrs",  "kilometri",  "kilometru"),   # nom sg, nom pl, gen pl
    "km.": ("kilometrs",  "kilometri",  "kilometru"),
    "m":   ("metrs",      "metri",      "metru"),
    "m.":  ("metrs",      "metri",      "metru"),
    "kg":  ("kilograms",  "kilogrami",  "kilogramu"),
    "kg.": ("kilograms",  "kilogrami",  "kilogramu"),
    "cm":  ("centimetrs", "centimetri", "centimetru"),
    "cm.": ("centimetrs", "centimetri", "centimetru"),
    "mm":  ("milimetrs",  "milimetri",  "milimetru"),
    "mm.": ("milimetrs",  "milimetri",  "milimetru"),
    "ml":  ("mililits",   "mililitri",  "mililitru"),
    "ml.": ("mililits",   "mililitri",  "mililitru"),
    "g":   ("grams",      "grami",      "gramu"),
    "g.":  ("grams",      "grami",      "gramu"),
}
_UNIT_ABBR_RE = "|".join(re.escape(k) for k in sorted(_UNIT_MAP, key=len, reverse=True))
_UNIT_PAT = re.compile(rf'(\d+)\s+({_UNIT_ABBR_RE})(?=\s|$|[,.])')

# Superscript units: km², m², m³, km³
_SUPER_UNIT_MAP = {
    "km²": ("kvadrātkilometrs", "kvadrātkilometri", "kvadrātkilometru"),
    "km³": ("kubikkilometrs",   "kubikkilometri",   "kubikkilometru"),
    "m²":  ("kvadrātmetrs",     "kvadrātmetri",     "kvadrātmetru"),
    "m³":  ("kubikmetrs",       "kubikmetri",       "kubikmetru"),
}
_SUPER_ABBR_RE = "|".join(re.escape(k) for k in sorted(_SUPER_UNIT_MAP, key=len, reverse=True))
_SUPER_PAT = re.compile(rf'(\d+)\s+({_SUPER_ABBR_RE})(?=\s|$|[,.])')

# Negative numbers: "-N" at word boundary, not preceded by a digit (avoid ranges like "5-6")
_NEG_PAT = re.compile(r'(?<!\d)-(\d+(?:[.,]\d+)?)')

# Percentage: integer or decimal followed by %
_PCT_PAT = re.compile(r'(\d+(?:[.,]\d+)?)\s*%')

# Noun forms of "procents" indexed by grammatical bucket
_PROCENT_NOUN = {
    1: "procents", 2: "procenta", 6: "procentu", 7: "procentā",
    8: "procenti",  9: "procentiem", 10: "procentus", 11: "procentos",
}

# Prepositions and the case bucket they govern for a following percentage
_PCT_PREPS = {
    "par": 9, "ar": 9, "līdz": 9,
    "no": 9, "pēc": 6, "pie": 6, "virs": 9, "zem": 6, "pirms": 6,
    "ap": 10,
}

# For n=1 (singular), some prepositions require accusative sg (bucket 6) rather than gen sg (bucket 2)
_PCT_PREPS_ONE = {"par": 6}

# Single word preceding a Roman-numeral candidate (to detect surname initials)
_WORD_BEFORE = re.compile(r'\w+\s+$')
# Capital-letter word following a dot+space — indicates a surname after an initial
_CAP_WORD_AFTER = re.compile(r'^\s+[A-ZĀČĒĢĪĶĻŅŠŪŽ]')

# Currency patterns — amount with symbol or ISO code
# Tonne: "53T" or "53 T" → "piecdesmit trīs tonnas" (feminine)
_TONNE_PAT = re.compile(r'(\d+)\s*T(?=\s|$|[,.])')

# Temperature: "36°C", "100°F", "90°"
_TEMP_PAT = re.compile(r'(\d+)°[CF]?(?=\s|$|[,.])')

# Vulgar fractions: "3/4", "1/2"; mixed: "2 1/4"
_FRACTION_DENOM = {
    2:   ("puse",        "puses",        "pušu"),
    3:   ("trešdaļa",   "trešdaļas",   "trešdaļu"),
    4:   ("ceturtdaļa", "ceturtdaļas", "ceturtdaļu"),
    5:   ("piektdaļa",  "piektdaļas",  "piektdaļu"),
    6:   ("sestdaļa",   "sestdaļas",   "sestdaļu"),
    7:   ("septītdaļa", "septītdaļas", "septītdaļu"),
    8:   ("astotdaļa",  "astotdaļas",  "astotdaļu"),
    9:   ("devītdaļa",  "devītdaļas",  "devītdaļu"),
    10:  ("desmitdaļa", "desmitdaļas", "desmitdaļu"),
    100: ("simtdaļa",   "simtdaļas",   "simtdaļu"),
}
_MIXED_FRAC_PAT = re.compile(r'(\d+)\s+(\d+)/(\d+)')
_SIMPLE_FRAC_PAT = re.compile(r'(\d+)/(\d+)')

# Class notation: "4.D klase", "4.d klasei"
_CLASS_PAT = re.compile(r'(\d+)\.([A-Za-z])\s+((?:klase|klaš)\w*)', re.IGNORECASE)

# Speed: "100 km/h"
_SPEED_PAT = re.compile(r'(\d+)\s*km/h(?=\s|$|[,.])')

# Age-gate label: "18+" → "astoņpadsmit plus"
_AGE_GATE_PAT = re.compile(r'\b(\d+)\+')

# Episode notation: "S02E03" — must be preserved as-is
_EPISODE_PAT = re.compile(r'\bS\d+E\d+\b', re.IGNORECASE)

# "sezona N" — cardinal N after the word "sezona" → ordinal before: "otrā sezona"
_SEASON_CARDINAL_PAT = re.compile(r'\b(sezona)\s+(\d+)\b', re.IGNORECASE)

# Academic year slash range: "2023./2024."
_ACAD_YEAR_PAT = re.compile(r'(\d+)\./(\d+)\.(?=\s|$|[,])')

_CURRENCY_SYMBOL_MAP = {'€': 'EUR', '$': 'USD', '£': 'GBP'}
_CUR_CODES_RE = '|'.join(re.escape(c) for c in sorted(CURRENCY_FORMS, key=len, reverse=True))
_CUR_AMT = r'(\d+)(?:[,.](\d{1,2}))?'
# Symbol before: €1,82 or € 1,82
_CUR_SYM_BEFORE = re.compile(r'([€$£])\s*' + _CUR_AMT)
# Symbol after: 1,82€ or 1,82 €
_CUR_SYM_AFTER = re.compile(_CUR_AMT + r'\s*([€$£])')
# Code before: EUR 1,82
_CUR_CODE_BEFORE = re.compile(r'\b(' + _CUR_CODES_RE + r')\s+' + _CUR_AMT, re.IGNORECASE)
# Code after: 1,82 EUR  or  1.82EUR (no space)
_CUR_CODE_AFTER = re.compile(_CUR_AMT + r'\s*(' + _CUR_CODES_RE + r')\b', re.IGNORECASE)


def _parse_cur_amount(int_str: str, dec_str: str | None) -> tuple[int, int]:
    major = int(int_str)
    if dec_str is None:
        minor = 0
    elif len(dec_str) == 1:
        minor = int(dec_str) * 10
    else:
        minor = int(dec_str[:2])
    return major, minor


def _expand_cur(major: int, minor: int, code: str, prev: str | None = None) -> str:
    accusative = prev is not None and detect_bucket(prev) in (2, 7)
    return _currency((major, minor), code.upper(), accusative=accusative)


def _expand_super_unit(m: re.Match) -> str:
    n = int(m.group(1))
    nom_sg, nom_pl, gen_pl = _SUPER_UNIT_MAP[m.group(2)]
    last2 = n % 100
    last1 = n % 10
    if 10 <= last2 <= 19 or last1 == 0:
        noun, bucket = gen_pl, 6
    elif last1 == 1:
        noun, bucket = nom_sg, 1
    else:
        noun, bucket = nom_pl, 8
    return f"{cardinal(n, bucket)} {noun}"


def _expand_unit(m: re.Match) -> str:
    n = int(m.group(1))
    nom_sg, nom_pl, gen_pl = _UNIT_MAP[m.group(2)]
    last2 = n % 100
    last1 = n % 10
    if 10 <= last2 <= 19 or last1 == 0:
        noun, bucket = gen_pl, 6
    elif last1 == 1:
        noun, bucket = nom_sg, 1
    else:
        noun, bucket = nom_pl, 8
    return f"{cardinal(n, bucket)} {noun}"


def _expand_speed(m: re.Match) -> str:
    n = int(m.group(1))
    last2 = n % 100
    last1 = n % 10
    if 10 <= last2 <= 19 or last1 == 0:
        noun, bucket = "kilometru", 6
    elif last1 == 1:
        noun, bucket = "kilometrs", 1
    else:
        noun, bucket = "kilometri", 8
    return f"{cardinal(n, bucket)} {noun} stundā"


def _expand_lpp(m: re.Match) -> str:
    n = int(m.group(1))
    last2 = n % 100
    last1 = n % 10
    if last1 == 1 and last2 != 11:
        return f"{cardinal(n, 2)} lappuse"
    elif 2 <= last1 <= 9 and not (10 <= last2 <= 19):
        return f"{cardinal(n, 3)} lappuses"
    else:
        return f"{cardinal(n, 6)} lappušu"


def _prev_word(text: str, start: int) -> str | None:
    """Return the Latvian word immediately before position start, or None."""
    before = text[:start].rstrip()
    m = LAT_WORD.search(before[::-1])
    if not m:
        return None
    return m.group(0)[::-1]


def _expand_temp(m: re.Match) -> str:
    n = int(m.group(1))
    if n == 0:
        return "nulle grādu"
    last2 = n % 100
    last1 = n % 10
    if last1 == 1 and last2 != 11:
        return f"{cardinal(n, 1)} grāds"
    return f"{cardinal(n, 8)} grādi"


def _expand_tonne(m: re.Match) -> str:
    n = int(m.group(1))
    last2 = n % 100
    last1 = n % 10
    if last1 == 1 and last2 != 11:
        return f"{cardinal(n, 2)} tonna"
    elif 2 <= last1 <= 9 and not (10 <= last2 <= 19):
        return f"{cardinal(n, 3)} tonnas"
    else:
        return f"{cardinal(n, 6)} tonnu"


def _expand_vulgar_fraction(num: int, denom: int) -> str:
    if denom not in _FRACTION_DENOM:
        return f"{num}/{denom}"
    nom_sg, nom_pl, gen_pl = _FRACTION_DENOM[denom]
    last2 = num % 100
    last1 = num % 10
    if last1 == 1 and last2 != 11:
        return f"{cardinal(num, 2)} {nom_sg}"
    elif 2 <= last1 <= 9 and not (10 <= last2 <= 19):
        return f"{cardinal(num, 3)} {nom_pl}"
    else:
        return f"{cardinal(num, 6)} {gen_pl}"


def _expand_mixed_fraction(m: re.Match) -> str:
    integer = int(m.group(1))
    num = int(m.group(2))
    denom = int(m.group(3))
    if denom not in _FRACTION_DENOM:
        return m.group(0)
    last2 = integer % 100
    last1 = integer % 10
    if last1 == 1 and last2 != 11:
        int_words = f"{cardinal(integer, 1)} vesels"
    elif 2 <= last1 <= 9 and not (10 <= last2 <= 19):
        int_words = f"{cardinal(integer, 8)} veseli"
    else:
        int_words = f"{cardinal(integer, 6)} veselu"
    return f"{int_words} {_expand_vulgar_fraction(num, denom)}"


def _expand_class(m: re.Match) -> str:
    n = int(m.group(1))
    letter = m.group(2).lower()
    klase = m.group(3)
    bucket = detect_bucket(klase)
    return f"{ordinal(n, bucket)} {letter} {klase}"


def _bucket_from_prev(word: str) -> int | None:
    """Return a case bucket override based on the word preceding the percentage, or None."""
    w = word.lower()
    if w in _PCT_PREPS:
        return _PCT_PREPS[w]
    if detect_bucket(word) == 2:  # ends in "a" — likely a verb taking accusative object
        return 10
    return None


def _expand_pct(m: re.Match, full_text: str) -> str:
    raw = m.group(1)
    prev = _prev_word(full_text, m.start())
    ctx = _bucket_from_prev(prev) if prev else None

    # If context is accusative (verb heuristic) but a noun follows, use genitive (attribute)
    if ctx == 10:
        rest = full_text[m.end():]
        if LAT_WORD.search(rest):
            ctx = 6

    if ',' in raw or '.' in raw:
        sep = ',' if ',' in raw else '.'
        int_part, dec_part = raw.split(sep, 1)
        bucket = ctx if ctx is not None else 8
        return fraction(int(int_part), dec_part, bucket) + " " + _PROCENT_NOUN[bucket]

    n = int(raw)
    last2 = n % 100
    last1 = n % 10
    if 10 <= last2 <= 19 or last1 == 0:
        if ctx is not None:
            return cardinal(n, ctx) + " " + _PROCENT_NOUN[ctx]
        return cardinal(n, 6) + " procentu"
    if last1 == 1:
        if prev:
            pw = prev.lower()
            if pw in _PCT_PREPS_ONE:
                b = _PCT_PREPS_ONE[pw]
                return cardinal(n, b) + " " + _PROCENT_NOUN[b]
        # With preposition context use genitive singular, otherwise nominative singular
        if ctx is not None:
            return cardinal(n, 2) + " " + _PROCENT_NOUN[2]
        return cardinal(n, 1) + " procents"
    # 2–9 range: use context bucket if available
    bucket = ctx if ctx is not None else 8
    return cardinal(n, bucket) + " " + _PROCENT_NOUN[bucket]


_SKIP_WORDS = {"un", "vai", "bet", "arī", "kā", "ar"}

# Prepositions that introduce a new phrase; when one follows a genitive noun,
# that noun is the head (not a genitive modifier), so the look-ahead must stop.
_PREP_WORDS = {"līdz", "no", "uz", "par", "pie", "pēc", "aiz", "pār", "ap",
               "virs", "zem", "pirms", "pēc", "starp", "caur"}


def _next_word_bucket(text: str, pos: int) -> int:
    """Find next Latvian word after pos and return its bucket."""
    rest = text[pos:]
    m = LAT_WORD.search(rest)
    if not m:
        return 1
    word = m.group(0)
    if word.lower() in _SKIP_WORDS:
        rest = rest[m.end():]
        m = LAT_WORD.search(rest)
        if not m:
            return 1
        word = m.group(0)
    bucket = detect_bucket(word)
    # If genitive (bucket 3 or 6), look at the word after for better context.
    # Stop if the following word is a preposition — it signals the genitive word
    # is the head noun, not an attribute (e.g. "4. jūnija līdz 7.").
    if bucket in (3, 6):
        rest2 = rest[m.end():]
        m2 = LAT_WORD.search(rest2)
        if m2:
            w2 = m2.group(0).lower()
            if w2 not in _PREP_WORDS:
                bucket2 = detect_bucket(m2.group(0))
                if bucket2 not in (3, 6):
                    return bucket2
    return bucket


def convert(text: str, expand_abbr: bool = True, no_roman: bool = False) -> str:
    # Collapse space-separated thousands ("150 000" → "150000") before any numeric processing
    text = _SPACE_THOU_PAT.sub(lambda m: m.group(0).replace(" ", "").replace(" ", ""), text)
    text = _TIME_PAT.sub(lambda m: clock_time(int(m.group(1)), int(m.group(2))), text)
    # Academic year slash range "2023./2024." before ordinal range pattern
    def _expand_acad_year(m: re.Match) -> str:
        bucket = _next_word_bucket(text, m.end())
        return f"{ordinal(int(m.group(1)), bucket)} līdz {ordinal(int(m.group(2)), bucket)}"
    text = _ACAD_YEAR_PAT.sub(_expand_acad_year, text)
    # Ordinal ranges like "1941.–1945. gads" must run before general range/ordinal patterns
    def _expand_ord_range(m: re.Match) -> str:
        bucket = _next_word_bucket(text, m.end())
        return f"{ordinal(int(m.group(1)), bucket)} līdz {ordinal(int(m.group(2)), bucket)}"
    text = _ORD_RANGE_PAT.sub(_expand_ord_range, text)
    # Undotted year ranges "1941–1945 gads" — treat as ordinals
    text = _YEAR_RANGE_PAT.sub(_expand_ord_range, text)
    # Scores must run after time (so clock patterns are already consumed)
    text = _SCORE_PAT.sub(
        lambda m: f"{cardinal(int(m.group(1)), 1)} {cardinal(int(m.group(2)), 1)}", text
    )
    # Percentage ranges "N–M%" must be handled before general range and pct patterns
    def _expand_pct_range(m: re.Match) -> str:
        prev = _prev_word(text, m.start())
        ctx = _bucket_from_prev(prev) if prev else None
        bucket = ctx if ctx is not None else 10
        n1_str, n2_str = m.group(1), m.group(2)
        def _spell_pct_part(raw: str) -> str:
            if ',' in raw or '.' in raw:
                sep = ',' if ',' in raw else '.'
                int_part, dec_part = raw.split(sep, 1)
                return fraction(int(int_part), dec_part, bucket)
            return cardinal(int(raw), bucket)
        noun = _PROCENT_NOUN.get(bucket, "procenti")
        return f"{_spell_pct_part(n1_str)} līdz {_spell_pct_part(n2_str)} {noun}"
    text = _PCT_RANGE_PAT.sub(_expand_pct_range, text)
    # Ranges: use the following noun's bucket for both numbers
    def _expand_range(m: re.Match) -> str:
        bucket = _next_word_bucket(text, m.end())
        return f"{cardinal(int(m.group(1)), bucket)} līdz {cardinal(int(m.group(2)), bucket)}"
    text = _RANGE_PAT.sub(_expand_range, text)
    text = _PCT_PAT.sub(lambda m: _expand_pct(m, text), text)
    text = _NEG_PAT.sub(lambda m: "mīnus " + m.group(1), text)
    # Handle superscript units (km², m², m³) before plain unit abbreviations
    text = _SUPER_PAT.sub(_expand_super_unit, text)
    # Handle speed (km/h) before plain unit abbreviations (which also match "km")
    text = _SPEED_PAT.sub(_expand_speed, text)
    # Handle unit abbreviations (km, m, kg) before general abbreviation expansion
    text = _UNIT_PAT.sub(_expand_unit, text)
    # Handle tonnes (feminine) — "53T" or "53 T"
    text = _TONNE_PAT.sub(_expand_tonne, text)
    # Handle "N lpp." before general abbreviation expansion so we can inflect both
    # the number and the noun correctly (e.g. "58 lpp." → "piecdesmit astoņas lappuses")
    text = _LPP_PAT.sub(_expand_lpp, text)

    # Currency amounts must expand before phones and abbreviations
    text = _CUR_CODE_BEFORE.sub(
        lambda m: _expand_cur(*_parse_cur_amount(m.group(2), m.group(3)), m.group(1),
                              _prev_word(text, m.start())), text)
    text = _CUR_CODE_AFTER.sub(
        lambda m: _expand_cur(*_parse_cur_amount(m.group(1), m.group(2)), m.group(3),
                              _prev_word(text, m.start())), text)
    text = _CUR_SYM_BEFORE.sub(
        lambda m: _expand_cur(*_parse_cur_amount(m.group(2), m.group(3)),
                              _CURRENCY_SYMBOL_MAP[m.group(1)],
                              _prev_word(text, m.start())), text)
    text = _CUR_SYM_AFTER.sub(
        lambda m: _expand_cur(*_parse_cur_amount(m.group(1), m.group(2)),
                              _CURRENCY_SYMBOL_MAP[m.group(3)],
                              _prev_word(text, m.start())), text)

    # Phone numbers must expand before abbreviations to prevent "tel." → "litrs"
    text = expand_phones(text)

    if expand_abbr:
        text = expand_abbreviations(text)

    # Class notation "4.D klase" before general pattern (prevents D → roman 500)
    text = _CLASS_PAT.sub(_expand_class, text)
    # Mixed fractions "2 1/4" before simple "3/4" and before general pattern
    text = _MIXED_FRAC_PAT.sub(_expand_mixed_fraction, text)
    text = _SIMPLE_FRAC_PAT.sub(lambda m: _expand_vulgar_fraction(int(m.group(1)), int(m.group(2))), text)
    # Temperature "36°C", "90°"
    text = _TEMP_PAT.sub(_expand_temp, text)
    # Age-gate labels "18+" before general pattern
    text = _AGE_GATE_PAT.sub(lambda m: cardinal(int(m.group(1)), 1) + " plus", text)
    # "sezona 2" → "otrā sezona" (cardinal after "sezona" treated as ordinal, word order flipped)
    text = _SEASON_CARDINAL_PAT.sub(lambda m: ordinal(int(m.group(2)), 2) + " " + m.group(1).lower(), text)
    # Protect episode notation "S02E03" from being mangled by PATTERN
    _ep_store: dict[str, str] = {}
    _ep_alpha = "abcdefghijklmnopqrstuvwxyz"
    def _protect_ep(m: re.Match) -> str:
        idx = len(_ep_store)
        key = f"\x00ep{_ep_alpha[idx % 26]}\x00"
        _ep_store[key] = m.group(0)
        return key
    text = _EPISODE_PAT.sub(_protect_ep, text)

    def replace(m):
        bucket = _next_word_bucket(text, m.end())

        if m.group(1) is not None:   # decimal
            return fraction(int(m.group(1)), m.group(2), bucket)
        elif m.group(3) is not None:  # arabic ordinal
            return ordinal(int(m.group(3)), bucket)
        elif m.group(4) is not None:  # roman ordinal
            if no_roman:
                return m.group(0)
            s = m.group(4)
            # Single uppercase letter before/after a capitalized word is likely a name initial
            if len(s) == 1 and (
                _WORD_BEFORE.search(text[:m.start()])
                or _CAP_WORD_AFTER.match(text[m.end():])
            ):
                return m.group(0)
            if is_valid_roman(s):
                return ordinal(roman_to_int(s), bucket)
            return m.group(0)
        elif m.group(5) is not None:  # roman cardinal
            if no_roman:
                return m.group(0)
            s = m.group(5)
            # Single uppercase letter before/after a capitalized word is likely a name initial
            if len(s) == 1 and (
                _WORD_BEFORE.search(text[:m.start()])
                or _CAP_WORD_AFTER.match(text[m.end():])
            ):
                return m.group(0)
            if is_valid_roman(s):
                return ordinal(roman_to_int(s), bucket)
            return m.group(0)
        elif m.group(6) is not None:  # arabic cardinal
            return cardinal(int(m.group(6)), bucket)
        return m.group(0)

    text = PATTERN.sub(replace, text)
    for key, val in _ep_store.items():
        text = text.replace(key, val)
    return text
