import re
from atciparotajs.endings import detect_bucket
from atciparotajs.cardinals import cardinal
from atciparotajs.ordinals import ordinal
from atciparotajs.fractions import fraction
from atciparotajs.roman import roman_to_int, is_valid_roman
from atciparotajs.abbreviations import expand_abbreviations
from atciparotajs.time import clock_time

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

# Matches "N lpp." to handle noun inflection together with the number
_LPP_PAT = re.compile(r'(\d+)\s+lpp\.')

# Single word preceding a Roman-numeral candidate (to detect surname initials)
_WORD_BEFORE = re.compile(r'\w+\s+$')


def _expand_lpp(m: re.Match) -> str:
    n = int(m.group(1))
    noun = "lappuse" if n == 1 else "lappuses"
    return f"{cardinal(n, 2)} {noun}"


def _next_word_bucket(text: str, pos: int) -> int:
    """Find next Latvian word after pos and return its bucket."""
    rest = text[pos:]
    m = LAT_WORD.search(rest)
    if not m:
        return 1
    word = m.group(0)
    bucket = detect_bucket(word)
    # If genitive (bucket 3 or 6), look at the word after for better context
    if bucket in (3, 6):
        rest2 = rest[m.end():]
        m2 = LAT_WORD.search(rest2)
        if m2:
            bucket2 = detect_bucket(m2.group(0))
            if bucket2 not in (3, 6):
                return bucket2
    return bucket


def convert(text: str, expand_abbr: bool = True) -> str:
    text = _TIME_PAT.sub(lambda m: clock_time(int(m.group(1)), int(m.group(2))), text)
    # Handle "N lpp." before general abbreviation expansion so we can inflect both
    # the number and the noun correctly (e.g. "58 lpp." → "piecdesmit astoņas lappuses")
    text = _LPP_PAT.sub(_expand_lpp, text)

    if expand_abbr:
        text = expand_abbreviations(text)

    def replace(m):
        bucket = _next_word_bucket(text, m.end())

        if m.group(1) is not None:   # decimal
            return fraction(int(m.group(1)), m.group(2), bucket)
        elif m.group(3) is not None:  # arabic ordinal
            return ordinal(int(m.group(3)), bucket)
        elif m.group(4) is not None:  # roman ordinal
            s = m.group(4)
            # Single uppercase letter after a word is likely a surname initial, not Roman
            if len(s) == 1 and _WORD_BEFORE.search(text[:m.start()]):
                return m.group(0)
            if is_valid_roman(s):
                return ordinal(roman_to_int(s), bucket)
            return m.group(0)
        elif m.group(5) is not None:  # roman cardinal
            s = m.group(5)
            # Single uppercase letter after a word is likely a surname initial, not Roman
            if len(s) == 1 and _WORD_BEFORE.search(text[:m.start()]):
                return m.group(0)
            if is_valid_roman(s):
                return ordinal(roman_to_int(s), bucket)
            return m.group(0)
        elif m.group(6) is not None:  # arabic cardinal
            return cardinal(int(m.group(6)), bucket)
        return m.group(0)

    return PATTERN.sub(replace, text)
