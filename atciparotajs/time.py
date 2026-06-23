from atciparotajs.cardinals import ONES, _below_hundred

# Locative forms of clock hours 0-23 (24-hour format).
_HOUR_LOC = {
    0:  "nullē",
    1:  "vienos",
    2:  ONES[2][11],   # "divos"
    3:  ONES[3][11],   # "trijos"
    4:  ONES[4][11],   # "četros"
    5:  ONES[5][11],   # "piecos"
    6:  ONES[6][11],   # "sešos"
    7:  ONES[7][11],   # "septiņos"
    8:  ONES[8][11],   # "astoņos"
    9:  ONES[9][11],   # "deviņos"
    10: "desmitos",
    11: "vienpadsmitos",
    12: "divpadsmitos",
    13: "trīspadsmitos",
    14: "četrpadsmitos",
    15: "piecpadsmitos",
    16: "sešpadsmitos",
    17: "septiņpadsmitos",
    18: "astoņpadsmitos",
    19: "deviņpadsmitos",
    20: "divdesmitos",
    21: "divdesmit vienos",
    22: "divdesmit divos",
    23: "divdesmit trijos",
}


def clock_time(h: int, m: int) -> str:
    """Convert clock time to spoken Latvian (e.g. 10:45 → 'desmitos četrdesmit piecās')."""
    hour_str = _HOUR_LOC.get(h, str(h))
    if m == 0:
        return hour_str
    min_str = _below_hundred(m, 13)
    return f"{hour_str} {min_str}"
