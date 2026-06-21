from atciparotajs.cardinals import cardinal

GENERIC_DOLLARS = ('dolārs', 'dolāri', 'dolāru')
GENERIC_CENTS = ('cents', 'centi', 'centu')
GENERIC_KRONA = ('krona', 'kronas', 'kronu')
GENERIC_ERA = ('ēre', 'ēres', 'ēru')

CURRENCY_FORMS = {
    'AUD': (GENERIC_DOLLARS, GENERIC_CENTS),
    'CAD': (GENERIC_DOLLARS, GENERIC_CENTS),
    'EUR': (('eiro', 'eiro', 'eiro'), GENERIC_CENTS),
    'EUR_LEGAL': (('euro', 'euro', 'euro'), GENERIC_CENTS),
    'GBP': (('sterliņu mārciņa', 'sterliņu mārciņas', 'sterliņu mārciņu'),
            ('penss', 'pensi', 'pensu')),
    'LTL': (('lits', 'liti', 'litu'), GENERIC_CENTS),
    'LVL': (('lats', 'lati', 'latu'),
            ('santīms', 'santīmi', 'santīmu')),
    'USD': (GENERIC_DOLLARS, GENERIC_CENTS),
    'RUB': (('rublis', 'rubļi', 'rubļu'),
            ('kapeika', 'kapeikas', 'kapeiku')),
    'SEK': (GENERIC_KRONA, GENERIC_ERA),
    'NOK': (GENERIC_KRONA, GENERIC_ERA),
    'PLN': (('zlots', 'zloti', 'zlotu'),
            ('grasis', 'graši', 'grašu')),
}

CURRENCY_ADJECTIVES = {
    'AUD': 'Austrālijas',
    'CAD': 'Kanādas',
    'GBP': 'Lielbritānijas',
    'NOK': 'Norvēģijas',
    'SEK': 'Zviedrijas',
    'USD': 'ASV',
    'RUB': 'Krievijas',
    'PLN': 'Polijas',
}


def _noun_gender(word: str) -> str:
    w = word.lower()
    if w.endswith(('a', 'e')):
        return 'f'
    return 'm'


def _pick_form(n: int, forms: tuple) -> tuple[str, int]:
    """Return (noun_form, cardinal_bucket) for integer n."""
    last2 = n % 100
    last1 = n % 10
    if last1 == 1 and last2 != 11:
        noun = forms[0]
        bucket = 2 if _noun_gender(noun) == 'f' else 1
    elif 2 <= last1 <= 9 and not (10 <= last2 <= 19):
        noun = forms[1]
        bucket = 3 if _noun_gender(forms[0]) == 'f' else 8
    else:
        noun = forms[2]
        bucket = 6
    return noun, bucket


def currency(
    amount,
    currency_code: str = 'EUR',
    adjective: bool = False,
    separator: str = 'un',
) -> str:
    """Spell a monetary amount in Latvian.

    amount: int (whole units only), float, or (int, int) tuple of (units, cents).
    """
    if isinstance(amount, tuple):
        major, minor = int(amount[0]), int(amount[1])
    elif isinstance(amount, float):
        major = int(amount)
        minor = round((amount - major) * 100)
    else:
        major = int(amount)
        minor = 0

    code = currency_code.upper()
    if code not in CURRENCY_FORMS:
        raise ValueError(f"Unknown currency: {currency_code!r}")

    major_forms, minor_forms = CURRENCY_FORMS[code]
    adj = CURRENCY_ADJECTIVES.get(code, '')

    major_noun, major_bucket = _pick_form(major, major_forms)
    if adjective and adj:
        major_str = cardinal(major, major_bucket) + ' ' + adj + ' ' + major_noun
    else:
        major_str = cardinal(major, major_bucket) + ' ' + major_noun

    if minor == 0:
        return major_str

    minor_noun, minor_bucket = _pick_form(minor, minor_forms)
    minor_str = cardinal(minor, minor_bucket) + ' ' + minor_noun

    return f"{major_str} {separator} {minor_str}"
