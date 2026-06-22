from atciparotajs.cardinals import cardinal

# Buckets that indicate feminine gender
_FEMININE_BUCKETS = {2, 3, 5, 12, 13}


# For plural buckets the integer part stays in nominative singular (gender-matched);
# for singular/accusative buckets the integer part follows the same case as the noun.
_PLURAL_BUCKETS = {3, 8, 9, 11}


def fraction(integer_part: int, decimal_str: str, bucket: int = 1) -> str:
    gender_bucket = 2 if bucket in _FEMININE_BUCKETS else 1
    int_bucket = gender_bucket if bucket in _PLURAL_BUCKETS else bucket
    dec_int = int(decimal_str)
    parts = [cardinal(integer_part, int_bucket), "komats", cardinal(dec_int, bucket)]
    return " ".join(parts)
