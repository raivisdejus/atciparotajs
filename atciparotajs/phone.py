import re

_DIGIT_NAMES = {
    '0': 'nulle', '1': 'viens', '2': 'divi', '3': 'trīs', '4': 'četri',
    '5': 'pieci', '6': 'seši', '7': 'septiņi', '8': 'astoņi', '9': 'deviņi',
}


def spell_phone(digits: str) -> str:
    """Spell a phone number digit by digit in Latvian."""
    return ' '.join(_DIGIT_NAMES[d] for d in digits if d.isdigit())


# {phone:digits} — explicit digit-by-digit markup
_EXPLICIT_PAT = re.compile(r'\{phone:(\d+)\}')

# tel/mob prefix: tel. tel: tel followed by optional +371 and digits
_PREFIX_PAT = re.compile(
    r'(?i)(?:tel|mob)[.:\s]\s*(?:\+371[\s-]?)?(\d[\d\s\-]{5,})',
)

# +371 international prefix without tel/mob
_INTL_PAT = re.compile(r'\+371[\s-]?(\d[\d\s\-]{5,})')


def expand_phones(text: str) -> str:
    text = _EXPLICIT_PAT.sub(lambda m: spell_phone(m.group(1)), text)
    text = _PREFIX_PAT.sub(lambda m: spell_phone(m.group(1)), text)
    text = _INTL_PAT.sub(lambda m: spell_phone(m.group(1)), text)
    return text
