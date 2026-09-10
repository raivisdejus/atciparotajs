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
from atciparotajs import convert, currency
from atciparotajs.cardinals import cardinal

# NOTE: All test-case constants must be defined here, before any test function.


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
    ("11 māju",             "vienpadsmit māju"),
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
    ("100 gramu",           "simts gramu"),             # gen masc pl
    ("Man ir 30",           "Man ir trīsdesmit"),       # standalone, no following noun
    ("Viņam ir 25 gadi",    "Viņam ir divdesmit pieci gadi"),   # age in sentence
    ("Viņai bija 18 gadu",  "Viņai bija astoņpadsmit gadu"),    # gen pl age
    ("apmēram 200 cilvēku", "apmēram divsimt cilvēku"),         # approximation word before
    ("aptuveni 5 km",       "aptuveni pieci kilometri"),        # approximation word before
    ("5 gadus vecs",        "piecus gadus vecs"),               # acc + adjective
    ("30 gadus veca",       "trīsdesmit gadus veca"),           # acc + fem adjective
]

# ============================================================
# Kārtas skaitļi (ordinals) — period after number
# ============================================================
ORDINAL_CASES = [
    ("5. maijs",            "piektais maijs"),          # nom masc sg
    ("1. maijā",            "pirmajā maijā"),           # loc sg
    ("3. vieta",            "trešā vieta"),             # nom fem sg
    ("3. vietā",            "trešajā vietā"),           # loc fem sg
    ("2. vieta",            "otrā vieta"),              # loc fem sg
    ("2. vietā",            "otrajā vietā"),            # nom fem sg
    ("1. vieta",            "pirmā vieta"),             # nom fem sg
    ("1. vietā",            "pirmajā vietā"),  # loc fem sg
    ("21 vieta",            "divdesmit viena vieta"),   # nom fem sg
    ("21. vieta",           "divdesmit pirmā vieta"),   # nom fem sg
    ("7. nodaļa",           "septītā nodaļa"),          # nom fem sg
    ("5. nodaļa",           "piektā nodaļa"),           # nom fem sg
    ("10. nodaļa",          "desmitā nodaļa"),          # nom fem sg
    ("100. jubileja",       "simtā jubileja"),          # nom fem sg
    ("1000. diena",         "tūkstošā diena"),          # nom fem sg
    ("janvāra 15.",         "janvāra piecpadsmitais"),  # standalone trailing ordinal
    ("ierādīja 3.",         "ierādīja trešais"),        # standalone trailing ordinal
]

# ============================================================
# Romiešu cipari (Roman numerals)
# ============================================================
ROMAN_CASES = [
    ("II pasaules karš",    "otrais pasaules karš"),        # nom masc sg
    ("XIV gs.",             "četrpadsmitais gadsimts"),     # nom masc sg + abbreviation
    ("pārvaldes V nodaļa",  "pārvaldes piektā nodaļa"),               # nom fem sg
    ("V nodaļa",            "piektā nodaļa"),               # nom fem sg
    ("XIX gs.",             "deviņpadsmitais gadsimts"),    # 19th century
    ("XXI gs.",             "divdesmit pirmais gadsimts"),  # 21st century
    ("XX gadsimtā",         "divdesmitajā gadsimtā"),       # loc sg (in the 20th century)
    ("IV sējums",           "ceturtais sējums"),            # nom masc sg
    ("III daļa",            "trešā daļa"),                  # nom fem sg
    ("V pants",             "piektais pants"),              # nom masc sg
    ("X klasē",             "desmitajā klasē"),             # loc fem sg
]

# ============================================================
# Lielo burtu saīsinājumi (uppercase acronyms) — must NOT be read
# as Roman numerals when no context word follows
# ============================================================
ACRONYM_NOT_ROMAN_CASES = [
    ("VID",                  "VID"),
    ("VIDM",                 "VIDM"),
    ("LV",                   "LV"),
    ("ID",                   "ID"),
    ("CV",                   "CV"),
    ("MI",                   "MI"),
    ("DI",                   "DI"),
    ("LIC",                  "LIC"),
    ("CD",                   "CD"),
    ("DVD",                  "DVD"),
    ("VID Muitas pārvalde",  "VID Muitas pārvalde"),
    ("LV rullē",             "LV rullē"),
]

# ============================================================
# Daļskaitļi un decimāli (fractions and decimals)
# ============================================================
FRACTION_CASES = [
    ("21,5 grami",          "divdesmit viens komats pieci grami"),
    ("21.5 grami",          "divdesmit viens komats pieci grami"),
    ("3,14",                "trīs komats četrpadsmit"),
    ("1,5 stundas",         "viena komats piecas stundas"),
    ("2,5 stundas",         "divas komats piecas stundas"),
    ("1,25 stundas",        "viena komats divdesmit piecas stundas"),
    ("0,5",                 "nulle komats pieci"),
]

# ============================================================
# Decimāldaļas sākuma nulles (leading zeros in the decimal part)
# ============================================================
DECIMAL_LEADING_ZERO_CASES = [
    ("1237,06 vienības", "tūkstoš divsimt trīsdesmit septiņas komats nulle sešas vienības"),
    ("1237,6 vienības",  "tūkstoš divsimt trīsdesmit septiņas komats sešas vienības"),
    ("1237,60 vienības", "tūkstoš divsimt trīsdesmit septiņas komats sešdesmit vienības"),
    ("10,01 punkti",     "desmit komats nulle vieni punkti"),
    ("10,01 punkts",     "desmit komats nulle viens punkts"),
    ("0,05",         "nulle komats nulle pieci"),
    ("0,5",          "nulle komats pieci"),
    ("2,003 kg",     "divi komats nulle nulle trīs kilogrami"),
    ("0,001 g",      "nulle komats nulle nulle viens grams"),
    ("1,00 kg",      "viens komats nulle nulle kilogramu"),
    ("0,05%",        "nulle komats nulle pieci procenti"),
]

