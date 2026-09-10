from __future__ import annotations

import re
from atciparotajs.endings import detect_bucket
from atciparotajs.cardinals import cardinal
from atciparotajs.ordinals import ordinal
from atciparotajs.fractions import fraction
from atciparotajs.roman import roman_to_int, is_valid_roman
from atciparotajs.abbreviations import expand_abbreviations
from atciparotajs.time import expand_times
from atciparotajs.phone import expand_phones, spell_phone
from atciparotajs.currency import currency as _currency, CURRENCY_FORMS

# What may follow an ordinal dot: whitespace, end of text, a letter glued to
# the dot ("2026.gada", "XX.gadsimts") or closing punctuation ("3., 4. vieta").
_AFTER_ORD = r'(?=\s|$|[^\W\d_]|[,;:)\]!?”"\'’»…])'

# End of a unit or symbol: anything but a letter or digit may follow
# ("5 km”", "(36°C)", "5 km!"), while "5 min" and "5 kmh" stay untouched.
_UNIT_END = r'(?![^\W_])'

# Groups: 1,2=decimal; 3=arabic ordinal; 4=roman ordinal; 5=roman cardinal; 6=arabic cardinal
PATTERN = re.compile(
    r'(\d+)[.,](\d+)'              # groups 1,2: decimal number
    rf'|(\d+)\.{_AFTER_ORD}'      # group 3: arabic ordinal (digit + dot)
    rf'|([IVXLCDM]+)\.{_AFTER_ORD}'  # group 4: roman ordinal
    r'|\b([IVXLCDM]+)\b'          # group 5: roman cardinal
    r'|(\d+)'                      # group 6: arabic cardinal
)


def _glue_space(text: str, pos: int) -> str:
    """Space needed after a consumed ordinal dot that glued two words together.

    "2026.gada" loses its dot when the ordinal expands, so without this the
    result would read "sestāgada".
    """
    if pos < len(text) and re.match(r'[^\W\d_]', text[pos]):
        return " "
    return ""

LAT_WORD = re.compile(r'[A-Za-zĀāČčĒēĢģĪīĶķĻļŅņŌōŖŗŠšŪūŽžāēīūčšžģķļņŗ]+')

# Counted amounts may be decimal ("2,5 kg"); the decimal part must not be split off
_DEC_NUM = r'(\d+(?:[.,]\d+)?)'

# Range separator: dash or ellipsis. A following unit abbreviation confirms the
# range, so there spaces are free; without one they must be symmetric ("5 – 6",
# not "5 -3" or "bija 5… 6"), leaving negative numbers and a sentence-trailing
# ellipsis their own reading.
_RANGE_SEP_CORE = r'(?:\.\.\.|[…–—-])'
_AMT_RANGE_SEP = rf'\s*{_RANGE_SEP_CORE}\s*'
_RANGE_SEP = rf'(?:{_RANGE_SEP_CORE}|\s+{_RANGE_SEP_CORE}\s+)'

# Sports score "N:M" — single-digit second operand means it's not a clock time
_SCORE_PAT = re.compile(r'\b(\d+):(\d+)\b')

# Ordinal year range "N.–M." (e.g. "1941.–1945. gads")
_ORD_RANGE_PAT = re.compile(rf'(\d+)\.[–\-—](\d+)\.{_AFTER_ORD}')

# Undotted year range "NNNN–NNNN gad…" (e.g. "1941–1945 gads", "1941 – 1945 gads")
_YEAR_RANGE_PAT = re.compile(r'\b(\d{4})\s*[–\-—]\s*(\d{4})(?=\s+gad)')

# Number range "N–M", "N - M", "N…M", "N...M"; either side may be decimal
# ("0–1,5 milimetri"), so the decimal part is not torn off by the range split
_RANGE_PAT = re.compile(rf'\b{_DEC_NUM}{_RANGE_SEP}{_DEC_NUM}\b')

# Percentage range "N–M%" or "N-M%"
_PCT_RANGE_PAT = re.compile(r'\b(\d+(?:[.,]\d+)?)[–\-—](\d+(?:[.,]\d+)?)\s*%')

