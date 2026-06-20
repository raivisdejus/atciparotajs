def detect_bucket(word: str) -> int:
    """Detect grammatical bucket 1-11 from Latvian word ending."""
    w = word.lower()
    # Check longest suffixes first
    if w.endswith("iem"):   return 9
    if w.endswith("ām"):    return 9
    if w.endswith("ēm"):    return 9
    if w.endswith("ais"):   return 1
    if w.endswith("am"):    return 4
    if w.endswith("im"):    return 4
    if w.endswith("um"):    return 4
    if w.endswith("ai"):    return 5
    if w.endswith("ei"):    return 5
    if w.endswith("os"):    return 11
    if w.endswith("ās"):    return 11
    if w.endswith("ēs"):    return 11
    # "-as" = nominative feminine plural → bucket 2 for cardinal agreement (e.g. "desas")
    # "-es" = genitive feminine singular → bucket 3 (e.g. "pasaules")
    if w.endswith("as"):    return 2
    if w.endswith("es"):    return 3
    if w.endswith("us"):    return 10
    if w.endswith("ā"):     return 7
    if w.endswith("ī"):     return 7
    if w.endswith("ē"):     return 7
    # Genitive masculine sg: plain vowel + j + a (e.g. "maija" = gen of "maijs")
    if (len(w) >= 3 and w.endswith("a") and w[-2] == "j" and w[-3] in "aeiou"):
        return 3
    if w.endswith("a"):     return 2
    if w.endswith("e"):     return 2
    if w.endswith("i"):     return 8
    if w.endswith("u"):     return 6
    if w.endswith("s"):     return 1
    return 1