# ============================================================
# Decimāli ar mērvienību saīsinājumiem (decimal amounts + unit abbreviations)
# ============================================================
DECIMAL_UNIT_CASES = [
    ("2,5 kg",     "divi komats pieci kilogrami"),
    ("1,5 km",     "viens komats pieci kilometri"),
    ("1,1 kg",     "viens komats viens kilograms"),
    ("2,10 kg",    "divi komats desmit kilogramu"),
    ("2,5 m²",     "divi komats pieci kvadrātmetri"),
    ("1,5 km/h",   "viens komats pieci kilometri stundā"),
    ("12,5 lpp.",  "divpadsmit komats piecas lappuses"),
    ("1,5 T",      "viena komats piecas tonnas"),
    ("2,1 T",      "divas komats viena tonna"),
    ("36,6°C",     "trīsdesmit seši komats seši grādi"),
    ("21,1°C",     "divdesmit viens komats viens grāds"),
    ("2,5 kg maisā", "divi komats pieci kilogrami maisā"),
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
    ("9 km²",               "deviņi kvadrātkilometri"),
    ("1 km²",               "viens kvadrātkilometrs"),
    ("10 km²",              "desmit kvadrātkilometru"),
    ("5 m²",                "pieci kvadrātmetri"),
    ("1 m²",                "viens kvadrātmetrs"),
    ("100 m²",              "simts kvadrātmetru"),
    ("3 m³",                "trīs kubikmetri"),
    ("1 m³",                "viens kubikmetrs"),
    ("20 m³",               "divdesmit kubikmetru"),
    ("100 g kultūras",      "simts gramu kultūras"),
    ("10 ml",               "desmit mililitru"),
    ("10 cm",               "desmit centimetru"),
    ("10 mm",               "desmit milimetru"),
]

# ============================================================
# Vārdi, kas nav saīsinājumi (words that must not be treated as abbreviations)
# ============================================================
NON_ABBREVIATION_CASES = [
    ("mežiem.",             "mežiem."),
    ("koks aug.",           "koks aug."),
    ("koeficientiem.",      "koeficientiem."),
    ("cilvēkiem.",          "cilvēkiem."),
    ("un tad vēl.",         "un tad vēl."),
    ("liels ceļojums.",     "liels ceļojums."),
    ("viņi devās mājup.",   "viņi devās mājup."),
    ("tas notika rudenī.",  "tas notika rudenī."),
    ("labs darbs, kolēģi.", "labs darbs, kolēģi."),
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
    ("1941 – 1945 gadā",
     "tūkstoš deviņsimt četrdesmit pirmajā līdz tūkstoš deviņsimt četrdesmit piektajā gadā"),
    ("1927. un 1928. gadā",
     "tūkstoš deviņsimt divdesmit septītajā un tūkstoš deviņsimt divdesmit astotajā gadā"),
    ("no 1942. gada 4. jūnija līdz 7. jūnijam",
     "no tūkstoš deviņsimt četrdesmit otrā gada ceturtā jūnija līdz septītajam jūnijam"),
]

# ============================================================
# Iniciāļi (initials) — single uppercase letter after a name
# must NOT be converted as a Roman numeral
# ============================================================
INITIAL_CASES = [
    # "V." after a name is a surname initial, not Roman numeral V (= 5)
    ("Kārlis V. uzvarēja",     "Kārlis V. uzvarēja"),
    ("V. Bērziņš uzvarēja",    "V. Bērziņš uzvarēja"),
    ("Jānis A. sacīja",        "Jānis A. sacīja"),
]

# ============================================================
# Numuri (reference numbers) — "nr." before a number
# ============================================================
NR_CASES = [
    ("Vilciens nr. 67",        "Vilciens numur sešdesmit septiņi"),
    ("Autobuss nr. 3",         "Autobuss numur trīs"),
    ("Autobuss Nr. 3",         "Autobuss numur trīs"),
]

# ============================================================
# Lappuses (pages) — "lpp." expands with correct plural noun
# ============================================================
LPP_CASES = [
    ("58 lpp. gara grāmata",   "piecdesmit astoņas lappuses gara grāmata"),
    ("1 lpp.",                 "viena lappuse"),
    ("100 lpp.",               "simts lappušu"),                # gen pl
    ("11 lpp.",                "vienpadsmit lappušu"),          # teen → gen pl
    ("21 lpp.",                "divdesmit viena lappuse"),      # ends-in-1 excl. 11 → sg
]

# ============================================================
# Pulksteņa laiks (clock time) — "H:MM" format
# ============================================================
TIME_CASES = [
    ("Vilciens pienāks 10:45",  "Vilciens pienāks desmitos četrdesmit piecās"),
    ("Pulksten 1:00",           "Pulksten vienos"),
    ("Sanāksme sākas 14:30",    "Sanāksme sākas četrpadsmitos trīsdesmit"),
    ("9:05",                    "deviņos piecās"),
    ("8:00",                    "astoņos"),
    ("12:00",                   "divpadsmitos"),
    ("23:59",                   "divdesmit trijos piecdesmit deviņās"),
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
    ("6000 gadu",           "seštūkstoš gadu"),
    ("6420 cilvēku",        "seštūkstoš četrsimt divdesmit cilvēku"),
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
    ("sasniedza 3,5%",      "sasniedza trīs komats piecus procentus"),
    ("sasniedza 2.5%",      "sasniedza divus komats piecus procentus"),
    ("sasniedza 2,5% slieksni", "sasniedza divu komats piecu procentu slieksni"),
    ("sasniedza 3,5 procentus", "sasniedza trīs komats piecus procentus"),
    # context-aware cases
    ("sasniedza 5%",           "sasniedza piecus procentus"),
    ("par 3,5%",               "par trīs komats pieciem procentiem"),
    ("no 1%",                  "no viena procenta"),
    ("no 5%",                  "no pieciem procentiem"),
    ("pārsniedza 5% slieksni", "pārsniedza piecu procentu slieksni"),
    ("pārsniedza 15–20%",      "pārsniedza piecpadsmit līdz divdesmit procentus"),
    ("6.—9. augustā",          "sestajā līdz devītajā augustā"), # Note. different dash (-)
]

# ============================================================
# Sporta rezultāti (sports scores)
# ============================================================
SCORE_CASES = [
    ("Rezultāts 3:2",       "Rezultāts trīs divi"),
    ("1:0",                 "viens nulle"),
    ("Spēle beidzās 4:3",   "Spēle beidzās četri trīs"),
    ("Rezultāts: 2:1",      "Rezultāts: divi viens"),   # colon after label word
]

