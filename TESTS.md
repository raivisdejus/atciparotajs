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
| `9 km²` | `deviņi kvadrātkilometri` | ✅ |
| `1 km²` | `viens kvadrātkilometrs` | ✅ |
| `10 km²` | `desmit kvadrātkilometru` | ✅ |
| `5 m²` | `pieci kvadrātmetri` | ✅ |
| `1 m²` | `viens kvadrātmetrs` | ✅ |
| `100 m²` | `simts kvadrātmetru` | ✅ |
| `3 m³` | `trīs kubikmetri` | ✅ |
| `1 m³` | `viens kubikmetrs` | ✅ |
| `20 m³` | `divdesmit kubikmetru` | ✅ |

## Dates

| Input | Expected | Result |
|-------|----------|--------|
| `4. oktobris, 1957. gads` | `ceturtais oktobris, tūkstoš deviņsimt piecdesmit septītais gads` | ✅ |
| `1961. gada 12. aprīlis` | `tūkstoš deviņsimt sešdesmit pirmā gada divpadsmitais aprīlis` | ✅ |
| `1969. gada 20. jūlijā` | `tūkstoš deviņsimt sešdesmit devītā gada divdesmitajā jūlijā` | ✅ |
| `2026. gads` | `divi tūkstoši divdesmit sestais gads` | ✅ |
| `1941.–1945. gads` | `tūkstoš deviņsimt četrdesmit pirmais līdz tūkstoš deviņsimt četrdesmit piektais gads` | ✅ |
| `1941–1945 gads` | `tūkstoš deviņsimt četrdesmit pirmais līdz tūkstoš deviņsimt četrdesmit piektais gads` | ✅ |
| `1941.–1945. gadā` | `tūkstoš deviņsimt četrdesmit pirmajā līdz tūkstoš deviņsimt četrdesmit piektajā gadā` | ✅ |
| `1941–1945 gadā` | `tūkstoš deviņsimt četrdesmit pirmajā līdz tūkstoš deviņsimt četrdesmit piektajā gadā` | ✅ |
| `1927. un 1928. gadā` | `tūkstoš deviņsimt divdesmit septītajā un tūkstoš deviņsimt divdesmit astotajā gadā` | ✅ |
| `no 1942. gada 4. jūnija līdz 7. jūnijam` | `no tūkstoš deviņsimt četrdesmit otrā gada ceturtā jūnija līdz septītajam jūnijam` | ✅ |

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
| `6.—9. augustā` | `sestajā līdz devītajā augustā` | ✅ |

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
| `6-8 cilvēkiem` | `sešiem līdz astoņiem cilvēkiem` | ✅ |

## Phones

| Input | Expected | Result |
|-------|----------|--------|
| `tel. 67 030 638` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |
| `tel: 67 030 638` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |
| `tel 67 030 638` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |
| `tel.67030638` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |
| `mob. 67 030 638` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |
| `mob: 67030638` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |
| `+371 67 030 638` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |
| `+37167030638` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |
| `tel. +371 67 030 638` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |
| `{phone:67030638}` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |

## Currency

