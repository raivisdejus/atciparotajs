_VALS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_int(s: str) -> int:
    if not s or not all(c in _VALS for c in s):
        return -1
    result = 0
    prev = 0
    for c in reversed(s):
        curr = _VALS[c]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr
    if result <= 0:
        return -1
    return result


def is_valid_roman(s: str) -> bool:
    return roman_to_int(s) > 0