# ============================================================
# Skaitļu diapazoni (number ranges)
# ============================================================
RANGE_CASES = [
    ("5–10 gadus",          "piecus līdz desmit gadus"),
    ("18–65 gadi",          "astoņpadsmit līdz sešdesmit pieci gadi"),
    ("2–5 minūtes",         "divas līdz piecas minūtes"),
    ("5–10 minūtes",        "piecas līdz desmit minūtes"),
    ("6-8 cilvēki",         "seši līdz astoņi cilvēki"),
    ("6-8 cilvēkiem",       "sešiem līdz astoņiem cilvēkiem"),
    ("5–10 cilvēki",        "pieci līdz desmit cilvēki"),
    # written-out unit: the decimal must not be torn apart by the range split
    ("0–2 milimetri",       "nulle līdz divi milimetri"),
    ("0–1,5 milimetri",     "nulle līdz viens komats pieci milimetri"),
    ("0–1,5 milimetru",     "nulle līdz vienu komats piecu milimetru"),
    ("1,5–3 milimetri",     "viens komats pieci līdz trīs milimetri"),
    ("2,5–3,5 kilogrami",   "divi komats pieci līdz trīs komats pieci kilogrami"),
    ("0…2 milimetri",       "nulle līdz divi milimetri"),      # ellipsis character
    ("0...1,5 milimetri",   "nulle līdz viens komats pieci milimetri"),  # three dots
    ("Svētdien: pārsvarā sauss, 0–1,5 milimetri;",
     "Svētdien: pārsvarā sauss, nulle līdz viens komats pieci milimetri;"),
]

# ============================================================
# Diapazoni ar mērvienību saīsinājumiem (ranges + unit abbreviations)
# ============================================================
# The noun agrees with the last number; both numbers take its case.
UNIT_RANGE_CASES = [
    ("0–2 mm",      "nulle līdz divi milimetri"),
    ("0-2 mm",      "nulle līdz divi milimetri"),      # plain hyphen
    ("0 – 2 mm",    "nulle līdz divi milimetri"),      # spaced dash
    ("0…2 mm",      "nulle līdz divi milimetri"),      # ellipsis character
    ("0...2 mm",    "nulle līdz divi milimetri"),      # three dots
    ("0–1,5 mm",    "nulle līdz viens komats pieci milimetri"),
    ("1,5–3 mm",    "viens komats pieci līdz trīs milimetri"),
    ("10–15 mm",    "desmit līdz piecpadsmit milimetru"),
    ("20–21 mm",    "divdesmit līdz divdesmit viens milimetrs"),
    ("3–5 km",      "trīs līdz pieci kilometri"),
    ("10–20 cm",    "desmit līdz divdesmit centimetru"),
    ("Sestdien: pārsvarā sauss, 0–2 mm; vējš 3–5 m/s.",
     "Sestdien: pārsvarā sauss, nulle līdz divi milimetri; vējš trīs līdz pieci metri sekundē."),
    # ranges without a unit abbreviation must stay untouched
    ("5–10 cilvēki",   "pieci līdz desmit cilvēki"),
    ("5–10%",          "piecus līdz desmit procentus"),
]

# ============================================================
# Telefona numuri (phone numbers)
# ============================================================
PHONE_CASES = [
    ("tel. 67 030 638",      "seši septiņi nulle trīs nulle seši trīs astoņi"),
    ("tel: 67 030 638",      "seši septiņi nulle trīs nulle seši trīs astoņi"),
    ("tel 67 030 638",       "seši septiņi nulle trīs nulle seši trīs astoņi"),
    ("tel.67030638",         "seši septiņi nulle trīs nulle seši trīs astoņi"),
    ("tālr. 67030638",       "seši septiņi nulle trīs nulle seši trīs astoņi"),
    ("mob. 67 030 638",      "seši septiņi nulle trīs nulle seši trīs astoņi"),
    ("mob: 67030638",        "seši septiņi nulle trīs nulle seši trīs astoņi"),
    ("+371 67 030 638",      "seši septiņi nulle trīs nulle seši trīs astoņi"),
    ("+37167030638",         "seši septiņi nulle trīs nulle seši trīs astoņi"),
    ("tel. +371 67 030 638", "seši septiņi nulle trīs nulle seši trīs astoņi"),
    ("{phone:67030638}",     "seši septiņi nulle trīs nulle seši trīs astoņi"),
]


# ============================================================
# Svars (weight) — kg (subtitle-common unit)
# ============================================================
WEIGHT_CASES = [
    ("1 kg",        "viens kilograms"),
    ("2 kg",        "divi kilogrami"),
    ("5 kg",        "pieci kilogrami"),
    ("10 kg",       "desmit kilogramu"),
    ("11 kg",       "vienpadsmit kilogramu"),
    ("21 kg",       "divdesmit viens kilograms"),
    ("100 kg",      "simts kilogramu"),
]

# ============================================================
# Sērijas un daļas (episodes and parts — subtitle-common ordinals)
# ============================================================
SUBTITLE_ORDINAL_CASES = [
    ("2. sezona",           "otrā sezona"),
    ("3. sērija",           "trešā sērija"),
    ("1. sērijā",           "pirmajā sērijā"),
    ("10. sērija",          "desmitā sērija"),
    ("21. sērija",          "divdesmit pirmā sērija"),
    ("4. daļa",             "ceturtā daļa"),
    ("sezona 2, 3. sērija", "otrā sezona, trešā sērija"),
]

# ============================================================
# Dekādes (decades — e.g. "the 90s")
# ============================================================
DECADE_CASES = [
    ("70. gados",   "septiņdesmitajos gados"),   # loc pl (in the 70s)
    ("80. gados",   "astoņdesmitajos gados"),    # loc pl
    ("90. gados",   "deviņdesmitajos gados"),    # loc pl
    ("90. gadu",    "deviņdesmito gadu"),        # gen sg (of the 90s)
    ("90. gadi",    "deviņdesmitie gadi"),       # nom pl
    ("20. gados",   "divdesmitajos gados"),      # loc pl (in the 20s)
]

# ============================================================
# Datumu teikumi (date sentences — subtitle-common patterns)
# ============================================================
DATE_SENTENCE_CASES = [
    ("Tas notika 1945. gadā",
     "Tas notika tūkstoš deviņsimt četrdesmit piektajā gadā"),
    ("2024. gada 1. janvārī",
     "divi tūkstoši divdesmit ceturtā gada pirmajā janvārī"),
]

# ============================================================
# Valūtas / Currency cases
# ============================================================

