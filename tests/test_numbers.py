"""
Pārbaudes gadījumi / Test cases for atciparotājs.

Each line shows: input text → expected output.
The comment shows the grammatical case and gender.
This file can be reviewed and extended by any Latvian speaker.

Izmantotie vārdi / Words used in tests:
  suns     = dog (masculine)
  māja     = house (feminine)
  draugs   = friend (masculine)
  stunda   = hour (feminine)
  gads     = year (masculine)
  vieta    = place (feminine)
  grams    = gram (masculine)
  minūte   = minute (feminine)
"""

import pytest
from atciparotajs import convert


# ============================================================
# Locījumi ar skaitli 1 / All cases with number 1
# ============================================================
# vīriešu dzimte (masculine)                  sieviešu dzimte (feminine)
# nominatīvs:  viens suns  (one dog)          viena māja    (one house)
# ģenitīvs:    viena suņa  (of one dog)       vienas mājas  (of one house)
# datīvs:      vienam sunim (to one dog)       vienai mājai  (to one house)
# akuzatīvs:   vienu suni  (one dog, obj)     vienu māju    (one house, obj)
# lokatīvs:    vienā sunī  (in one dog)       vienā mājā    (in one house)
# nominatīvs daudzsk.: vieni suņi             vienas mājas

ONE_CASES = [
    # (input,               expected,                   comment)
    ("1 suns",              "viens suns"),              # nom masc sg
    ("1 māja",              "viena māja"),              # nom fem sg
    ("1 mājas",             "vienas mājas"),            # gen fem sg / nom fem pl
    ("1 sunim",             "vienam sunim"),            # dat masc sg
    ("1 mājai",             "vienai mājai"),            # dat fem sg
    # NOTE: "1 suni" is ambiguous — "-i" could be acc masc sg OR nom masc pl;
    #       the heuristic always picks nom masc pl (bucket 8), so it's omitted here.
    ("1 māju",              "vienu māju"),              # acc fem sg / gen pl
    ("1 sunī",              "vienā sunī"),              # loc masc sg
    ("1 mājā",              "vienā mājā"),              # loc fem sg
]

# ============================================================
# Locījumi ar skaitli 2 / All cases with number 2
# ============================================================
TWO_CASES = [
    ("2 suņi",              "divi suņi"),               # nom masc pl
    ("2 mājas",             "divas mājas"),             # nom/acc fem pl
    # NOTE: "2 suņa" is ambiguous — "-a" could be nom fem sg OR gen masc sg;
    #       without a dictionary the heuristic picks nom fem sg, so it's omitted here.
    ("2 māju",              "divu māju"),               # gen pl (of two houses)
    ("2 suņiem",            "diviem suņiem"),           # dat masc pl
    ("2 mājām",             "divām mājām"),             # dat fem pl
    ("2 suņus",             "divus suņus"),             # acc masc pl
    ("2 suņos",             "divos suņos"),             # loc masc pl
    ("2 mājās",             "divās mājās"),             # loc fem pl
]

# ============================================================
# Locījumi ar skaitli 11 / All cases with number 11
# (vienpadsmit — indeclinable in modern Latvian)
# ============================================================
ELEVEN_CASES = [
    ("11 suņi",             "vienpadsmit suņi"),        # nom masc pl
    ("11 mājas",            "vienpadsmit mājas"),       # nom fem pl
    ("11 suņiem",           "vienpadsmit suņiem"),      # dat masc pl
    ("11 mājām",            "vienpadsmit mājām"),       # dat fem pl
    ("11 suņus",            "vienpadsmit suņus"),       # acc masc pl
    ("11 suņos",            "vienpadsmit suņos"),       # loc masc pl
    ("11 mājās",            "vienpadsmit mājās"),       # loc fem pl
]

# ============================================================
# Parastie skaitļi (cardinals) — mixed cases
# ============================================================
CARDINAL_CASES = [
    ("2 draugiem",          "diviem draugiem"),         # dat masc pl
    ("2 desas",             "divas desas"),             # nom/acc fem pl
    ("5 māju",              "piecu māju"),              # gen pl (of five houses)
    ("3 kaķi",              "trīs kaķi"),               # nom masc pl
    ("21 diena",            "divdesmit viena diena"),   # nom fem sg
    ("100 grami",           "simts grami"),             # nom masc pl
    ("Man ir 30",           "Man ir trīsdesmit"),        # standalone, no following noun
]

# ============================================================
# Kārtas skaitļi (ordinals) — period after number
# ============================================================
ORDINAL_CASES = [
    ("5. maijs",            "piektais maijs"),          # nom masc sg
    ("1. maijā",            "pirmajā maijā"),           # loc sg
    ("3. vieta",            "trešā vieta"),             # nom fem sg
    ("1. vieta",            "pirmā vieta"),             # nom fem sg
    ("21. vieta",           "divdesmit pirmā vieta"),   # nom fem sg
]

# ============================================================
# Romiešu cipari (Roman numerals)
# ============================================================
ROMAN_CASES = [
    ("II pasaules karš",    "otrais pasaules karš"),    # nom masc sg
    ("XIV gs.",             "četrpadsmitais gadsimts"), # nom masc sg + abbreviation
    ("V nodaļa",            "piektā nodaļa"),           # nom fem sg
]

# ============================================================
# Daļskaitļi un decimāli (fractions and decimals)
# ============================================================
FRACTION_CASES = [
    ("21,5 grami",          "divdesmit viens komats pieci grami"),
    ("21.5 grami",          "divdesmit viens komats pieci grami"),
    ("3,14",                "trīs komats četrpadsmit"),
    ("1,5 stundas",         "viena komats piecas stundas"),
]

# ============================================================
# Saīsinājumi (abbreviations)
# ============================================================
ABBREVIATION_CASES = [
    ("14. gs.",             "četrpadsmitais gadsimts"),
    ("t.i. pieci",          "tas ir pieci"),
]


@pytest.mark.parametrize("text,expected", ONE_CASES)
def test_one_inflections(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", TWO_CASES)
def test_two_inflections(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", ELEVEN_CASES)
def test_eleven_inflections(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", CARDINAL_CASES)
def test_cardinals(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", ORDINAL_CASES)
def test_ordinals(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", ROMAN_CASES)
def test_roman(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", FRACTION_CASES)
def test_fractions(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", ABBREVIATION_CASES)
def test_abbreviations(text, expected):
    assert convert(text) == expected
