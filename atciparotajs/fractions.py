from atciparotajs.cardinals import cardinal


def fraction(integer_part: int, decimal_str: str, bucket: int = 1) -> str:
    """Convert decimal number to Latvian words.
    Integer part and decimal part always use bucket 1 (nominative masculine).
    """
    dec_int = int(decimal_str)
    parts = [cardinal(integer_part, 1), "komats", cardinal(dec_int, 1)]
    return " ".join(parts)
