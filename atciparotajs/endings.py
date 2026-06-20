def detect_bucket(word: str) -> int:
    """Detect grammatical bucket 1-13 from Latvian word ending.

    Buckets:
      1  nominative masculine singular     (-s, -is, -us)
      2  nominative feminine singular      (-a, -e)
      3  genitive/nominative feminine      (-as, -es)
      4  dative masculine singular         (-am, -im, -um)
      5  dative feminine singular          (-ai, -ei)
      6  accusative singular / genitive pl (-u)
      7  locative singular                 (-ā, -ī, -ē)
      8  nominative masculine plural       (-i)
      9  dative masculine plural           (-iem)
      10 accusative masculine plural       (-us)
      11 locative masculine plural         (-os)
      12 dative feminine plural            (-ām, -ēm)
      13 locative feminine plural          (-ās, -ēs)
    """
    w = word.lower()
    # Check longest suffixes first to avoid prefix mismatches
    if w.endswith("iem"):   return 9   # dat masc pl
    if w.endswith("ām"):    return 12  # dat fem pl
    if w.endswith("ēm"):    return 12  # dat fem pl
    if w.endswith("ais"):   return 1   # nom masc sg definite (adjectives/ordinals)
    if w.endswith("am"):    return 4   # dat masc sg
    if w.endswith("im"):    return 4   # dat masc sg
    if w.endswith("um"):    return 4   # dat masc sg
    if w.endswith("ai"):    return 5   # dat fem sg
    if w.endswith("ei"):    return 5   # dat fem sg
    if w.endswith("os"):    return 11  # loc masc pl
    if w.endswith("ās"):    return 13  # loc fem pl
    if w.endswith("ēs"):    return 13  # loc fem pl
    if w.endswith("as"):    return 3   # gen fem sg / nom fem pl
    if w.endswith("es"):    return 3   # gen fem sg / nom fem pl
    if w.endswith("us"):    return 10  # acc masc pl
    if w.endswith("ā"):     return 7   # loc sg
    if w.endswith("ī"):     return 7   # loc sg
    if w.endswith("ē"):     return 7   # loc sg
    # Genitive masculine sg: vowel + j + a (e.g. "maija" = gen of "maijs")
    if (len(w) >= 3 and w.endswith("a") and w[-2] == "j" and w[-3] in "aeiou"):
        return 3
    if w.endswith("a"):     return 2   # nom fem sg
    if w.endswith("e"):     return 2   # nom fem sg
    if w.endswith("i"):     return 8   # nom masc pl (ambiguous with acc masc sg)
    if w.endswith("u"):     return 6   # acc sg / gen pl
    if w.endswith("s"):     return 1   # nom masc sg
    return 1
