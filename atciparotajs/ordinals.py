ORD_STEMS = {
    1: "pirm", 2: "otr", 3: "treš", 4: "ceturt", 5: "piekt",
    6: "sest", 7: "septīt", 8: "astot", 9: "devīt", 10: "desmit",
    11: "vienpadsmit", 12: "divpadsmit", 13: "trīspadsmit", 14: "četrpadsmit",
    15: "piecpadsmit", 16: "sešpadsmit", 17: "septiņpadsmit", 18: "astoņpadsmit",
    19: "deviņpadsmit",
}

TENS_ORD_STEMS = {
    2: "divdesmit", 3: "trīsdesmit", 4: "četrdesmit", 5: "piecdesmit",
    6: "sešdesmit", 7: "septiņdesmit", 8: "astoņdesmit", 9: "deviņdesmit",
}

ORDINAL_ENDINGS = {
    1: "ais",
    2: "ā",
    3: "ā",
    4: "ajam",
    5: "ajai",
    6: "o",
    7: "ajā",
    8: "ie",
    9: "ajiem",
    10: "os",
    11: "ajos",
}


def _apply_ending(stem: str, bucket: int) -> str:
    return stem + ORDINAL_ENDINGS[bucket]


def ordinal(n: int, bucket: int = 1) -> str:
    """Spell ordinal n in Latvian with given bucket."""
    if n in ORD_STEMS:
        return _apply_ending(ORD_STEMS[n], bucket)
    if 20 <= n <= 99:
        tens = n // 10
        units = n % 10
        tens_prefix = TENS_ORD_STEMS[tens]
        if units == 0:
            return _apply_ending(tens_prefix, bucket)
        else:
            units_ord = _apply_ending(ORD_STEMS[units], bucket)
            return tens_prefix + " " + units_ord
    if 100 <= n <= 999:
        from atciparotajs.cardinals import HUNDREDS_PREFIX, SIMTS_FORMS
        hundreds = n // 100
        remainder = n % 100
        if hundreds == 1:
            prefix = "simts"
        else:
            prefix = HUNDREDS_PREFIX[hundreds]
        if remainder == 0:
            return _apply_ending("simt", bucket)
        else:
            return prefix + " " + ordinal(remainder, bucket)
    if 1000 <= n:
        from atciparotajs.cardinals import _below_thousand
        thousands = n // 1000
        remainder = n % 1000
        if thousands == 1:
            thou_word = "tūkstoš"
        else:
            thou_word = _below_thousand(thousands, 1) + " tūkstoš"
        if remainder == 0:
            return _apply_ending(thou_word, bucket)
        else:
            return thou_word + "i " + ordinal(remainder, bucket)
    return str(n)