# Identifier codes: a token with two or more dashes and at least one digit
# ("BIS-BL-827846-114426", "978-9934-0-1234-5"). Not a range; every digit run is
# read digit by digit like a phone number. Both dashes must be glued between
# alphanumerics, so a signed temperature range ("-5…-3°C") is not taken for a code.
_CODE_PAT = re.compile(r'(?<!\S)(?=\S*\d)(?=(?:\S*[^\W_][-–—](?=[^\W_])){2})\S+')

# Maximal digit run inside an identifier code
_CODE_DIGITS_PAT = re.compile(r'\d+')

# Space-separated thousands like "150 000" (collapse to plain number before any other processing)
_SPACE_THOU_PAT = re.compile(r'\b(\d{1,3}(?:[  ]{1,2}\d{3})+)\b')

# Matches "N lpp." to handle noun inflection together with the number
_LPP_PAT = re.compile(rf'{_DEC_NUM}\s*lpp\.')

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
_UNIT_PAT = re.compile(rf'{_DEC_NUM}\s*({_UNIT_ABBR_RE}){_UNIT_END}')

# Superscript units: km², m², m³, km³
_SUPER_UNIT_MAP = {
    "km²": ("kvadrātkilometrs", "kvadrātkilometri", "kvadrātkilometru"),
    "km³": ("kubikkilometrs",   "kubikkilometri",   "kubikkilometru"),
    "m²":  ("kvadrātmetrs",     "kvadrātmetri",     "kvadrātmetru"),
    "m³":  ("kubikmetrs",       "kubikmetri",       "kubikmetru"),
}
_SUPER_ABBR_RE = "|".join(re.escape(k) for k in sorted(_SUPER_UNIT_MAP, key=len, reverse=True))
_SUPER_PAT = re.compile(rf'{_DEC_NUM}\s*({_SUPER_ABBR_RE}){_UNIT_END}')

# Negative numbers: "-N" at word boundary, not preceded by a digit (avoid ranges
# like "5-6"), a letter or another dash — a glued hyphen belongs to a name or a
# code ("COVID-19", "LV-1010"), not to a negative number.
_NEG_PAT = re.compile(r'(?<![\w-])-(\d+(?:[.,]\d+)?)')

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

# Context words that license reading an uppercase letter sequence as a Roman
# numeral. Without one, acronyms ("VID", "LV", "CV", "MI") stay untouched.
_ROMAN_CONTEXT = re.compile(
    r'^[\s]*(?:'
    r'gadsimt|gadu|gadsimtu|tūkstošgad'
    r'|nodaļ|apakšnodaļ|sadaļ|daļ|sējum|pant|punkt|pielikum|nodalījum'
    r'|pasaul|kārt|posm|grup|klas|sērij|sezon|izdevum|grāmat|tabul|attēl'
    r'|kongres|koncert|simfonij|olimpiād'
    r')', re.IGNORECASE
)

# Single word preceding a Roman-numeral candidate (to detect surname initials)
_WORD_BEFORE = re.compile(r'\w+\s+$')
# Capital-letter word following a dot+space — indicates a surname after an initial
_CAP_WORD_AFTER = re.compile(r'^\s*[A-ZĀČĒĢĪĶĻŅŠŪŽ]')

# Currency patterns — amount with symbol or ISO code
# Tonne: "53T" or "53 T" → "piecdesmit trīs tonnas" (feminine)
_TONNE_PAT = re.compile(rf'{_DEC_NUM}\s*T{_UNIT_END}')

# Temperature: "36°C", "100°F", "90°", "21 °C", "+21°C", "+14…+15 °C", "-5…-3°C"
# Range separators: ellipsis ("…" or "..."), en/em dash, hyphen — spaces optional.
_TEMP_SEP = r'\s*(?:\.\.\.|[…–—-])\s*'
# Optional second operand of a range; groups: 3=sign, 4=number
_TEMP_RANGE = rf'(?:{_TEMP_SEP}([+-]?){_DEC_NUM})?'
# Groups: 1=sign, 2=number, 3=sign, 4=number
_TEMP_PAT = re.compile(rf'([+-]?){_DEC_NUM}{_TEMP_RANGE}\s*°[CF]?{_UNIT_END}')