CURRENCY_CASES = [
    # EUR — invariable noun "eiro", cents = "cents/centi/centu"
    ((1,    0,  'EUR'), "viens eiro"),
    ((2,    0,  'EUR'), "divi eiro"),
    ((5,    0,  'EUR'), "pieci eiro"),
    ((11,   0,  'EUR'), "vienpadsmit eiro"),
    ((21,   0,  'EUR'), "divdesmit viens eiro"),
    ((0,    1,  'EUR'), "nulle eiro un viens cents"),
    ((1,   50,  'EUR'), "viens eiro un piecdesmit centu"),
    ((10,  99,  'EUR'), "desmit eiro un deviņdesmit deviņi centi"),
    ((100,  0,  'EUR'), "simts eiro"),
    # USD — masculine: dolārs/dolāri/dolāru
    ((1,    0,  'USD'), "viens dolārs"),
    ((2,    0,  'USD'), "divi dolāri"),
    ((10,   0,  'USD'), "desmit dolāru"),
    ((1,   25,  'USD'), "viens dolārs un divdesmit pieci centi"),
    # LVL — lats/lati/latu + santīms/santīmi/santīmu
    ((1,    0,  'LVL'), "viens lats"),
    ((4,    0,  'LVL'), "četri lati"),
    ((20,   0,  'LVL'), "divdesmit latu"),
    ((1,    1,  'LVL'), "viens lats un viens santīms"),
    ((3,    2,  'LVL'), "trīs lati un divi santīmi"),
    ((10,  15,  'LVL'), "desmit latu un piecpadsmit santīmu"),
    # RUB — rublis/rubļi/rubļu + kapeika/kapeikas/kapeiku (feminine cents)
    ((1,    0,  'RUB'), "viens rublis"),
    ((5,    0,  'RUB'), "pieci rubļi"),
    ((11,   0,  'RUB'), "vienpadsmit rubļu"),
    ((1,    1,  'RUB'), "viens rublis un viena kapeika"),
    ((2,    2,  'RUB'), "divi rubļi un divas kapeikas"),
    ((10,  10,  'RUB'), "desmit rubļu un desmit kapeiku"),
    # GBP — feminine major: sterliņu mārciņa/mārciņas/mārciņu
    ((1,    0,  'GBP'), "viena sterliņu mārciņa"),
    ((3,    0,  'GBP'), "trīs sterliņu mārciņas"),
    ((15,   0,  'GBP'), "piecpadsmit sterliņu mārciņu"),
    # SEK — krona/kronas/kronu + ēre/ēres/ēru (feminine)
    ((1,    0,  'SEK'), "viena krona"),
    ((2,    0,  'SEK'), "divas kronas"),
    ((10,   0,  'SEK'), "desmit kronu"),
    ((1,   50,  'SEK'), "viena krona un piecdesmit ēru"),
]

CURRENCY_ADJECTIVE_CASES = [
    ((1,   0, 'USD', True), "viens ASV dolārs"),
    ((10,  0, 'USD', True), "desmit ASV dolāru"),
    ((1,   0, 'SEK', True), "viena Zviedrijas krona"),
    ((1,   0, 'AUD', True), "viens Austrālijas dolārs"),
    # EUR has no adjective entry — adjective=True is a no-op
    ((5,   0, 'EUR', True), "pieci eiro"),
]

CURRENCY_FLOAT_CASES = [
    (10.5,   'EUR', "desmit eiro un piecdesmit centu"),
    (1.01,   'USD', "viens dolārs un viens cents"),
    (2.99,   'LVL', "divi lati un deviņdesmit deviņi santīmi"),
]

TEMPERATURE_CASES = [
    ("36°C",    "trīsdesmit seši grādi"),
    ("100°F",   "simts grādi"),
    ("90°",     "deviņdesmit grādi"),
    ("1°C",     "viens grāds"),
    ("21°",     "divdesmit viens grāds"),
    ("11°C",    "vienpadsmit grādi"),
    ("0°",      "nulle grādu"),
    ("2°",      "divi grādi"),
    # atstarpe pirms ° (space before the degree sign)
    ("21 °C",   "divdesmit viens grāds"),
    ("-5 °C",   "mīnus pieci grādi"),
    ("-5°C",    "mīnus pieci grādi"),
    ("-1°C",    "mīnus viens grāds"),
    ("0°C",     "nulle grādu"),
    # plus zīme (plus sign)
    ("+21°C",   "plus divdesmit viens grāds"),
    ("+21 °C",  "plus divdesmit viens grāds"),
    ("+1°C",    "plus viens grāds"),
    # diapazoni (ranges)
    ("14…15°C",   "četrpadsmit līdz piecpadsmit grādi"),
    ("14…15 °C",  "četrpadsmit līdz piecpadsmit grādi"),
    ("14...15 °C", "četrpadsmit līdz piecpadsmit grādi"),
    ("14–15°C",   "četrpadsmit līdz piecpadsmit grādi"),
    ("14-15 °C",  "četrpadsmit līdz piecpadsmit grādi"),
    ("14 – 15 °C", "četrpadsmit līdz piecpadsmit grādi"),
    ("20…21°",    "divdesmit līdz divdesmit viens grāds"),
    # diapazoni ar zīmēm (signed ranges)
    ("-5…-3°C",   "mīnus pieci līdz mīnus trīs grādi"),
    ("-5…+3 °C",  "mīnus pieci līdz plus trīs grādi"),
    ("-5…0°C",    "mīnus pieci līdz nulle grādu"),
    ("-2…0 °C",   "mīnus divi līdz nulle grādu"),
    ("0…+3°C",    "nulle līdz plus trīs grādi"),
    ("-3…+1 °C",  "mīnus trīs līdz plus viens grāds"),
    # vārds "grādi" bez ° zīmes (spelled-out noun)
    ("+5 grādi",  "plus pieci grādi"),
    ("-5 grādi",  "mīnus pieci grādi"),
    ("14–15 grādi", "četrpadsmit līdz piecpadsmit grādi"),
    ("+14…+15 grādi", "plus četrpadsmit līdz plus piecpadsmit grādi"),
    ("-1…0 grādi",  "mīnus viens līdz nulle grādi"),
    ("21 grādi",    "divdesmit viens grādi"),
    ("+21 grādi",   "plus divdesmit viens grādi"),
    ("-1 grāds",    "mīnus viens grāds"),
    ("20…21 grādi", "divdesmit līdz divdesmit viens grādi"),
    ("+21…+22 grādos", "plus divdesmit vienā līdz plus divdesmit divos grādos"),
    # decimāldaļas (decimals)
    ("36,6°C",  "trīsdesmit seši komats seši grādi"),
    ("21,1°C",  "divdesmit viens komats viens grāds"),
    # laika ziņas (weather forecast sentences)
    ("Ceturtdien: +14…+15 °C",
     "Ceturtdien: plus četrpadsmit līdz plus piecpadsmit grādi"),
    ("naktī +9…+10 °C, dienā +18…+19 °C",
     "naktī plus deviņi līdz plus desmit grādi, "
     "dienā plus astoņpadsmit līdz plus deviņpadsmit grādi"),
]

