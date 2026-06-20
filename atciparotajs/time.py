from atciparotajs.cardinals import ONES, _below_hundred

# Locative forms of clock hours 1-12.
# Hours 1-9 use ONES table; 10-12 need explicit forms because TEENS are indeclinable.
_HOUR_LOC = {
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
}


def clock_time(h: int, m: int) -> str:
    """Convert clock time to spoken Latvian (e.g. 10:45 → 'desmitos četrdesmit piecās')."""
    hour_key = h % 12 or 12
    hour_str = _HOUR_LOC.get(hour_key, str(h))
    if m == 0:
        return hour_str
    min_str = _below_hundred(m, 13)
    return f"{hour_str} {min_str}"