| Input | Expected | Result |
|-------|----------|--------|
| `(1, 0, 'EUR')` | `viens eiro` | ✅ |
| `(2, 0, 'EUR')` | `divi eiro` | ✅ |
| `(5, 0, 'EUR')` | `pieci eiro` | ✅ |
| `(11, 0, 'EUR')` | `vienpadsmit eiro` | ✅ |
| `(21, 0, 'EUR')` | `divdesmit viens eiro` | ✅ |
| `(0, 1, 'EUR')` | `nulle eiro un viens cents` | ✅ |
| `(1, 50, 'EUR')` | `viens eiro un piecdesmit centu` | ✅ |
| `(10, 99, 'EUR')` | `desmit eiro un deviņdesmit deviņi centi` | ✅ |
| `(100, 0, 'EUR')` | `simts eiro` | ✅ |
| `(1, 0, 'EUR_LEGAL')` | `viens euro` | ✅ |
| `(3, 0, 'EUR_LEGAL')` | `trīs euro` | ✅ |
| `(1, 0, 'USD')` | `viens dolārs` | ✅ |
| `(2, 0, 'USD')` | `divi dolāri` | ✅ |
| `(10, 0, 'USD')` | `desmit dolāru` | ✅ |
| `(1, 25, 'USD')` | `viens dolārs un divdesmit pieci centi` | ✅ |
| `(1, 0, 'LVL')` | `viens lats` | ✅ |
| `(4, 0, 'LVL')` | `četri lati` | ✅ |
| `(20, 0, 'LVL')` | `divdesmit latu` | ✅ |
| `(1, 1, 'LVL')` | `viens lats un viens santīms` | ✅ |
| `(3, 2, 'LVL')` | `trīs lati un divi santīmi` | ✅ |
| `(10, 15, 'LVL')` | `desmit latu un piecpadsmit santīmu` | ✅ |
| `(1, 0, 'RUB')` | `viens rublis` | ✅ |
| `(5, 0, 'RUB')` | `pieci rubļi` | ✅ |
| `(11, 0, 'RUB')` | `vienpadsmit rubļu` | ✅ |
| `(1, 1, 'RUB')` | `viens rublis un viena kapeika` | ✅ |
| `(2, 2, 'RUB')` | `divi rubļi un divas kapeikas` | ✅ |
| `(10, 10, 'RUB')` | `desmit rubļu un desmit kapeiku` | ✅ |
| `(1, 0, 'GBP')` | `viena sterliņu mārciņa` | ✅ |
| `(3, 0, 'GBP')` | `trīs sterliņu mārciņas` | ✅ |
| `(15, 0, 'GBP')` | `piecpadsmit sterliņu mārciņu` | ✅ |
| `(1, 0, 'SEK')` | `viena krona` | ✅ |
| `(2, 0, 'SEK')` | `divas kronas` | ✅ |
| `(10, 0, 'SEK')` | `desmit kronu` | ✅ |
| `(1, 50, 'SEK')` | `viena krona un piecdesmit ēru` | ✅ |

## Currency Adjective

| Input | Expected | Result |
|-------|----------|--------|
| `(1, 0, 'USD', True)` | `viens ASV dolārs` | ✅ |
| `(10, 0, 'USD', True)` | `desmit ASV dolāru` | ✅ |
| `(1, 0, 'SEK', True)` | `viena Zviedrijas krona` | ✅ |
| `(1, 0, 'AUD', True)` | `viens Austrālijas dolārs` | ✅ |
| `(5, 0, 'EUR', True)` | `pieci eiro` | ✅ |

## Currency Float

| Input | Expected | Result |
|-------|----------|--------|
| `10.5 EUR` | `desmit eiro un piecdesmit centu` | ✅ |
| `1.01 USD` | `viens dolārs un viens cents` | ✅ |
| `2.99 LVL` | `divi lati un deviņdesmit deviņi santīmi` | ✅ |

## Currency In Text

| Input | Expected | Result |
|-------|----------|--------|
| `1,82€` | `viens eiro un astoņdesmit divi centi` | ✅ |
| `5€` | `pieci eiro` | ✅ |
| `1,82$` | `viens dolārs un astoņdesmit divi centi` | ✅ |
| `1,82£` | `viena sterliņu mārciņa un astoņdesmit divi pensi` | ✅ |
| `1,82 €` | `viens eiro un astoņdesmit divi centi` | ✅ |
| `10 €` | `desmit eiro` | ✅ |
| `€1,82` | `viens eiro un astoņdesmit divi centi` | ✅ |
| `$5` | `pieci dolāri` | ✅ |
| `€ 1,82` | `viens eiro un astoņdesmit divi centi` | ✅ |
| `1,82 EUR` | `viens eiro un astoņdesmit divi centi` | ✅ |
| `5 EUR` | `pieci eiro` | ✅ |
| `10,99 USD` | `desmit dolāru un deviņdesmit deviņi centi` | ✅ |
| `1 LVL` | `viens lats` | ✅ |
| `EUR 1,82` | `viens eiro un astoņdesmit divi centi` | ✅ |
| `USD 10,99` | `desmit dolāru un deviņdesmit deviņi centi` | ✅ |
| `EUR 100` | `simts eiro` | ✅ |
| `1.82€` | `viens eiro un astoņdesmit divi centi` | ✅ |
| `EUR 1.82` | `viens eiro un astoņdesmit divi centi` | ✅ |
| `1,8€` | `viens eiro un astoņdesmit centu` | ✅ |
| `Prece maksā 2,50 EUR.` | `Prece maksā divus eiro un piecdesmit centu.` | ✅ |
| `Salāti maksā 1.83EUR` | `Salāti maksā vienu eiro un astoņdesmit trīs centus` | ✅ |