# Signed values and ranges written out as "… grādi" ("+5 grādi", "+14…+15 grādi").
# The noun itself is left as the author wrote it; only signs and the range are expanded.
_TEMP_WORD_PAT = re.compile(rf'([+-]?){_DEC_NUM}{_TEMP_RANGE}(?=\s+grād)')

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

# Speed: "100 km/h", "5 m/s"
_KMH_FORMS = ("kilometrs", "kilometri", "kilometru")
_MS_FORMS = ("metrs", "metri", "metru")
_SPEED_PAT = re.compile(rf'{_DEC_NUM}\s*km/h{_UNIT_END}')
_MS_SPEED_PAT = re.compile(rf'{_DEC_NUM}\s*m/s{_UNIT_END}')

# Ranges of counted amounts: "0–2 mm", "1,5–3 km", "5–8 m/s", "80–100 km/h".
# These must run before the generic range patterns, which would spell the digits
# out and leave the unit abbreviation behind unexpanded.
_UNIT_RANGE_PAT = re.compile(
    rf'{_DEC_NUM}{_AMT_RANGE_SEP}{_DEC_NUM}\s*({_UNIT_ABBR_RE}){_UNIT_END}')
_SPEED_RANGE_PAT = re.compile(rf'{_DEC_NUM}{_AMT_RANGE_SEP}{_DEC_NUM}\s*km/h{_UNIT_END}')
_MS_SPEED_RANGE_PAT = re.compile(rf'{_DEC_NUM}{_AMT_RANGE_SEP}{_DEC_NUM}\s*m/s{_UNIT_END}')

# Age-gate label: "18+" → "astoņpadsmit plus"
_AGE_GATE_PAT = re.compile(r'\b(\d+)\+')

# Episode notation: "S02E03" — must be preserved as-is
_EPISODE_PAT = re.compile(r'\bS\d+E\d+\b', re.IGNORECASE)

# "sezona N" — cardinal N after the word "sezona" → ordinal before: "otrā sezona"
_SEASON_CARDINAL_PAT = re.compile(r'\b(sezona)\s+(\d+)\b', re.IGNORECASE)

# Academic year slash range: "2023./2024."
_ACAD_YEAR_PAT = re.compile(rf'(\d+)\./(\d+)\.{_AFTER_ORD}')

_CURRENCY_SYMBOL_MAP = {'€': 'EUR', '$': 'USD', '£': 'GBP'}
_CUR_CODES_RE = '|'.join(re.escape(c) for c in sorted(CURRENCY_FORMS, key=len, reverse=True))
# The lookbehind keeps the pattern off the decimal part of a longer number ("2,003 EUR")
_CUR_AMT = r'(?<![\d,.])(\d+)(?:[,.](\d{1,2}))?'
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


def _split_amount(raw: str) -> tuple[str, str | None]:
    """Split a possibly decimal amount into its integer and decimal parts."""
    for sep in (',', '.'):
        if sep in raw:
            int_part, dec_part = raw.split(sep, 1)
            return int_part, dec_part
    return raw, None


def _count_form(raw: str, forms: tuple[str, str, str],
                feminine: bool = False) -> tuple[str, int]:
    """Pick the noun form and case bucket agreeing with a counted amount."""
    nom_sg, nom_pl, gen_pl = forms
    sg_bucket, pl_bucket = (2, 3) if feminine else (1, 8)
    dec_part = _split_amount(raw)[1]
    n = int(dec_part) if dec_part is not None else int(raw)
    last2 = n % 100
    last1 = n % 10
    if last1 == 1 and last2 != 11:
        return nom_sg, sg_bucket
    if 2 <= last1 <= 9 and not (10 <= last2 <= 19):
        return nom_pl, pl_bucket
    return gen_pl, 6


