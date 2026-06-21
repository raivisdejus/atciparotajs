# Test Cases

Auto-generated after each `pytest` run. Shows every parametrised case with its last recorded outcome.

## One Inflections

| Input | Expected | Result |
|-------|----------|--------|
| `1 suns` | `viens suns` | ✅ |
| `1 māja` | `viena māja` | ✅ |
| `1 mājas` | `vienas mājas` | ✅ |
| `1 sunim` | `vienam sunim` | ✅ |
| `1 mājai` | `vienai mājai` | ✅ |
| `1 māju` | `vienu māju` | ✅ |
| `1 sunī` | `vienā sunī` | ✅ |
| `1 mājā` | `vienā mājā` | ✅ |

## Two Inflections

| Input | Expected | Result |
|-------|----------|--------|
| `2 suņi` | `divi suņi` | ✅ |
| `2 mājas` | `divas mājas` | ✅ |
| `2 māju` | `divu māju` | ✅ |
| `2 suņiem` | `diviem suņiem` | ✅ |
| `2 mājām` | `divām mājām` | ✅ |
| `2 suņus` | `divus suņus` | ✅ |
| `2 suņos` | `divos suņos` | ✅ |
| `2 mājās` | `divās mājās` | ✅ |

## Eleven Inflections

| Input | Expected | Result |
|-------|----------|--------|
| `11 suņi` | `vienpadsmit suņi` | ✅ |
| `11 mājas` | `vienpadsmit mājas` | ✅ |
| `11 suņiem` | `vienpadsmit suņiem` | ✅ |
| `11 mājām` | `vienpadsmit mājām` | ✅ |
| `11 suņus` | `vienpadsmit suņus` | ✅ |
| `11 suņos` | `vienpadsmit suņos` | ✅ |
| `11 mājās` | `vienpadsmit mājās` | ✅ |

## Cardinals

| Input | Expected | Result |
|-------|----------|--------|
| `2 draugiem` | `diviem draugiem` | ✅ |
| `2 desas` | `divas desas` | ✅ |
| `5 māju` | `piecu māju` | ✅ |
| `3 kaķi` | `trīs kaķi` | ✅ |
| `21 diena` | `divdesmit viena diena` | ✅ |
| `100 grami` | `simts grami` | ✅ |
| `Man ir 30` | `Man ir trīsdesmit` | ✅ |

## Ordinals

| Input | Expected | Result |
|-------|----------|--------|
| `5. maijs` | `piektais maijs` | ✅ |
| `1. maijā` | `pirmajā maijā` | ✅ |
| `3. vieta` | `trešā vieta` | ✅ |
| `2. vietā` | `otrajā vietā` | ✅ |
| `1. vieta` | `pirmā vieta` | ✅ |
| `21. vieta` | `divdesmit pirmā vieta` | ✅ |

## Roman

| Input | Expected | Result |
|-------|----------|--------|
| `II pasaules karš` | `otrais pasaules karš` | ✅ |
| `XIV gs.` | `četrpadsmitais gadsimts` | ✅ |
| `V nodaļa` | `piektā nodaļa` | ✅ |

## Fractions

| Input | Expected | Result |
|-------|----------|--------|
| `21,5 grami` | `divdesmit viens komats pieci grami` | ✅ |
| `21.5 grami` | `divdesmit viens komats pieci grami` | ✅ |
| `3,14` | `trīs komats četrpadsmit` | ✅ |
| `1,5 stundas` | `viena komats piecas stundas` | ✅ |

## Abbreviations

| Input | Expected | Result |
|-------|----------|--------|
| `14. gs.` | `četrpadsmitais gadsimts` | ✅ |
| `t.i. pieci` | `tas ir pieci` | ✅ |
| `15 km dziļumā` | `piecpadsmit kilometru dziļumā` | ✅ |
| `15 km. dziļumā` | `piecpadsmit kilometru dziļumā` | ✅ |
| `600 mm mortīra` | `sešsimt milimetru mortīra` | ✅ |

## Dates