TONNE_CASES = [
    ("53T",     "piecdesmit trīs tonnas"),
    ("1T",      "viena tonna"),
    ("1 T",      "viena tonna"),
    ("10T",     "desmit tonnu"),
    ("21T",     "divdesmit viena tonna"),
    ("5 T",     "piecas tonnas"),
    ("11T",     "vienpadsmit tonnu"),
]

VULGAR_FRACTION_CASES = [
    ("3/4",     "trīs ceturtdaļas"),
    ("1/2",     "viena puse"),
    ("9/10",    "deviņas desmitdaļas"),
    ("2 1/4",   "divi veseli viena ceturtdaļa"),
    ("1 1/2",   "viens vesels viena puse"),
    ("1/3",     "viena trešdaļa"),
    ("2/3",     "divas trešdaļas"),
    ("5/8",     "piecas astotdaļas"),
]

NO_ROMAN_CASES = [
    ("II pasaules karš",  "II pasaules karš"),
    ("V nodaļa",          "V nodaļa"),
    ("XIV gs.",           "XIV gadsimts"),
]

CLASS_CASES = [
    ("4.D klase",    "ceturtā d klase"),
    ("4.d klasei",   "ceturtajai d klasei"),
    ("1.A klase",    "pirmā a klase"),
    ("10.B klase",   "desmitā b klase"),
]

CURRENCY_CONVERT_CASES = [
    # Symbol after (no space)
    ("1,82€",           "viens eiro un astoņdesmit divi centi"),
    ("5€",              "pieci eiro"),
    ("1,82$",           "viens dolārs un astoņdesmit divi centi"),
    ("1,82£",           "viena sterliņu mārciņa un astoņdesmit divi pensi"),
    # Symbol after (with space)
    ("1,82 €",          "viens eiro un astoņdesmit divi centi"),
    ("10 €",            "desmit eiro"),
    # Symbol before (no space)
    ("€1,82",           "viens eiro un astoņdesmit divi centi"),
    ("$5",              "pieci dolāri"),
    # Symbol before (with space)
    ("€ 1,82",          "viens eiro un astoņdesmit divi centi"),
    # Code after
    ("1,82 EUR",        "viens eiro un astoņdesmit divi centi"),
    ("5 EUR",           "pieci eiro"),
    ("10,99 USD",       "desmit dolāru un deviņdesmit deviņi centi"),
    ("1 LVL",           "viens lats"),
    # Code before
    ("EUR 1,82",        "viens eiro un astoņdesmit divi centi"),
    ("USD 10,99",       "desmit dolāru un deviņdesmit deviņi centi"),
    ("EUR 100",         "simts eiro"),
    # Decimal with dot separator
    ("1.82€",           "viens eiro un astoņdesmit divi centi"),
    ("EUR 1.82",        "viens eiro un astoņdesmit divi centi"),
    # Single-digit fractional part (e.g. 1,8 → 80 cents)
    ("1,8€",            "viens eiro un astoņdesmit centu"),
    # Embedded in sentence
    ("Prece maksā 2,50 EUR.", "Prece maksā divus eiro un piecdesmit centu."),
    ("Salāti maksā 1.83EUR", "Salāti maksā vienu eiro un astoņdesmit trīs centus"),
    # More decimals than a currency has — read as a plain decimal, not as cents
    ("2,003 eiro",      "divi komats nulle nulle trīs eiro"),
]

# ============================================================
# Valūta, rakstīta ar vārdiem (spelled-out currency name — NOT a currency trigger)
#
# Only the formal "EUR" and "€" split an amount into units and cents; when the
# currency is written out as a word the number is read as a plain decimal, with
# the leading zeros of the fractional part spoken.
# ============================================================
CURRENCY_WORD_CASES = [
    ("1237,06 eiro", "tūkstoš divsimt trīsdesmit septiņi komats nulle seši eiro"),
    ("1237,6 eiro",  "tūkstoš divsimt trīsdesmit septiņi komats seši eiro"),
    ("1237,60 eiro", "tūkstoš divsimt trīsdesmit septiņi komats sešdesmit eiro"),
    ("10,01 eiro",   "desmit komats nulle viens eiro"),
    ("1 eiro",       "viens eiro"),
    ("5 eiro",       "pieci eiro"),
    ("11 eiro",      "vienpadsmit eiro"),
    ("2,50 euro",    "divi komats piecdesmit euro"),
    ("Prece maksā 2,50 eiro.", "Prece maksā divi komats piecdesmit eiro."),
    ("eiro kurss",   "eiro kurss"),
]


# ============================================================
# Vīriešu dzimtes kārtas skaitļi (masculine ordinals — subtitle narration)
# ============================================================
MASCULINE_ORDINAL_CASES = [
    ("3. stāvs",        "trešais stāvs"),
    ("2. kanāls",       "otrais kanāls"),
    ("1. iemesls",      "pirmais iemesls"),
    ("3. stāvā",        "trešajā stāvā"),
    ("5. maijam",       "piektajam maijam"),
    ("3. stāvam",       "trešajam stāvam"),
    ("1. vietai",       "pirmajai vietai"),
    ("par 3. vietu",    "par trešo vietu"),
    ("1. iemesls",      "pirmais iemesls"),
]

# ============================================================
# Reizes (repetitions — common in dialogue)
# ============================================================
REPETITION_CASES = [
    ("1 reize",     "viena reize"),
    ("2 reizes",    "divas reizes"),
    ("3 reizes",    "trīs reizes"),
    ("5 reizes",    "piecas reizes"),
    ("10 reizes",   "desmit reizes"),
    ("3 reizēm",    "trim reizēm"),
]

# ============================================================
# Pulksteņa laiks ar "plkst." (clock time with plkst. prefix)
# ============================================================
CLOCK_TIME_PLKST_CASES = [
    ("plkst. 10:45",   "pulksten desmitos četrdesmit piecās"),
    ("plkst. 9:00",    "pulksten deviņos"),
    ("plkst. 14:30",   "pulksten četrpadsmitos trīsdesmit"),
]

