"""
Pārbaudes gadījumi / Test cases for atciparotājs.
Each line shows: input text → expected output
"""

import pytest
from atciparotajs import convert

CARDINAL_CASES = [
    ("2 draugiem",   "diviem draugiem"),
    ("2 desas",      "divas desas"),
    ("5 maija",      "piecu maija"),
    ("3 kaķi",       "trīs kaķi"),
    ("1 māja",       "viena māja"),
    ("21 diena",     "divdesmit viena diena"),
    ("100 grami",    "simts grami"),
    ("Es esmu 30",   "Es esmu trīsdesmit"),
]

ORDINAL_CASES = [
    ("5. maijs",     "piektais maijs"),
    ("1. maijā",     "pirmajā maijā"),
    ("3. vieta",     "trešā vieta"),
    ("1. vieta",     "pirmā vieta"),
    ("21. vieta",    "divdesmit pirmā vieta"),
]

ROMAN_CASES = [
    ("II pasaules karš",   "otrais pasaules karš"),
    ("XIV gs.",            "četrpadsmitais gadsimts"),
    ("V nodaļa",           "piektā nodaļa"),
]

FRACTION_CASES = [
    ("21,5 grami",   "divdesmit viens komats pieci grami"),
    ("21.5 grami",   "divdesmit viens komats pieci grami"),
    ("3,14",         "trīs komats četrpadsmit"),
    ("1,5 stundas",  "viens komats pieci stundas"),
]

ABBREVIATION_CASES = [
    ("14. gs.",      "četrpadsmitais gadsimts"),
    ("t.i. pieci",   "tas ir pieci"),
]


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