def _spell_amount(raw: str, bucket: int, feminine: bool = False) -> str:
    """Spell one possibly decimal amount in the given case bucket."""
    int_part, dec_part = _split_amount(raw)
    if dec_part is None:
        return cardinal(int(raw), bucket)
    # The integer part stays nominative even when the noun is genitive plural
    int_bucket = 2 if feminine else 1
    return fraction(int(int_part), dec_part, bucket, int_bucket=int_bucket)


def _spell_number(raw: str, bucket: int) -> str:
    """Spell one possibly decimal number the way the main number pass does."""
    int_part, dec_part = _split_amount(raw)
    if dec_part is None:
        return cardinal(int(raw), bucket)
    return fraction(int(int_part), dec_part, bucket)


def _counted(raw: str, forms: tuple[str, str, str], feminine: bool = False) -> str:
    """Spell a possibly decimal amount together with its noun.

    The noun agrees with the last number spoken, so "2,5 kg" reads
    "divi komats pieci kilogrami" (five kilograms), not "two kilograms".
    """
    noun, bucket = _count_form(raw, forms, feminine)
    return f"{_spell_amount(raw, bucket, feminine)} {noun}"


def _counted_range(raw1: str, raw2: str, forms: tuple[str, str, str],
                   feminine: bool = False) -> str:
    """Spell a range of amounts together with its noun.

    As for a single amount the noun agrees with the last number spoken, and
    both numbers are spelled in the case that goes with that noun form, so
    "10–20 cm" reads "desmit līdz divdesmit centimetru".
    """
    noun, bucket = _count_form(raw2, forms, feminine)
    return (f"{_spell_amount(raw1, bucket, feminine)} līdz "
            f"{_spell_amount(raw2, bucket, feminine)} {noun}")


def _expand_super_unit(m: re.Match) -> str:
    return _counted(m.group(1), _SUPER_UNIT_MAP[m.group(2)])


def _expand_unit(m: re.Match) -> str:
    return _counted(m.group(1), _UNIT_MAP[m.group(2)])


def _expand_unit_range(m: re.Match) -> str:
    return _counted_range(m.group(1), m.group(2), _UNIT_MAP[m.group(3)])


def _expand_speed(m: re.Match) -> str:
    return _counted(m.group(1), _KMH_FORMS) + " stundā"


def _expand_speed_range(m: re.Match) -> str:
    return _counted_range(m.group(1), m.group(2), _KMH_FORMS) + " stundā"


def _expand_ms_speed(m: re.Match) -> str:
    return _counted(m.group(1), _MS_FORMS) + " sekundē"


def _expand_ms_speed_range(m: re.Match) -> str:
    return _counted_range(m.group(1), m.group(2), _MS_FORMS) + " sekundē"


def _expand_lpp(m: re.Match) -> str:
    return _counted(m.group(1), ("lappuse", "lappuses", "lappušu"), feminine=True)


def _prev_word(text: str, start: int) -> str | None:
    """Return the Latvian word immediately before position start, or None."""
    before = text[:start].rstrip()
    m = LAT_WORD.search(before[::-1])
    if not m:
        return None
    return m.group(0)[::-1]


def _sign_word(sign: str) -> str:
    """Spoken form of a temperature sign; unsigned values get no prefix."""
    return {"+": "plus ", "-": "mīnus "}.get(sign, "")


def _temp_bucket(raw: str) -> int:
    """Case bucket for a temperature value, read colloquially (nominative)."""
    _, dec_part = _split_amount(raw)
    n = int(dec_part) if dec_part is not None else int(raw)
    last2 = n % 100
    last1 = n % 10
    return 1 if last1 == 1 and last2 != 11 else 8


def _spell_temp(raw: str, sign: str) -> str:
    int_part, dec_part = _split_amount(raw)
    bucket = _temp_bucket(raw)
    if dec_part is None:
        return _sign_word(sign) + cardinal(int(raw), bucket)
    return _sign_word(sign) + fraction(int(int_part), dec_part, bucket, int_bucket=1)