# ============================================================
# Pulksteņa laiks ar punktu un laika intervāli
# (dotted clock times "10.00" and time ranges "10.00–10.30")
# ============================================================
DOTTED_TIME_CASES = [
    # Punktotais pieraksts ar norādi uz pulksteni lasās tāpat kā "10:00"
    ("plkst. 10.00",            "pulksten desmitos"),
    ("pulksten 9.05",           "pulksten deviņos piecās"),
    ("plkst 14.30",             "plkst četrpadsmitos trīsdesmit"),
    # Intervālus lasa ar "līdz" — gan ar kolu, gan ar punktu
    ("plkst. 10:00–10:30",      "pulksten desmitos līdz desmitos trīsdesmit"),
    ("plkst. 10.00–10.30",      "pulksten desmitos līdz desmitos trīsdesmit"),
    ("plkst. 10.00 – 10.30",    "pulksten desmitos līdz desmitos trīsdesmit"),
    ("10:00–10:30",             "desmitos līdz desmitos trīsdesmit"),
    ("10.00–10.30",             "desmitos līdz desmitos trīsdesmit"),
    ("10.00-10.30",             "desmitos līdz desmitos trīsdesmit"),
    ("23.59–00.30",             "divdesmit trijos piecdesmit deviņās līdz nullē trīsdesmit"),
    # Teikuma beigu punkts paliek pieturzīme, nekļūst par kārtas skaitli
    ("plkst. 10.00–10.30.",     "pulksten desmitos līdz desmitos trīsdesmit."),
    # "līdz" turpina norādi uz pulksteni
    ("no plkst. 10.00 līdz 10.30",
     "no pulksten desmitos līdz desmitos trīsdesmit"),
    ("Ielikts kalendārā: 7. septembrī, plkst. 10.00–10.30.",
     "Ielikts kalendārā: septītajā septembrī, pulksten desmitos līdz desmitos trīsdesmit."),
]

# Bez norādes uz pulksteni punktotais pieraksts paliek decimālskaitlis
NOT_A_TIME_CASES = [
    ("12.30",        "divpadsmit komats trīsdesmit"),
    ("21.5 grami",   "divdesmit viens komats pieci grami"),
    ("21,5 grami",   "divdesmit viens komats pieci grami"),
    ("1.10",         "viens komats desmit"),
    ("9.60",         "deviņi komats sešdesmit"),
    ("3.–5. klase",  "trešā līdz piektā klase"),
    ("1. – 2. vieta", "pirmā – otrā vieta"),
]

# ============================================================
# Sporta rezultāti ar nulli (sports scores with zero)
# ============================================================
SCORE_EDGE_CASES = [
    ("0:0",     "nulle nulle"),
    ("0:3",     "nulle trīs"),
    ("10:0",    "desmit nulle"),
]

# ============================================================
# Gadsimtu kārtas skaitļi (century ordinals — documentary narration)
# ============================================================
ORDINAL_CENTURY_CASES = [
    ("3. gadsimta sākumā",    "trešā gadsimta sākumā"),
    ("20. gadsimta sākumā",   "divdesmitā gadsimta sākumā"),
    ("21. gadsimtā",          "divdesmit pirmajā gadsimtā"),
]

# ============================================================
# Procenti ar prievārdiem (percentages with prepositions)
# ============================================================
PERCENTAGE_PREPOSITION_CASES = [
    ("par 1%",    "par vienu procentu"),
    ("par 5%",    "par pieciem procentiem"),
    ("līdz 50%",  "līdz piecdesmit procentiem"),
    ("virs 90%",  "virs deviņdesmit procentiem"),
]

# ============================================================
# Ātrums (speed — km/h, m/s)
# ============================================================
SPEED_CASES = [
    ("1 km/h",    "viens kilometrs stundā"),
    ("2 km/h",    "divi kilometri stundā"),
    ("11 km/h",   "vienpadsmit kilometru stundā"),
    ("21 km/h",   "divdesmit viens kilometrs stundā"),
    ("100 km/h",  "simts kilometru stundā"),
    ("80–100 km/h", "astoņdesmit līdz simts kilometru stundā"),
    ("1 m/s",     "viens metrs sekundē"),
    ("5 m/s",     "pieci metri sekundē"),
    ("10 m/s",    "desmit metru sekundē"),
    ("21 m/s",    "divdesmit viens metrs sekundē"),
    ("2,5 m/s",   "divi komats pieci metri sekundē"),
    ("5–8 m/s",   "pieci līdz astoņi metri sekundē"),
    ("vējš 5–8 m/s, brāzmās 15 m/s",
     "vējš pieci līdz astoņi metri sekundē, brāzmās piecpadsmit metru sekundē"),
]

# ============================================================
# Vecuma ierobežojumi (age-gate labels — "18+")
# ============================================================
AGE_GATE_CASES = [
    ("18+",              "astoņpadsmit plus"),
    ("16+",              "sešpadsmit plus"),
    ("6+",               "seši plus"),
    ("Filma ir 18+",     "Filma ir astoņpadsmit plus"),
]

# ============================================================
# Sēriju apzīmējumi (episode notation — "S02E03" must pass through)
# ============================================================
EPISODE_NOTATION_CASES = [
    ("S02E03",           "S02E03"),
    ("S01E01",           "S01E01"),
    ("Skatāmies S02E03", "Skatāmies S02E03"),
]

# ============================================================
# Mācību gadi (academic year slash range — "2023./2024.")
# ============================================================
ACADEMIC_YEAR_CASES = [
    ("2023./2024. mācību gads",
     "divi tūkstoši divdesmit trešais līdz divi tūkstoši divdesmit ceturtais mācību gads"),
    ("2023./2024. mācību gadā",
     "divi tūkstoši divdesmit trešajā līdz divi tūkstoši divdesmit ceturtajā mācību gadā"),
]


# ============================================================
# Kārtas skaitļi bez atstarpes aiz punkta
# (ordinals whose dot is glued to the next word — "2026.gada")
# ============================================================
ORDINAL_NO_SPACE_CASES = [
    ("2026.gada augusts",   "divi tūkstoši divdesmit sestā gada augusts"),
    ("2026.gadā",           "divi tūkstoši divdesmit sestajā gadā"),
    ("2026.g.",             "divi tūkstoši divdesmit sestais gads"),
    ("15.augustā",          "piecpadsmitajā augustā"),
    ("3.vieta",             "trešā vieta"),
    ("1.klase",             "pirmā klase"),
    ("2.pants",             "otrais pants"),
    ("XX.gadsimts",         "divdesmitais gadsimts"),       # roman ordinal
    ("2026.gada 5.maijā",   "divi tūkstoši divdesmit sestā gada piektajā maijā"),
    ("(2026.gada)",         "(divi tūkstoši divdesmit sestā gada)"),
    ("2026.gada.",          "divi tūkstoši divdesmit sestā gada."),
    ("3., 4. vieta",        "trešā, ceturtā vieta"),
    ("3.,4.vieta",          "trešā,ceturtā vieta"),
    ("1941.-1945.gads",
     "tūkstoš deviņsimt četrdesmit pirmais līdz tūkstoš deviņsimt četrdesmit piektais gads"),
    ("2023./2024.gads",
     "divi tūkstoši divdesmit trešais līdz divi tūkstoši divdesmit ceturtais gads"),
    ("4.D klase",           "ceturtā d klase"),             # class notation still wins
    ("5.5",                 "pieci komats pieci"),          # decimal, not an ordinal
    ("Viņam ir 25.",        "Viņam ir divdesmit piektais"), # trailing ordinal unchanged
]

