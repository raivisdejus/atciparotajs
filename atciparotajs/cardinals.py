ONES = {
    0: {b: "nulle" for b in range(1, 14)},
    #      b1        b2        b3         b4          b5         b6       b7        b8        b9           b10       b11       b12        b13
    1: {1:"viens",  2:"viena",  3:"vienas", 4:"vienam", 5:"vienai", 6:"vienu",  7:"vienā",  8:"vieni",  9:"vieniem", 10:"vienu",  11:"vienā",  12:"vienām",  13:"vienās"},
    2: {1:"divi",   2:"divas",  3:"divas",  4:"diviem", 5:"divām",  6:"divu",   7:"divos",  8:"divi",   9:"diviem",  10:"divus",  11:"divos",  12:"divām",   13:"divās"},
    3: {1:"trīs",   2:"trīs",   3:"trīs",   4:"trim",   5:"trim",   6:"trīs",   7:"trijos", 8:"trīs",   9:"trim",    10:"trīs",   11:"trijos", 12:"trim",    13:"trijos"},
    4: {1:"četri",  2:"četras", 3:"četras", 4:"četriem",5:"četrām", 6:"četru",  7:"četros", 8:"četri",  9:"četriem", 10:"četrus", 11:"četros", 12:"četrām",  13:"četrās"},
    5: {1:"pieci",  2:"piecas", 3:"piecas", 4:"pieciem",5:"piecām", 6:"piecu",  7:"piecos", 8:"pieci",  9:"pieciem", 10:"piecus", 11:"piecos", 12:"piecām",  13:"piecās"},
    6: {1:"seši",   2:"sešas",  3:"sešas",  4:"sešiem", 5:"sešām",  6:"sešu",   7:"sešos",  8:"seši",   9:"sešiem",  10:"sešus",  11:"sešos",  12:"sešām",   13:"sešās"},
    7: {1:"septiņi",2:"septiņas",3:"septiņas",4:"septiņiem",5:"septiņām",6:"septiņu",7:"septiņos",8:"septiņi",9:"septiņiem",10:"septiņus",11:"septiņos",12:"septiņām",13:"septiņās"},
    8: {1:"astoņi", 2:"astoņas",3:"astoņas",4:"astoņiem",5:"astoņām",6:"astoņu", 7:"astoņos",8:"astoņi", 9:"astoņiem",10:"astoņus", 11:"astoņos", 12:"astoņām",  13:"astoņās"},
    9: {1:"deviņi", 2:"deviņas",3:"deviņas",4:"deviņiem",5:"deviņām",6:"deviņu", 7:"deviņos",8:"deviņi", 9:"deviņiem",10:"deviņus", 11:"deviņos", 12:"deviņām",  13:"deviņās"},
}

TEENS = [
    "desmit", "vienpadsmit", "divpadsmit", "trīspadsmit", "četrpadsmit",
    "piecpadsmit", "sešpadsmit", "septiņpadsmit", "astoņpadsmit", "deviņpadsmit"
]

TENS_PREFIX = [
    "", "", "divdesmit", "trīsdesmit", "četrdesmit", "piecdesmit",
    "sešdesmit", "septiņdesmit", "astoņdesmit", "deviņdesmit"
]

HUNDREDS_PREFIX = [
    "", "", "divsimt", "trīssimt", "četrsimt", "piecsimt",
    "sešsimt", "septiņsimt", "astoņsimt", "deviņsimt"
]

SIMTS_FORMS = {1:"simts", 2:"simtu", 3:"simtu", 4:"simtam", 5:"simtai", 6:"simtu", 7:"simtā", 8:"simti", 9:"simtiem", 10:"simtus", 11:"simtos"}

# Indeclinable compound thousands for 1000–9000 (e.g. "piectūkstoš")
_THOU_COMPOUND = {
    1: "tūkstoš",
    2: "divtūkstoš",
    3: "trīstūkstoš",
    4: "četrtūkstoš",
    5: "piectūkstoš",
    6: "sešttūkstoš",
    7: "septiņtūkstoš",
    8: "astoņtūkstoš",
    9: "deviņtūkstoš",
}


def _ones(n: int, bucket: int) -> str:
    return ONES[n][bucket]


def _teens(n: int) -> str:
    # n is 10..19
    return TEENS[n - 10]


def _below_hundred(n: int, bucket: int) -> str:
    """Spell 1-99 with given bucket on last component."""
    if n == 0:
        return ""
    if 1 <= n <= 9:
        return _ones(n, bucket)
    if 10 <= n <= 19:
        return _teens(n)
    tens = n // 10
    units = n % 10
    if units == 0:
        return TENS_PREFIX[tens]
    else:
        return TENS_PREFIX[tens] + " " + _ones(units, bucket)


def _below_thousand(n: int, bucket: int) -> str:
    """Spell 1-999 with given bucket on last component."""
    if n == 0:
        return ""
    hundreds = n // 100
    remainder = n % 100
    if hundreds == 0:
        return _below_hundred(n, bucket)
    if remainder == 0:
        # Round hundreds — always use nominative "simts" form, not inflected
        if hundreds == 1:
            return "simts"
        else:
            return HUNDREDS_PREFIX[hundreds]
    else:
        if hundreds == 1:
            return "simts " + _below_hundred(remainder, bucket)
        else:
            return HUNDREDS_PREFIX[hundreds] + " " + _below_hundred(remainder, bucket)


def cardinal(n: int, bucket: int = 1) -> str:
    """Spell integer n (0-999999) in Latvian with given bucket."""
    if n == 0:
        return ONES[0][bucket]
    thousands = n // 1000
    remainder = n % 1000
    if thousands == 0:
        return _below_thousand(n, bucket)
    # 1000–9000: use indeclinable compound form (e.g. "piectūkstoš")
    if 1 <= thousands <= 9:
        thou_word = _THOU_COMPOUND[thousands]
        if remainder == 0:
            return thou_word
        return thou_word + " " + _below_thousand(remainder, bucket)
    # 10 000+: spelled-out thousands with "tūkstoši"
    thou_word = _below_thousand(thousands, 1) + " tūkstoši"
    if remainder == 0:
        return thou_word
    return thou_word + " " + _below_thousand(remainder, bucket)