def _temp_noun(raw: str) -> str:
    """Colloquial noun for a temperature value: "grāds" for …1, "grādu" for
    integer zero (CLDR zero form = genitive plural), "grādi" otherwise."""
    if _split_amount(raw)[1] is None and int(raw) == 0:
        return "grādu"
    return "grāds" if _temp_bucket(raw) == 1 else "grādi"


def _expand_temp(m: re.Match) -> str:
    # Temperatures read colloquially: "divdesmit grādi", not "divdesmit grādu".
    # In a range the noun agrees with the last number spoken.
    sign1, num1, sign2, num2 = m.group(1), m.group(2), m.group(3), m.group(4)
    noun = _temp_noun(num1 if num2 is None else num2)
    if num2 is None:
        return f"{_spell_temp(num1, sign1)} {noun}"
    return f"{_spell_temp(num1, sign1)} līdz {_spell_temp(num2, sign2)} {noun}"


# Nominative-style noun forms after which temperatures are read colloquially
# ("divdesmit viens grādi", "mīnus viens līdz nulle grādi"), each number with
# its own bucket. Other forms ("grādiem", "grādos") follow the noun's case.
_TEMP_NOM_NOUNS = {"grāds", "grādi", "grādu"}
_TEMP_NOUN_AFTER = re.compile(r'\s+(grād\w*)')


def _expand_temp_word(m: re.Match, full_text: str) -> str:
    """Expand signs/ranges before an explicit "grād…" noun, leaving the noun alone."""
    sign1, num1, sign2, num2 = m.group(1), m.group(2), m.group(3), m.group(4)
    noun_m = _TEMP_NOUN_AFTER.match(full_text, m.end())
    colloquial = noun_m is not None and noun_m.group(1).lower() in _TEMP_NOM_NOUNS
    if not colloquial and not sign1 and not sign2 and num2 is None:
        return m.group(0)   # plain "5 grādiem" — leave it to the general pattern
    case_bucket = None if colloquial else _next_word_bucket(full_text, m.end())

    def spell(raw: str, sign: str) -> str:
        int_part, dec_part = _split_amount(raw)
        bucket = _temp_bucket(raw) if case_bucket is None else case_bucket
        if dec_part is None:
            return _sign_word(sign) + cardinal(int(raw), bucket)
        if case_bucket is None:
            return _sign_word(sign) + fraction(int(int_part), dec_part, bucket, int_bucket=1)
        return _sign_word(sign) + fraction(int(int_part), dec_part, bucket)

    if num2 is None:
        return spell(num1, sign1)
    return f"{spell(num1, sign1)} līdz {spell(num2, sign2)}"


def _expand_tonne(m: re.Match) -> str:
    return _counted(m.group(1), ("tonna", "tonnas", "tonnu"), feminine=True)


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