# Iniciāļi paliek neskarti arī bez atstarpes aiz punkta
# (name initials stay untouched even when glued to the surname)
GLUED_INITIAL_CASES = [
    ("A.Briāna ielā 16",    "A.Briāna ielā sešpadsmit"),    # "A" is no Roman numeral
    ("V.Bērziņš",           "V.Bērziņš"),                   # initial before a surname
]

# ============================================================
# Mērvienības bez atstarpes aiz skaitļa (units glued to the number)
# ============================================================
GLUED_UNIT_CASES = [
    ("5km",         "pieci kilometri"),
    ("2,5kg",       "divi komats pieci kilogrami"),
    ("10m²",        "desmit kvadrātmetru"),          # gen pl, as for "10 km²"
    ("0–2mm",       "nulle līdz divi milimetri"),
    ("5lpp.",       "piecas lappuses"),
    # "min" is not the unit "m" — only the number is spoken
    ("5min",        "piecimin"),
    ("5 m/s",       "pieci metri sekundē"),
    ("100km/h",     "simts kilometru stundā"),
]

# ============================================================
# Tūkstoši ar dubultu atstarpi (thousands split by a double space)
# ============================================================
SPACED_THOUSANDS_CASES = [
    ("150 000 eiro",    "simt piecdesmit tūkstoši eiro"),
    ("150  000 eiro",   "simt piecdesmit tūkstoši eiro"),   # two spaces
]

# ============================================================
# Saīsinājumi ar atstarpi (officially spaced abbreviations)
# ============================================================
SPACED_ABBR_CASES = [
    ("u. c.",       "un citi"),
    ("u. tml.",     "un tamlīdzīgi"),
    ("t. i.",       "tas ir"),
    ("pr. Kr.",     "pirms Kristus"),
    ("p. Kr.",      "pēc Kristus"),
]

# Saīsinājums pielipis skaitlim (abbreviation glued to a digit)
GLUED_ABBR_DIGIT_CASES = [
    ("Nr.5",        "numur pieci"),
    ("nr.5",        "numur pieci"),
    ("lpp.5",       "lappuse pieci"),
]

# ============================================================
# Pulksteņa norāde pielipusi laikam (clock-time cue glued to the time)
# ============================================================
GLUED_TIME_CASES = [
    ("plkst.10.00",             "pulksten desmitos"),
    ("plkst.10.00 līdz 11.30",  "pulksten desmitos līdz vienpadsmitos trīsdesmit"),
    ("plkst. 10.00",            "pulksten desmitos"),
]

# ============================================================
# Garas ciparu virknes un sākuma nulles
# (long digit strings and leading zeros — identifier codes)
# ============================================================
LONG_DIGIT_CASES = [
    ("01000230010002",
     "nulle viens nulle nulle nulle divi trīs nulle nulle viens nulle nulle nulle divi"),
    ("kadastra apzīmējums: 01000230010002",
     "kadastra apzīmējums: nulle viens nulle nulle nulle divi trīs "
     "nulle nulle viens nulle nulle nulle divi"),
    ("1234567890",
     "viens divi trīs četri pieci seši septiņi astoņi deviņi nulle"),
    # nine digits are still a quantity
    ("123456789 eiro",
     "simt divdesmit trīs miljoni četrsimt piecdesmit seši tūkstoši "
     "septiņsimt astoņdesmit deviņi eiro"),
    ("0", "nulle"),
    ("05.05.2026", "pieci komats nulle pieci.divtūkstoš divdesmit seši"),
]

# Miljardi (billions)
BILLION_CASES = [
    (1_000_000_000, "viens miljards"),
    (2_500_000_000, "divi miljardi piecsimt miljoni"),
    (1_000_000, "viens miljons"),
]

# ============================================================
# Mērvienības pēdiņās, iekavās vai pirms pieturzīmes
# Units followed by a closing quote, bracket or "!?:"
# ============================================================
QUOTED_UNIT_CASES = [
    ("“5km”",           "“pieci kilometri”"),
    ("(5 km)",          "(pieci kilometri)"),
    ("5km!",            "pieci kilometri!"),
    ("5 km?",           "pieci kilometri?"),
    ("5 km:",           "pieci kilometri:"),
    ("“2,5kg”",         "“divi komats pieci kilogrami”"),
    ("“10m²”",          "“desmit kvadrātmetru”"),
    ("“0–2mm”",         "“nulle līdz divi milimetri”"),
    ("“36°C”",          "“trīsdesmit seši grādi”"),
    ("“100 km/h”",      "“simts kilometru stundā”"),
    ("“5 m/s”",         "“pieci metri sekundē”"),
    ("“53T”",           "“piecdesmit trīs tonnas”"),
    ("“80–100 km/h”",   "“astoņdesmit līdz simts kilometru stundā”"),
    ("2026.gada»",      "divi tūkstoši divdesmit sestā gada»"),
    ("3.…",             "trešais…"),
    # nemainīgi / unchanged: "min" and "kmh" are not unit abbreviations
    ("5 min",           "pieci min"),
    ("5min",            "piecimin"),
    ("5 kmh",           "pieci kmh"),
    ("2 mājas",         "divas mājas"),
    ("5. maijs",        "piektais maijs"),
]

# Viss teikums ar pielipušām mērvienībām / whole line, nothing left unexpanded
QUOTED_UNIT_LINE_CASES = [
    ("Pielipušas mērvienības: “5km”, “2,5kg”, “10m²”, “0–2mm”, “5lpp.” "
     "iepriekš deva “piecikm”. Saīsinājums pielipis pie cipara: "
     "“Nr.5” deva “numurpieci”.",
     "Pielipušas mērvienības: “pieci kilometri”, “divi komats pieci kilogrami”, "
     "“desmit kvadrātmetru”, “nulle līdz divi milimetri”, “piecas lappuses” "
     "iepriekš deva “piecikm”. Saīsinājums pielipis pie cipara: "
     "“numur pieci” deva “numurpieci”."),
]