| Input | Expected | Result |
|-------|----------|--------|
| `4. oktobris, 1957. gads` | `ceturtais oktobris, tūkstoš deviņsimt piecdesmit septītais gads` | ✅ |
| `1961. gada 12. aprīlis` | `tūkstoš deviņsimt sešdesmit pirmā gada divpadsmitais aprīlis` | ✅ |
| `1969. gada 20. jūlijā` | `tūkstoš deviņsimt sešdesmit devītā gada divdesmitajā jūlijā` | ✅ |
| `2026. gads` | `divi tūkstoši divdesmit sestais gads` | ✅ |
| `1941.–1945. gads` | `tūkstoš deviņsimt četrdesmit pirmais līdz tūkstoš deviņsimt četrdesmit piektais gads` | ✅ |
| `1941.–1945. gadā` | `tūkstoš deviņsimt četrdesmit pirmajā līdz tūkstoš deviņsimt četrdesmit piektajā gadā` | ✅ |
| `1927. un 1928. gadā` | `tūkstoš deviņsimt divdesmit septītajā un tūkstoš deviņsimt divdesmit astotajā gadā` | ✅ |

## Initials Not Roman

| Input | Expected | Result |
|-------|----------|--------|
| `Kārlis V. uzvarēja` | `Kārlis V. uzvarēja` | ✅ |
| `Jānis A. sacīja` | `Jānis A. sacīja` | ✅ |

## Nr Keeps Digits

| Input | Expected | Result |
|-------|----------|--------|
| `Vilciens nr. 67` | `Vilciens numur sešdesmit septiņi` | ✅ |
| `Autobuss nr. 3` | `Autobuss numur trīs` | ✅ |

## Lpp Plural

| Input | Expected | Result |
|-------|----------|--------|
| `58 lpp. gara grāmata` | `piecdesmit astoņas lappuses gara grāmata` | ✅ |
| `1 lpp.` | `viena lappuse` | ✅ |
| `100 lpp.` | `simts lappuses` | ✅ |

## Clock Time

| Input | Expected | Result |
|-------|----------|--------|
| `Vilciens pienāks 10:45` | `Vilciens pienāks desmitos četrdesmit piecās` | ✅ |
| `Pulksten 1:00` | `Pulksten vienos` | ✅ |
| `Sanāksme sākas 14:30` | `Sanāksme sākas divos trīsdesmit` | ✅ |
| `9:05` | `deviņos piecās` | ✅ |

## Negative Numbers

| Input | Expected | Result |
|-------|----------|--------|
| `-5 grādi` | `mīnus pieci grādi` | ✅ |
| `-10,5 grādi` | `mīnus desmit komats pieci grādi` | ✅ |
| `-1 grāds` | `mīnus viens grāds` | ✅ |

## Large Numbers

| Input | Expected | Result |
|-------|----------|--------|
| `1000 cilvēku` | `tūkstoš cilvēku` | ✅ |
| `3000 gadu` | `trīstūkstoš gadu` | ✅ |
| `5000 gadus` | `piectūkstoš gadus` | ✅ |
| `10000 cilvēku` | `desmit tūkstoši cilvēku` | ✅ |
| `10 000 cilvēku` | `desmit tūkstoši cilvēku` | ✅ |
| `150 000 karavīru` | `simt piecdesmit tūkstoši karavīru` | ✅ |
| `2 000 000 cilvēku` | `divi miljoni cilvēku` | ✅ |

## Percentages

| Input | Expected | Result |
|-------|----------|--------|
| `5%` | `pieci procenti` | ✅ |
| `21%` | `divdesmit viens procents` | ✅ |
| `100%` | `simts procentu` | ✅ |
| `0,5%` | `nulle komats pieci procenti` | ✅ |
| `Inflācija sasniedza 3,5%` | `Inflācija sasniedza trīs komats piecus procentus` | ✅ |
| `Inflācija sasniedza 3,5 procentus` | `Inflācija sasniedza trīs komats piecus procentus` | ✅ |
| `sasniedza 5%` | `sasniedza piecus procentus` | ✅ |
| `par 3,5%` | `par trīs komats pieciem procentiem` | ✅ |
| `no 5%` | `no piecu procentu` | ✅ |
| `pārsniedza 15–20%` | `pārsniedza piecpadsmit līdz divdesmit procentus` | ✅ |

## Scores

| Input | Expected | Result |
|-------|----------|--------|
| `Rezultāts 3:2` | `Rezultāts trīs divi` | ✅ |
| `1:0` | `viens nulle` | ✅ |
| `Spēle beidzās 4:3` | `Spēle beidzās četri trīs` | ✅ |

## Ranges

| Input | Expected | Result |
|-------|----------|--------|
| `5–10 gadus` | `piecus līdz desmit gadus` | ✅ |
| `18–65 gadi` | `astoņpadsmit līdz sešdesmit pieci gadi` | ✅ |
| `2–5 minūtes` | `divas līdz piecas minūtes` | ✅ |
| `6-8 cilvēki` | `seši līdz astoņi cilvēki` | ✅ |
