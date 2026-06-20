from atciparotajs.cardinals import cardinal

# Buckets that indicate feminine gender
_FEMININE_BUCKETS = {2, 3, 5, 12, 13}


def fraction(integer_part: int, decimal_str: str, bucket: int = 1) -> str:
    """Convert decimal number to Latvian words.
    Both integer and decimal parts use nominative form matching the noun's gender:
    feminine (buckets 2,3,5,12,13) → bucket 2; masculine → bucket 1.
    """
    gender_bucket = 2 if bucket in _FEMININE_BUCKETS else 1
    dec_int = int(decimal_str)
    parts = [cardinal(integer_part, gender_bucket), "komats", cardinal(dec_int, gender_bucket)]
    return " ".join(parts)