# ============================================================
# Locījums nepārlec pāri aizverošai pēdiņai vai iekavai
# Noun agreement stops at a closing quote/bracket
# ============================================================
BUCKET_STOP_CASES = [
    ("“Nr.5” deva",         "“numur pieci” deva"),
    ("(Nr. 5) mājas",       "(numur pieci) mājas"),
    # komats, punkts un domuzīme neaptur / commas, dots and dashes do not stop it
    ("1., 2. un 3. vieta",  "pirmā, otrā un trešā vieta"),
    ("3.,4.vieta",          "trešā,ceturtā vieta"),
]

# ============================================================
# Identifikatori ar divām vai vairāk domuzīmēm nav diapazons
# A token with two or more dashes is an identifier code, not a range
# ============================================================
_BIS_CODE = ("BIS-BL-astoņi divi septiņi astoņi četri seši-"
             "viens viens četri četri divi seši")
CODE_TOKEN_CASES = [
    ("BIS-BL-827846-114426",    _BIS_CODE),
    ("lieta BIS-BL-827846-114426, būvdarbu",
     f"lieta {_BIS_CODE}, būvdarbu"),
    ("“BIS-BL-827846-114426”",  f"“{_BIS_CODE}”"),
    ("ISBN 978-9934-0-1234-5",
     "ISBN deviņi septiņi astoņi-deviņi deviņi trīs četri-nulle-"
     "viens divi trīs četri-pieci"),
    # viena domuzīme joprojām ir diapazons / one dash is still a range
    ("1941–1945 gads",
     "tūkstoš deviņsimt četrdesmit pirmais līdz "
     "tūkstoš deviņsimt četrdesmit piektais gads"),
    ("5–6 grādi",       "pieci līdz seši grādi"),
    ("0–2 mm",          "nulle līdz divi milimetri"),
    ("10-20 procenti",  "desmit līdz divdesmit procenti"),
    ("80–100 km/h",     "astoņdesmit līdz simts kilometru stundā"),
]

# ============================================================
# Domuzīme pielipusi burtam nav mīnusa zīme
# A hyphen glued to a letter is not a minus sign
# ============================================================
LETTER_MINUS_CASES = [
    ("COVID-19",    "COVID-deviņpadsmit"),
    ("LV-1010",     "LV-tūkstoš desmit"),
    # īsts mīnuss joprojām strādā / real negatives still work
    ("-5",          "mīnus pieci"),
    ("5 -3",        "piecus mīnus trīs"),
    ("(-5)",        "(mīnus pieci)"),
    ("-5°C",        "mīnus pieci grādi"),
    ("-5…-3°C",     "mīnus pieci līdz mīnus trīs grādi"),
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


@pytest.mark.parametrize("text,expected", ACRONYM_NOT_ROMAN_CASES)
def test_acronym_not_roman(text, expected):
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


@pytest.mark.parametrize("text,expected", NON_ABBREVIATION_CASES)
def test_non_abbreviations(text, expected):
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


@pytest.mark.parametrize("text,expected", UNIT_RANGE_CASES)
def test_unit_ranges(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", PHONE_CASES)
def test_phones(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("args,expected", CURRENCY_CASES)
def test_currency(args, expected):
    n, c, code = args
    assert currency((n, c), code) == expected


@pytest.mark.parametrize("args,expected", CURRENCY_ADJECTIVE_CASES)
def test_currency_adjective(args, expected):
    n, c, code, adj = args
    assert currency((n, c), code, adjective=adj) == expected


@pytest.mark.parametrize("amount,code,expected", CURRENCY_FLOAT_CASES)
def test_currency_float(amount, code, expected):
    assert currency(amount, code) == expected


@pytest.mark.parametrize("text,expected", CURRENCY_CONVERT_CASES)
def test_currency_in_text(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", WEIGHT_CASES)
def test_weight_kg(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", SUBTITLE_ORDINAL_CASES)
def test_subtitle_ordinals(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", DECADE_CASES)
def test_decades(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", DATE_SENTENCE_CASES)
def test_date_sentences(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", TEMPERATURE_CASES)
def test_temperature(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", TONNE_CASES)
def test_tonnes(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", VULGAR_FRACTION_CASES)
def test_vulgar_fractions(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", NO_ROMAN_CASES)
def test_no_roman(text, expected):
    assert convert(text, no_roman=True) == expected


@pytest.mark.parametrize("text,expected", CLASS_CASES)
def test_class_notation(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", MASCULINE_ORDINAL_CASES)
def test_masculine_ordinals(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", REPETITION_CASES)
def test_repetitions(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", CLOCK_TIME_PLKST_CASES)
def test_clock_time_plkst(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", SCORE_EDGE_CASES)
def test_score_edge(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", ORDINAL_CENTURY_CASES)
def test_ordinal_centuries(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", PERCENTAGE_PREPOSITION_CASES)
def test_percentage_prepositions(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", SPEED_CASES)
def test_speed(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", AGE_GATE_CASES)
def test_age_gate(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", EPISODE_NOTATION_CASES)
def test_episode_notation(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", ACADEMIC_YEAR_CASES)
def test_academic_year(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", DECIMAL_LEADING_ZERO_CASES)
def test_decimal_leading_zeros(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", DECIMAL_UNIT_CASES)
def test_decimal_units(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", CURRENCY_WORD_CASES)
def test_currency_word(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", DOTTED_TIME_CASES)
def test_dotted_clock_times(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", NOT_A_TIME_CASES)
def test_dotted_numbers_are_not_times(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", ORDINAL_NO_SPACE_CASES)
def test_ordinal_without_space(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", GLUED_INITIAL_CASES)
def test_glued_initials(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", GLUED_UNIT_CASES)
def test_glued_units(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", SPACED_THOUSANDS_CASES)
def test_spaced_thousands(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", SPACED_ABBR_CASES)
def test_spaced_abbreviations(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", GLUED_ABBR_DIGIT_CASES)
def test_abbreviation_glued_to_digit(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", GLUED_TIME_CASES)
def test_glued_clock_times(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", LONG_DIGIT_CASES)
def test_long_digit_strings(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("n,expected", BILLION_CASES)
def test_billions(n, expected):
    assert cardinal(n) == expected


@pytest.mark.parametrize("text,expected", QUOTED_UNIT_CASES)
def test_units_before_closing_punctuation(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", QUOTED_UNIT_LINE_CASES)
def test_glued_units_full_line(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", BUCKET_STOP_CASES)
def test_bucket_stops_at_closing_quote(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", CODE_TOKEN_CASES)
def test_identifier_codes_are_not_ranges(text, expected):
    assert convert(text) == expected


@pytest.mark.parametrize("text,expected", LETTER_MINUS_CASES)
def test_hyphen_after_letter_is_not_minus(text, expected):
    assert convert(text) == expected