# Characters that end the phrase a number belongs to: a following noun no
# longer governs its case ("“Nr.5” deva", "(Nr. 5) mājas").
_BUCKET_STOP = re.compile(r'[”"’»)\]!?;:]')

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
    # A closing quote/bracket or sentence-final punctuation cuts the phrase off:
    # in "“Nr.5” deva" the case must not be taken from "deva". Commas, dots,
    # digits and dashes do not stop it ("1., 2. un 3. vieta").
    if _BUCKET_STOP.search(rest[:m.start()]):
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
    # Identifier codes ("BIS-BL-827846-114426") must be spelled out before any
    # range pattern reads the dashes as "līdz". Only the digit runs are rewritten;
    # letters, dashes and punctuation stay as written. No digits are left behind,
    # so the later passes leave the token alone.
    text = _CODE_PAT.sub(
        lambda m: _CODE_DIGITS_PAT.sub(lambda d: spell_phone(d.group(0)), m.group(0)),
        text)
    # Clock times and time ranges must be expanded before the general pattern
    # (and before _SCORE_PAT) sees the digits
    text = expand_times(text)
    # Academic year slash range "2023./2024." before ordinal range pattern
    def _expand_acad_year(m: re.Match) -> str:
        bucket = _next_word_bucket(text, m.end())
        return (f"{ordinal(int(m.group(1)), bucket)} līdz "
                f"{ordinal(int(m.group(2)), bucket)}{_glue_space(text, m.end())}")
    text = _ACAD_YEAR_PAT.sub(_expand_acad_year, text)
    # Ordinal ranges like "1941.–1945. gads" must run before general range/ordinal patterns
    def _expand_ord_range(m: re.Match) -> str:
        bucket = _next_word_bucket(text, m.end())
        return (f"{ordinal(int(m.group(1)), bucket)} līdz "
                f"{ordinal(int(m.group(2)), bucket)}{_glue_space(text, m.end())}")
    text = _ORD_RANGE_PAT.sub(_expand_ord_range, text)
    # Undotted year ranges "1941–1945 gads" — treat as ordinals
    text = _YEAR_RANGE_PAT.sub(_expand_ord_range, text)
    # Ranges before a unit ("0–2 mm", "5–8 m/s") must run before the generic
    # range patterns, which would leave the abbreviation unexpanded
    text = _SPEED_RANGE_PAT.sub(_expand_speed_range, text)
    text = _MS_SPEED_RANGE_PAT.sub(_expand_ms_speed_range, text)
    text = _UNIT_RANGE_PAT.sub(_expand_unit_range, text)
    # Scores must run after time (so clock patterns are already consumed)
    text = _SCORE_PAT.sub(
        lambda m: f"{cardinal(int(m.group(1)), 1)} {cardinal(int(m.group(2)), 1)}", text
    )
    # Temperatures (signs and ranges included) must run before the generic range
    # and negative-number handlers, otherwise "°" is left orphaned
    text = _TEMP_PAT.sub(_expand_temp, text)
    text = _TEMP_WORD_PAT.sub(lambda m: _expand_temp_word(m, text), text)
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
        return (f"{_spell_number(m.group(1), bucket)} līdz "
                f"{_spell_number(m.group(2), bucket)}")
    text = _RANGE_PAT.sub(_expand_range, text)
    text = _PCT_PAT.sub(lambda m: _expand_pct(m, text), text)
    text = _NEG_PAT.sub(lambda m: "mīnus " + m.group(1), text)
    # Handle superscript units (km², m², m³) before plain unit abbreviations
    text = _SUPER_PAT.sub(_expand_super_unit, text)
    # Handle speed (km/h, m/s) before plain unit abbreviations (which also match "km", "m")
    text = _SPEED_PAT.sub(_expand_speed, text)
    text = _MS_SPEED_PAT.sub(_expand_ms_speed, text)
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
            return ordinal(int(m.group(3)), bucket) + _glue_space(text, m.end())
        elif m.group(4) is not None or m.group(5) is not None:  # roman ordinal/cardinal
            if no_roman:
                return m.group(0)
            s = m.group(4) if m.group(4) is not None else m.group(5)
            after = text[m.end():]
            # Only read as a Roman numeral when a context word follows
            if not _ROMAN_CONTEXT.match(after):
                return m.group(0)
            # Single uppercase letter followed by a capitalized word is likely
            # a name initial ("Jānis V. Grupa"); a lowercase context word
            # ("pārvaldes V nodaļa") outweighs that heuristic.
            if len(s) == 1 and _CAP_WORD_AFTER.match(after):
                return m.group(0)
            if is_valid_roman(s):
                glue = _glue_space(text, m.end()) if m.group(4) is not None else ""
                return ordinal(roman_to_int(s), bucket) + glue
            return m.group(0)
        elif m.group(6) is not None:  # arabic cardinal
            digits = m.group(6)
            # Identifier codes (cadastre, account, registration numbers) are read
            # digit by digit: too long to be a quantity, or padded with a
            # leading zero, which a cardinal reading would silently drop.
            if len(digits) >= 10 or (len(digits) >= 2 and digits[0] == '0'):
                return spell_phone(digits)
            return cardinal(int(digits), bucket)
        return m.group(0)

    text = PATTERN.sub(replace, text)
    for key, val in _ep_store.items():
        text = text.replace(key, val)
    return text
