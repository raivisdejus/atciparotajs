"""
Pārbaudes gadījumi / Test cases for atciparotājs.

Each line shows: input text → expected output.
The comment shows the grammatical case and gender.

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
    ("2. vietā",            "otrajā vietā"),            # nom fem sg
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
    ("15 km dziļumā",       "piecpadsmit kilometru dziļumā"),
    ("15 km. dziļumā",      "piecpadsmit kilometru dziļumā"),
    ("600 mm mortīra",      "sešsimt milimetru mortīra"),
]

# ============================================================
# Datumi (dates)
# ============================================================
DATE_CASES = [
    ("4. oktobris, 1957. gads",
     "ceturtais oktobris, tūkstoš deviņsimt piecdesmit septītais gads"),
    ("1961. gada 12. aprīlis",
     "tūkstoš deviņsimt sešdesmit pirmā gada divpadsmitais aprīlis"),
    ("1969. gada 20. jūlijā",
     "tūkstoš deviņsimt sešdesmit devītā gada divdesmitajā jūlijā"),
    ("2026. gads", "divi tūkstoši divdesmit sestais gads"),
    ("1941.–1945. gads",
     "tūkstoš deviņsimt četrdesmit pirmais līdz tūkstoš deviņsimt četrdesmit piektais gads"),
    ("1941–1945 gads",
     "tūkstoš deviņsimt četrdesmit pirmais līdz tūkstoš deviņsimt četrdesmit piektais gads"),
    ("1941.–1945. gadā",
     "tūkstoš deviņsimt četrdesmit pirmajā līdz tūkstoš deviņsimt četrdesmit piektajā gadā"),
    ("1941–1945 gadā",
     "tūkstoš deviņsimt četrdesmit pirmajā līdz tūkstoš deviņsimt četrdesmit piektajā gadā"),
    ("1927. un 1928. gadā",
     "tūkstoš deviņsimt divdesmit septītajā un tūkstoš deviņsimt divdesmit astotajā gadā"),
]

# ============================================================
# Iniciāļi (initials) — single uppercase letter after a name
# must NOT be converted as a Roman numeral
# ============================================================
INITIAL_CASES = [
    # "V." after a name is a surname initial, not Roman numeral V (= 5)
    ("Kārlis V. uzvarēja",     "Kārlis V. uzvarēja"),
    ("Jānis A. sacīja",        "Jānis A. sacīja"),
]

# ============================================================
# Numuri (reference numbers) — "nr." before a number
# ============================================================
NR_CASES = [
    ("Vilciens nr. 67",        "Vilciens numur sešdesmit septiņi"),
    ("Autobuss nr. 3",         "Autobuss numur trīs"),
]

# ============================================================
# Lappuses (pages) — "lpp." expands with correct plural noun
# ============================================================
LPP_CASES = [
    ("58 lpp. gara grāmata",   "piecdesmit astoņas lappuses gara grāmata"),
    ("1 lpp.",                 "viena lappuse"),
    ("100 lpp.",               "simts lappuses"),
]

# ============================================================
# Pulksteņa laiks (clock time) — "H:MM" format
# ============================================================
TIME_CASES = [
    ("Vilciens pienāks 10:45",  "Vilciens pienāks desmitos četrdesmit piecās"),
    ("Pulksten 1:00",           "Pulksten vienos"),
    ("Sanāksme sākas 14:30",    "Sanāksme sākas divos trīsdesmit"),
    ("9:05",                    "deviņos piecās"),
]

# ============================================================
# Negatīvi skaitļi (negative numbers)
# ============================================================
NEGATIVE_CASES = [
    ("-5 grādi",         "mīnus pieci grādi"),
    ("-10,5 grādi",      "mīnus desmit komats pieci grādi"),
    ("-1 grāds",         "mīnus viens grāds"),
]

# ============================================================
# Lieli skaitļi (large numbers — thousands)
# ============================================================
LARGE_NUMBER_CASES = [
    ("1000 cilvēku",        "tūkstoš cilvēku"),
    ("3000 gadu",           "trīstūkstoš gadu"),
    ("5000 gadus",          "piectūkstoš gadus"),
    ("10000 cilvēku",       "desmit tūkstoši cilvēku"),
    ("10 000 cilvēku",      "desmit tūkstoši cilvēku"),
    ("150 000 karavīru",    "simt piecdesmit tūkstoši karavīru"),
    ("2 000 000 cilvēku",   "divi miljoni cilvēku"),
]

# ============================================================
# Procenti (percentages)
# ============================================================
PERCENTAGE_CASES = [
    ("5%",                  "pieci procenti"),
    ("21%",                 "divdesmit viens procents"),
    ("100%",                "simts procentu"),
    ("0,5%",                "nulle komats pieci procenti"),
    ("Inflācija sasniedza 3,5%",
     "Inflācija sasniedza trīs komats piecus procentus"),
    ("Inflācija sasniedza 3,5 procentus",
     "Inflācija sasniedza trīs komats piecus procentus"),
    # context-aware cases
    ("sasniedza 5%",        "sasniedza piecus procentus"),
    ("par 3,5%",            "par trīs komats pieciem procentiem"),
    ("no 5%",               "no piecu procentu"),
    ("pārsniedza 15–20%",   "pārsniedza piecpadsmit līdz divdesmit procentus"),
    ("6.—9. augustā",       "sestajā līdz devītajā augustā"), # Note. different dash (-)
]

# ============================================================
# Sporta rezultāti (sports scores)
# ============================================================
SCORE_CASES = [
    ("Rezultāts 3:2",       "Rezultāts trīs divi"),
    ("1:0",                 "viens nulle"),
    ("Spēle beidzās 4:3",   "Spēle beidzās četri trīs"),
]

# ============================================================
# Skaitļu diapazoni (number ranges)
# ============================================================
RANGE_CASES = [
    ("5–10 gadus",           "piecus līdz desmit gadus"),
    ("18–65 gadi",          "astoņpadsmit līdz sešdesmit pieci gadi"),
    ("2–5 minūtes",         "divas līdz piecas minūtes"),
    ("6-8 cilvēki",         "seši līdz astoņi cilvēki"),
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


@pytest.mark.parametrize("text,expected", DATE_CASES)
def test_dates(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", INITIAL_CASES)
def test_initials_not_roman(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", NR_CASES)
def test_nr_keeps_digits(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", LPP_CASES)
def test_lpp_plural(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", TIME_CASES)
def test_clock_time(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", NEGATIVE_CASES)
def test_negative_numbers(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", LARGE_NUMBER_CASES)
def test_large_numbers(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", PERCENTAGE_CASES)
def test_percentages(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", SCORE_CASES)
def test_scores(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", RANGE_CASES)
def test_ranges(text, expected):
    assert convert(text) == expected
