ABBREVIATIONS = {
    "gs.":    "gadsimts",
    "g.":     "gads",
    "km.":    "kilometrs",
    "m.":     "metrs",
    "kg.":    "kilograms",
    "mg.":    "miligrams",
    "ml.":    "mililītrs",
    "l.":     "lītrs",
    "nr.":    "numurs",
    "lpp.":   "lappuse",
    "u.c.":   "un citi",
    "u.tml.": "un tamlīdzīgi",
    "t.i.":   "tas ir",
    "pr.Kr.": "pirms Kristus",
    "p.Kr.":  "pēc Kristus",
}


def expand_abbreviations(text: str) -> str:
    for abbr in sorted(ABBREVIATIONS, key=len, reverse=True):
        text = text.replace(abbr, ABBREVIATIONS[abbr])
    return text
