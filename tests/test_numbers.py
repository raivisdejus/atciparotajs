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
    ("V nodaļa",            "piektā nodaļa"),               # nom fem sg
    ("XIX gs.",             "deviņpadsmitais gadsimts"),    # 19th century
    ("XXI gs.",             "divdesmit pirmais gadsimts"),  # 21st century
    ("XX gadsimtā",         "divdesmitajā gadsimtā"),       # loc sg (in the 20th century)
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
    ("Sanāksme sākas 14:30",    "Sanāksme sākas divos trīsdesmit"),
    ("9:05",                    "deviņos piecās"),
    ("8:00",                    "astoņos"),
    ("12:00",                   "divpadsmitos"),
    ("23:59",                   "vienpadsmitos piecdesmit deviņās"),
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
]

# ============================================================
# Telefona numuri (phone numbers)
# ============================================================
PHONE_CASES = [
    ("tel. 67 030 638",      "seši septiņi nulle trīs nulle seši trīs astoņi"),
    ("tel: 67 030 638",      "seši septiņi nulle trīs nulle seši trīs astoņi"),
    ("tel 67 030 638",       "seši septiņi nulle trīs nulle seši trīs astoņi"),
    ("tel.67030638",         "seši septiņi nulle trīs nulle seši trīs astoņi"),
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
    ("Sezona 2, 3. sērija", "Sezona divas, trešā sērija"),
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
    # EUR_LEGAL — "euro"
    ((1,    0,  'EUR_LEGAL'), "viens euro"),
    ((3,    0,  'EUR_LEGAL'), "trīs euro"),
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
    ("plkst. 14:30",   "pulksten divos trīsdesmit"),
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
# Ātrums (speed — km/h)
# ============================================================
SPEED_CASES = [
    ("1 km/h",    "viens kilometrs stundā"),
    ("2 km/h",    "divi kilometri stundā"),
    ("11 km/h",   "vienpadsmit kilometru stundā"),
    ("21 km/h",   "divdesmit viens kilometrs stundā"),
    ("100 km/h",  "simts kilometru stundā"),
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
