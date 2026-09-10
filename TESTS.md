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
| `11 māju` | `vienpadsmit māju` | ✅ |
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
| `100 gramu` | `simts gramu` | ✅ |
| `Man ir 30` | `Man ir trīsdesmit` | ✅ |
| `Viņam ir 25 gadi` | `Viņam ir divdesmit pieci gadi` | ✅ |
| `Viņai bija 18 gadu` | `Viņai bija astoņpadsmit gadu` | ✅ |
| `apmēram 200 cilvēku` | `apmēram divsimt cilvēku` | ✅ |
| `aptuveni 5 km` | `aptuveni pieci kilometri` | ✅ |
| `5 gadus vecs` | `piecus gadus vecs` | ✅ |
| `30 gadus veca` | `trīsdesmit gadus veca` | ✅ |

## Ordinals

| Input | Expected | Result |
|-------|----------|--------|
| `5. maijs` | `piektais maijs` | ✅ |
| `1. maijā` | `pirmajā maijā` | ✅ |
| `3. vieta` | `trešā vieta` | ✅ |
| `3. vietā` | `trešajā vietā` | ✅ |
| `2. vieta` | `otrā vieta` | ✅ |
| `2. vietā` | `otrajā vietā` | ✅ |
| `1. vieta` | `pirmā vieta` | ✅ |
| `1. vietā` | `pirmajā vietā` | ✅ |
| `21 vieta` | `divdesmit viena vieta` | ✅ |
| `21. vieta` | `divdesmit pirmā vieta` | ✅ |
| `7. nodaļa` | `septītā nodaļa` | ✅ |
| `5. nodaļa` | `piektā nodaļa` | ✅ |
| `10. nodaļa` | `desmitā nodaļa` | ✅ |
| `100. jubileja` | `simtā jubileja` | ✅ |
| `1000. diena` | `tūkstošā diena` | ✅ |
| `janvāra 15.` | `janvāra piecpadsmitais` | ✅ |
| `ierādīja 3.` | `ierādīja trešais` | ✅ |

## Acronym Not Roman

| Input | Expected | Result |
|-------|----------|--------|
| `VID` | `VID` | ✅ |
| `VIDM` | `VIDM` | ✅ |
| `LV` | `LV` | ✅ |
| `ID` | `ID` | ✅ |
| `CV` | `CV` | ✅ |
| `MI` | `MI` | ✅ |
| `DI` | `DI` | ✅ |
| `LIC` | `LIC` | ✅ |
| `CD` | `CD` | ✅ |
| `DVD` | `DVD` | ✅ |
| `VID Muitas pārvalde` | `VID Muitas pārvalde` | ✅ |
| `LV rullē` | `LV rullē` | ✅ |

## Roman

| Input | Expected | Result |
|-------|----------|--------|
| `II pasaules karš` | `otrais pasaules karš` | ✅ |
| `XIV gs.` | `četrpadsmitais gadsimts` | ✅ |
| `pārvaldes V nodaļa` | `pārvaldes piektā nodaļa` | ✅ |
| `V nodaļa` | `piektā nodaļa` | ✅ |
| `XIX gs.` | `deviņpadsmitais gadsimts` | ✅ |
| `XXI gs.` | `divdesmit pirmais gadsimts` | ✅ |
| `XX gadsimtā` | `divdesmitajā gadsimtā` | ✅ |
| `IV sējums` | `ceturtais sējums` | ✅ |
| `III daļa` | `trešā daļa` | ✅ |
| `V pants` | `piektais pants` | ✅ |
| `X klasē` | `desmitajā klasē` | ✅ |

## Fractions

| Input | Expected | Result |
|-------|----------|--------|
| `21,5 grami` | `divdesmit viens komats pieci grami` | ✅ |
| `21.5 grami` | `divdesmit viens komats pieci grami` | ✅ |
| `3,14` | `trīs komats četrpadsmit` | ✅ |
| `1,5 stundas` | `viena komats piecas stundas` | ✅ |
| `2,5 stundas` | `divas komats piecas stundas` | ✅ |
| `1,25 stundas` | `viena komats divdesmit piecas stundas` | ✅ |
| `0,5` | `nulle komats pieci` | ✅ |

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
| `100 g kultūras` | `simts gramu kultūras` | ✅ |
| `10 ml` | `desmit mililitru` | ✅ |
| `10 cm` | `desmit centimetru` | ✅ |
| `10 mm` | `desmit milimetru` | ✅ |

## Non Abbreviations

| Input | Expected | Result |
|-------|----------|--------|
| `mežiem.` | `mežiem.` | ✅ |
| `koks aug.` | `koks aug.` | ✅ |
| `koeficientiem.` | `koeficientiem.` | ✅ |
| `cilvēkiem.` | `cilvēkiem.` | ✅ |
| `un tad vēl.` | `un tad vēl.` | ✅ |
| `liels ceļojums.` | `liels ceļojums.` | ✅ |
| `viņi devās mājup.` | `viņi devās mājup.` | ✅ |
| `tas notika rudenī.` | `tas notika rudenī.` | ✅ |
| `labs darbs, kolēģi.` | `labs darbs, kolēģi.` | ✅ |

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
| `1941 – 1945 gadā` | `tūkstoš deviņsimt četrdesmit pirmajā līdz tūkstoš deviņsimt četrdesmit piektajā gadā` | ✅ |
| `1927. un 1928. gadā` | `tūkstoš deviņsimt divdesmit septītajā un tūkstoš deviņsimt divdesmit astotajā gadā` | ✅ |
| `no 1942. gada 4. jūnija līdz 7. jūnijam` | `no tūkstoš deviņsimt četrdesmit otrā gada ceturtā jūnija līdz septītajam jūnijam` | ✅ |

## Initials Not Roman

| Input | Expected | Result |
|-------|----------|--------|
| `Kārlis V. uzvarēja` | `Kārlis V. uzvarēja` | ✅ |
| `V. Bērziņš uzvarēja` | `V. Bērziņš uzvarēja` | ✅ |
| `Jānis A. sacīja` | `Jānis A. sacīja` | ✅ |

## Nr Keeps Digits

| Input | Expected | Result |
|-------|----------|--------|
| `Vilciens nr. 67` | `Vilciens numur sešdesmit septiņi` | ✅ |
| `Autobuss nr. 3` | `Autobuss numur trīs` | ✅ |
| `Autobuss Nr. 3` | `Autobuss numur trīs` | ✅ |

## Lpp Plural

| Input | Expected | Result |
|-------|----------|--------|
| `58 lpp. gara grāmata` | `piecdesmit astoņas lappuses gara grāmata` | ✅ |
| `1 lpp.` | `viena lappuse` | ✅ |
| `100 lpp.` | `simts lappušu` | ✅ |
| `11 lpp.` | `vienpadsmit lappušu` | ✅ |
| `21 lpp.` | `divdesmit viena lappuse` | ✅ |

## Clock Time

| Input | Expected | Result |
|-------|----------|--------|
| `Vilciens pienāks 10:45` | `Vilciens pienāks desmitos četrdesmit piecās` | ✅ |
| `Pulksten 1:00` | `Pulksten vienos` | ✅ |
| `Sanāksme sākas 14:30` | `Sanāksme sākas četrpadsmitos trīsdesmit` | ✅ |
| `9:05` | `deviņos piecās` | ✅ |
| `8:00` | `astoņos` | ✅ |
| `12:00` | `divpadsmitos` | ✅ |
| `23:59` | `divdesmit trijos piecdesmit deviņās` | ✅ |

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
| `6000 gadu` | `seštūkstoš gadu` | ✅ |
| `6420 cilvēku` | `seštūkstoš četrsimt divdesmit cilvēku` | ✅ |
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
| `sasniedza 3,5%` | `sasniedza trīs komats piecus procentus` | ✅ |
| `sasniedza 2.5%` | `sasniedza divus komats piecus procentus` | ✅ |
| `sasniedza 2,5% slieksni` | `sasniedza divu komats piecu procentu slieksni` | ✅ |
| `sasniedza 3,5 procentus` | `sasniedza trīs komats piecus procentus` | ✅ |
| `sasniedza 5%` | `sasniedza piecus procentus` | ✅ |
| `par 3,5%` | `par trīs komats pieciem procentiem` | ✅ |
| `no 1%` | `no viena procenta` | ✅ |
| `no 5%` | `no pieciem procentiem` | ✅ |
| `pārsniedza 5% slieksni` | `pārsniedza piecu procentu slieksni` | ✅ |
| `pārsniedza 15–20%` | `pārsniedza piecpadsmit līdz divdesmit procentus` | ✅ |
| `6.—9. augustā` | `sestajā līdz devītajā augustā` | ✅ |

## Scores

| Input | Expected | Result |
|-------|----------|--------|
| `Rezultāts 3:2` | `Rezultāts trīs divi` | ✅ |
| `1:0` | `viens nulle` | ✅ |
| `Spēle beidzās 4:3` | `Spēle beidzās četri trīs` | ✅ |
| `Rezultāts: 2:1` | `Rezultāts: divi viens` | ✅ |

## Ranges

| Input | Expected | Result |
|-------|----------|--------|
| `5–10 gadus` | `piecus līdz desmit gadus` | ✅ |
| `18–65 gadi` | `astoņpadsmit līdz sešdesmit pieci gadi` | ✅ |
| `2–5 minūtes` | `divas līdz piecas minūtes` | ✅ |
| `5–10 minūtes` | `piecas līdz desmit minūtes` | ✅ |
| `6-8 cilvēki` | `seši līdz astoņi cilvēki` | ✅ |
| `6-8 cilvēkiem` | `sešiem līdz astoņiem cilvēkiem` | ✅ |
| `5–10 cilvēki` | `pieci līdz desmit cilvēki` | ✅ |
| `0–2 milimetri` | `nulle līdz divi milimetri` | ✅ |
| `0–1,5 milimetri` | `nulle līdz viens komats pieci milimetri` | ✅ |
| `0–1,5 milimetru` | `nulle līdz vienu komats piecu milimetru` | ✅ |
| `1,5–3 milimetri` | `viens komats pieci līdz trīs milimetri` | ✅ |
| `2,5–3,5 kilogrami` | `divi komats pieci līdz trīs komats pieci kilogrami` | ✅ |
| `0…2 milimetri` | `nulle līdz divi milimetri` | ✅ |
| `0...1,5 milimetri` | `nulle līdz viens komats pieci milimetri` | ✅ |
| `Svētdien: pārsvarā sauss, 0–1,5 milimetri;` | `Svētdien: pārsvarā sauss, nulle līdz viens komats pieci milimetri;` | ✅ |

## Unit Ranges

| Input | Expected | Result |
|-------|----------|--------|
| `0–2 mm` | `nulle līdz divi milimetri` | ✅ |
| `0-2 mm` | `nulle līdz divi milimetri` | ✅ |
| `0 – 2 mm` | `nulle līdz divi milimetri` | ✅ |
| `0…2 mm` | `nulle līdz divi milimetri` | ✅ |
| `0...2 mm` | `nulle līdz divi milimetri` | ✅ |
| `0–1,5 mm` | `nulle līdz viens komats pieci milimetri` | ✅ |
| `1,5–3 mm` | `viens komats pieci līdz trīs milimetri` | ✅ |
| `10–15 mm` | `desmit līdz piecpadsmit milimetru` | ✅ |
| `20–21 mm` | `divdesmit līdz divdesmit viens milimetrs` | ✅ |
| `3–5 km` | `trīs līdz pieci kilometri` | ✅ |
| `10–20 cm` | `desmit līdz divdesmit centimetru` | ✅ |
| `Sestdien: pārsvarā sauss, 0–2 mm; vējš 3–5 m/s.` | `Sestdien: pārsvarā sauss, nulle līdz divi milimetri; vējš trīs līdz pieci metri sekundē.` | ✅ |
| `5–10 cilvēki` | `pieci līdz desmit cilvēki` | ✅ |
| `5–10%` | `piecus līdz desmit procentus` | ✅ |

## Phones

| Input | Expected | Result |
|-------|----------|--------|
| `tel. 67 030 638` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |
| `tel: 67 030 638` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |
| `tel 67 030 638` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |
| `tel.67030638` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |
| `tālr. 67030638` | `seši septiņi nulle trīs nulle seši trīs astoņi` | ✅ |
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
| `2,003 eiro` | `divi komats nulle nulle trīs eiro` | ✅ |

## Weight Kg

| Input | Expected | Result |
|-------|----------|--------|
| `1 kg` | `viens kilograms` | ✅ |
| `2 kg` | `divi kilogrami` | ✅ |
| `5 kg` | `pieci kilogrami` | ✅ |
| `10 kg` | `desmit kilogramu` | ✅ |
| `11 kg` | `vienpadsmit kilogramu` | ✅ |
| `21 kg` | `divdesmit viens kilograms` | ✅ |
| `100 kg` | `simts kilogramu` | ✅ |

## Subtitle Ordinals

| Input | Expected | Result |
|-------|----------|--------|
| `2. sezona` | `otrā sezona` | ✅ |
| `3. sērija` | `trešā sērija` | ✅ |
| `1. sērijā` | `pirmajā sērijā` | ✅ |
| `10. sērija` | `desmitā sērija` | ✅ |
| `21. sērija` | `divdesmit pirmā sērija` | ✅ |
| `4. daļa` | `ceturtā daļa` | ✅ |
| `sezona 2, 3. sērija` | `otrā sezona, trešā sērija` | ✅ |

## Decades

| Input | Expected | Result |
|-------|----------|--------|
| `70. gados` | `septiņdesmitajos gados` | ✅ |
| `80. gados` | `astoņdesmitajos gados` | ✅ |
| `90. gados` | `deviņdesmitajos gados` | ✅ |
| `90. gadu` | `deviņdesmito gadu` | ✅ |
| `90. gadi` | `deviņdesmitie gadi` | ✅ |
| `20. gados` | `divdesmitajos gados` | ✅ |

## Date Sentences

| Input | Expected | Result |
|-------|----------|--------|
| `Tas notika 1945. gadā` | `Tas notika tūkstoš deviņsimt četrdesmit piektajā gadā` | ✅ |
| `2024. gada 1. janvārī` | `divi tūkstoši divdesmit ceturtā gada pirmajā janvārī` | ✅ |

## Temperature

| Input | Expected | Result |
|-------|----------|--------|
| `36°C` | `trīsdesmit seši grādi` | ✅ |
| `100°F` | `simts grādi` | ✅ |
| `90°` | `deviņdesmit grādi` | ✅ |
| `1°C` | `viens grāds` | ✅ |
| `21°` | `divdesmit viens grāds` | ✅ |
| `11°C` | `vienpadsmit grādi` | ✅ |
| `0°` | `nulle grādu` | ✅ |
| `2°` | `divi grādi` | ✅ |
| `21 °C` | `divdesmit viens grāds` | ✅ |
| `-5 °C` | `mīnus pieci grādi` | ✅ |
| `-5°C` | `mīnus pieci grādi` | ✅ |
| `-1°C` | `mīnus viens grāds` | ✅ |
| `0°C` | `nulle grādu` | ✅ |
| `+21°C` | `plus divdesmit viens grāds` | ✅ |
| `+21 °C` | `plus divdesmit viens grāds` | ✅ |
| `+1°C` | `plus viens grāds` | ✅ |
| `14…15°C` | `četrpadsmit līdz piecpadsmit grādi` | ✅ |
| `14…15 °C` | `četrpadsmit līdz piecpadsmit grādi` | ✅ |
| `14...15 °C` | `četrpadsmit līdz piecpadsmit grādi` | ✅ |
| `14–15°C` | `četrpadsmit līdz piecpadsmit grādi` | ✅ |
| `14-15 °C` | `četrpadsmit līdz piecpadsmit grādi` | ✅ |
| `14 – 15 °C` | `četrpadsmit līdz piecpadsmit grādi` | ✅ |
| `20…21°` | `divdesmit līdz divdesmit viens grāds` | ✅ |
| `-5…-3°C` | `mīnus pieci līdz mīnus trīs grādi` | ✅ |
| `-5…+3 °C` | `mīnus pieci līdz plus trīs grādi` | ✅ |
| `-5…0°C` | `mīnus pieci līdz nulle grādu` | ✅ |
| `-2…0 °C` | `mīnus divi līdz nulle grādu` | ✅ |
| `0…+3°C` | `nulle līdz plus trīs grādi` | ✅ |
| `-3…+1 °C` | `mīnus trīs līdz plus viens grāds` | ✅ |
| `+5 grādi` | `plus pieci grādi` | ✅ |
| `-5 grādi` | `mīnus pieci grādi` | ✅ |
| `14–15 grādi` | `četrpadsmit līdz piecpadsmit grādi` | ✅ |
| `+14…+15 grādi` | `plus četrpadsmit līdz plus piecpadsmit grādi` | ✅ |
| `-1…0 grādi` | `mīnus viens līdz nulle grādi` | ✅ |
| `21 grādi` | `divdesmit viens grādi` | ✅ |
| `+21 grādi` | `plus divdesmit viens grādi` | ✅ |
| `-1 grāds` | `mīnus viens grāds` | ✅ |
| `20…21 grādi` | `divdesmit līdz divdesmit viens grādi` | ✅ |
| `+21…+22 grādos` | `plus divdesmit vienā līdz plus divdesmit divos grādos` | ✅ |
| `36,6°C` | `trīsdesmit seši komats seši grādi` | ✅ |
| `21,1°C` | `divdesmit viens komats viens grāds` | ✅ |
| `Ceturtdien: +14…+15 °C` | `Ceturtdien: plus četrpadsmit līdz plus piecpadsmit grādi` | ✅ |
| `naktī +9…+10 °C, dienā +18…+19 °C` | `naktī plus deviņi līdz plus desmit grādi, dienā plus astoņpadsmit līdz plus deviņpadsmit grādi` | ✅ |

## Tonnes

| Input | Expected | Result |
|-------|----------|--------|
| `53T` | `piecdesmit trīs tonnas` | ✅ |
| `1T` | `viena tonna` | ✅ |
| `1 T` | `viena tonna` | ✅ |
| `10T` | `desmit tonnu` | ✅ |
| `21T` | `divdesmit viena tonna` | ✅ |
| `5 T` | `piecas tonnas` | ✅ |
| `11T` | `vienpadsmit tonnu` | ✅ |

## Vulgar Fractions

| Input | Expected | Result |
|-------|----------|--------|
| `3/4` | `trīs ceturtdaļas` | ✅ |
| `1/2` | `viena puse` | ✅ |
| `9/10` | `deviņas desmitdaļas` | ✅ |
| `2 1/4` | `divi veseli viena ceturtdaļa` | ✅ |
| `1 1/2` | `viens vesels viena puse` | ✅ |
| `1/3` | `viena trešdaļa` | ✅ |
| `2/3` | `divas trešdaļas` | ✅ |
| `5/8` | `piecas astotdaļas` | ✅ |

## No Roman

| Input | Expected | Result |
|-------|----------|--------|
| `II pasaules karš` | `II pasaules karš` | ✅ |
| `V nodaļa` | `V nodaļa` | ✅ |
| `XIV gs.` | `XIV gadsimts` | ✅ |

## Class Notation

| Input | Expected | Result |
|-------|----------|--------|
| `4.D klase` | `ceturtā d klase` | ✅ |
| `4.d klasei` | `ceturtajai d klasei` | ✅ |
| `1.A klase` | `pirmā a klase` | ✅ |
| `10.B klase` | `desmitā b klase` | ✅ |

## Masculine Ordinals

| Input | Expected | Result |
|-------|----------|--------|
| `3. stāvs` | `trešais stāvs` | ✅ |
| `2. kanāls` | `otrais kanāls` | ✅ |
| `1. iemesls` | `pirmais iemesls` | ✅ |
| `3. stāvā` | `trešajā stāvā` | ✅ |
| `5. maijam` | `piektajam maijam` | ✅ |
| `3. stāvam` | `trešajam stāvam` | ✅ |
| `1. vietai` | `pirmajai vietai` | ✅ |
| `par 3. vietu` | `par trešo vietu` | ✅ |
| `1. iemesls` | `pirmais iemesls` | ✅ |

## Repetitions

| Input | Expected | Result |
|-------|----------|--------|
| `1 reize` | `viena reize` | ✅ |
| `2 reizes` | `divas reizes` | ✅ |
| `3 reizes` | `trīs reizes` | ✅ |
| `5 reizes` | `piecas reizes` | ✅ |
| `10 reizes` | `desmit reizes` | ✅ |
| `3 reizēm` | `trim reizēm` | ✅ |

## Clock Time Plkst

| Input | Expected | Result |
|-------|----------|--------|
| `plkst. 10:45` | `pulksten desmitos četrdesmit piecās` | ✅ |
| `plkst. 9:00` | `pulksten deviņos` | ✅ |
| `plkst. 14:30` | `pulksten četrpadsmitos trīsdesmit` | ✅ |

## Score Edge

| Input | Expected | Result |
|-------|----------|--------|
| `0:0` | `nulle nulle` | ✅ |
| `0:3` | `nulle trīs` | ✅ |
| `10:0` | `desmit nulle` | ✅ |

## Ordinal Centuries

| Input | Expected | Result |
|-------|----------|--------|
| `3. gadsimta sākumā` | `trešā gadsimta sākumā` | ✅ |
| `20. gadsimta sākumā` | `divdesmitā gadsimta sākumā` | ✅ |
| `21. gadsimtā` | `divdesmit pirmajā gadsimtā` | ✅ |

## Percentage Prepositions

| Input | Expected | Result |
|-------|----------|--------|
| `par 1%` | `par vienu procentu` | ✅ |
| `par 5%` | `par pieciem procentiem` | ✅ |
| `līdz 50%` | `līdz piecdesmit procentiem` | ✅ |
| `virs 90%` | `virs deviņdesmit procentiem` | ✅ |

## Speed

| Input | Expected | Result |
|-------|----------|--------|
| `1 km/h` | `viens kilometrs stundā` | ✅ |
| `2 km/h` | `divi kilometri stundā` | ✅ |
| `11 km/h` | `vienpadsmit kilometru stundā` | ✅ |
| `21 km/h` | `divdesmit viens kilometrs stundā` | ✅ |
| `100 km/h` | `simts kilometru stundā` | ✅ |
| `80–100 km/h` | `astoņdesmit līdz simts kilometru stundā` | ✅ |
| `1 m/s` | `viens metrs sekundē` | ✅ |
| `5 m/s` | `pieci metri sekundē` | ✅ |
| `10 m/s` | `desmit metru sekundē` | ✅ |
| `21 m/s` | `divdesmit viens metrs sekundē` | ✅ |
| `2,5 m/s` | `divi komats pieci metri sekundē` | ✅ |
| `5–8 m/s` | `pieci līdz astoņi metri sekundē` | ✅ |
| `vējš 5–8 m/s, brāzmās 15 m/s` | `vējš pieci līdz astoņi metri sekundē, brāzmās piecpadsmit metru sekundē` | ✅ |

## Age Gate

| Input | Expected | Result |
|-------|----------|--------|
| `18+` | `astoņpadsmit plus` | ✅ |
| `16+` | `sešpadsmit plus` | ✅ |
| `6+` | `seši plus` | ✅ |
| `Filma ir 18+` | `Filma ir astoņpadsmit plus` | ✅ |

## Episode Notation

| Input | Expected | Result |
|-------|----------|--------|
| `S02E03` | `S02E03` | ✅ |
| `S01E01` | `S01E01` | ✅ |
| `Skatāmies S02E03` | `Skatāmies S02E03` | ✅ |

## Academic Year

| Input | Expected | Result |
|-------|----------|--------|
| `2023./2024. mācību gads` | `divi tūkstoši divdesmit trešais līdz divi tūkstoši divdesmit ceturtais mācību gads` | ✅ |
| `2023./2024. mācību gadā` | `divi tūkstoši divdesmit trešajā līdz divi tūkstoši divdesmit ceturtajā mācību gadā` | ✅ |

## Decimal Leading Zeros

| Input | Expected | Result |
|-------|----------|--------|
| `1237,06 vienības` | `tūkstoš divsimt trīsdesmit septiņas komats nulle sešas vienības` | ✅ |
| `1237,6 vienības` | `tūkstoš divsimt trīsdesmit septiņas komats sešas vienības` | ✅ |
| `1237,60 vienības` | `tūkstoš divsimt trīsdesmit septiņas komats sešdesmit vienības` | ✅ |
| `10,01 punkti` | `desmit komats nulle vieni punkti` | ✅ |
| `10,01 punkts` | `desmit komats nulle viens punkts` | ✅ |
| `0,05` | `nulle komats nulle pieci` | ✅ |
| `0,5` | `nulle komats pieci` | ✅ |
| `2,003 kg` | `divi komats nulle nulle trīs kilogrami` | ✅ |
| `0,001 g` | `nulle komats nulle nulle viens grams` | ✅ |
| `1,00 kg` | `viens komats nulle nulle kilogramu` | ✅ |
| `0,05%` | `nulle komats nulle pieci procenti` | ✅ |

## Decimal Units

| Input | Expected | Result |
|-------|----------|--------|
| `2,5 kg` | `divi komats pieci kilogrami` | ✅ |
| `1,5 km` | `viens komats pieci kilometri` | ✅ |
| `1,1 kg` | `viens komats viens kilograms` | ✅ |
| `2,10 kg` | `divi komats desmit kilogramu` | ✅ |
| `2,5 m²` | `divi komats pieci kvadrātmetri` | ✅ |
| `1,5 km/h` | `viens komats pieci kilometri stundā` | ✅ |
| `12,5 lpp.` | `divpadsmit komats piecas lappuses` | ✅ |
| `1,5 T` | `viena komats piecas tonnas` | ✅ |
| `2,1 T` | `divas komats viena tonna` | ✅ |
| `36,6°C` | `trīsdesmit seši komats seši grādi` | ✅ |
| `21,1°C` | `divdesmit viens komats viens grāds` | ✅ |
| `2,5 kg maisā` | `divi komats pieci kilogrami maisā` | ✅ |

## Currency Word

| Input | Expected | Result |
|-------|----------|--------|
| `1237,06 eiro` | `tūkstoš divsimt trīsdesmit septiņi komats nulle seši eiro` | ✅ |
| `1237,6 eiro` | `tūkstoš divsimt trīsdesmit septiņi komats seši eiro` | ✅ |
| `1237,60 eiro` | `tūkstoš divsimt trīsdesmit septiņi komats sešdesmit eiro` | ✅ |
| `10,01 eiro` | `desmit komats nulle viens eiro` | ✅ |
| `1 eiro` | `viens eiro` | ✅ |
| `5 eiro` | `pieci eiro` | ✅ |
| `11 eiro` | `vienpadsmit eiro` | ✅ |
| `2,50 euro` | `divi komats piecdesmit euro` | ✅ |
| `Prece maksā 2,50 eiro.` | `Prece maksā divi komats piecdesmit eiro.` | ✅ |
| `eiro kurss` | `eiro kurss` | ✅ |

## Dotted Clock Times

| Input | Expected | Result |
|-------|----------|--------|
| `plkst. 10.00` | `pulksten desmitos` | ✅ |
| `pulksten 9.05` | `pulksten deviņos piecās` | ✅ |
| `plkst 14.30` | `plkst četrpadsmitos trīsdesmit` | ✅ |
| `plkst. 10:00–10:30` | `pulksten desmitos līdz desmitos trīsdesmit` | ✅ |
| `plkst. 10.00–10.30` | `pulksten desmitos līdz desmitos trīsdesmit` | ✅ |
| `plkst. 10.00 – 10.30` | `pulksten desmitos līdz desmitos trīsdesmit` | ✅ |
| `10:00–10:30` | `desmitos līdz desmitos trīsdesmit` | ✅ |
| `10.00–10.30` | `desmitos līdz desmitos trīsdesmit` | ✅ |
| `10.00-10.30` | `desmitos līdz desmitos trīsdesmit` | ✅ |
| `23.59–00.30` | `divdesmit trijos piecdesmit deviņās līdz nullē trīsdesmit` | ✅ |
| `plkst. 10.00–10.30.` | `pulksten desmitos līdz desmitos trīsdesmit.` | ✅ |
| `no plkst. 10.00 līdz 10.30` | `no pulksten desmitos līdz desmitos trīsdesmit` | ✅ |
| `Ielikts kalendārā: 7. septembrī, plkst. 10.00–10.30.` | `Ielikts kalendārā: septītajā septembrī, pulksten desmitos līdz desmitos trīsdesmit.` | ✅ |

## Dotted Numbers Are Not Times

| Input | Expected | Result |
|-------|----------|--------|
| `12.30` | `divpadsmit komats trīsdesmit` | ✅ |
| `21.5 grami` | `divdesmit viens komats pieci grami` | ✅ |
| `21,5 grami` | `divdesmit viens komats pieci grami` | ✅ |
| `1.10` | `viens komats desmit` | ✅ |
| `9.60` | `deviņi komats sešdesmit` | ✅ |
| `3.–5. klase` | `trešā līdz piektā klase` | ✅ |
| `1. – 2. vieta` | `pirmā – otrā vieta` | ✅ |

## Ordinal Without Space

| Input | Expected | Result |
|-------|----------|--------|
| `2026.gada augusts` | `divi tūkstoši divdesmit sestā gada augusts` | ✅ |
| `2026.gadā` | `divi tūkstoši divdesmit sestajā gadā` | ✅ |
| `2026.g.` | `divi tūkstoši divdesmit sestais gads` | ✅ |
| `15.augustā` | `piecpadsmitajā augustā` | ✅ |
| `3.vieta` | `trešā vieta` | ✅ |
| `1.klase` | `pirmā klase` | ✅ |
| `2.pants` | `otrais pants` | ✅ |
| `XX.gadsimts` | `divdesmitais gadsimts` | ✅ |
| `2026.gada 5.maijā` | `divi tūkstoši divdesmit sestā gada piektajā maijā` | ✅ |
| `(2026.gada)` | `(divi tūkstoši divdesmit sestā gada)` | ✅ |
| `2026.gada.` | `divi tūkstoši divdesmit sestā gada.` | ✅ |
| `3., 4. vieta` | `trešā, ceturtā vieta` | ✅ |
| `3.,4.vieta` | `trešā,ceturtā vieta` | ✅ |
| `1941.-1945.gads` | `tūkstoš deviņsimt četrdesmit pirmais līdz tūkstoš deviņsimt četrdesmit piektais gads` | ✅ |
| `2023./2024.gads` | `divi tūkstoši divdesmit trešais līdz divi tūkstoši divdesmit ceturtais gads` | ✅ |
| `4.D klase` | `ceturtā d klase` | ✅ |
| `5.5` | `pieci komats pieci` | ✅ |
| `Viņam ir 25.` | `Viņam ir divdesmit piektais` | ✅ |

## Glued Initials

| Input | Expected | Result |
|-------|----------|--------|
| `A.Briāna ielā 16` | `A.Briāna ielā sešpadsmit` | ✅ |
| `V.Bērziņš` | `V.Bērziņš` | ✅ |

## Glued Units

| Input | Expected | Result |
|-------|----------|--------|
| `5km` | `pieci kilometri` | ✅ |
| `2,5kg` | `divi komats pieci kilogrami` | ✅ |
| `10m²` | `desmit kvadrātmetru` | ✅ |
| `0–2mm` | `nulle līdz divi milimetri` | ✅ |
| `5lpp.` | `piecas lappuses` | ✅ |
| `5min` | `piecimin` | ✅ |
| `5 m/s` | `pieci metri sekundē` | ✅ |
| `100km/h` | `simts kilometru stundā` | ✅ |

## Spaced Thousands

| Input | Expected | Result |
|-------|----------|--------|
| `150 000 eiro` | `simt piecdesmit tūkstoši eiro` | ✅ |
| `150  000 eiro` | `simt piecdesmit tūkstoši eiro` | ✅ |

## Spaced Abbreviations

| Input | Expected | Result |
|-------|----------|--------|
| `u. c.` | `un citi` | ✅ |
| `u. tml.` | `un tamlīdzīgi` | ✅ |
| `t. i.` | `tas ir` | ✅ |
| `pr. Kr.` | `pirms Kristus` | ✅ |
| `p. Kr.` | `pēc Kristus` | ✅ |

## Abbreviation Glued To Digit

| Input | Expected | Result |
|-------|----------|--------|
| `Nr.5` | `numur pieci` | ✅ |
| `nr.5` | `numur pieci` | ✅ |
| `lpp.5` | `lappuse pieci` | ✅ |

## Glued Clock Times

| Input | Expected | Result |
|-------|----------|--------|
| `plkst.10.00` | `pulksten desmitos` | ✅ |
| `plkst.10.00 līdz 11.30` | `pulksten desmitos līdz vienpadsmitos trīsdesmit` | ✅ |
| `plkst. 10.00` | `pulksten desmitos` | ✅ |

## Long Digit Strings

| Input | Expected | Result |
|-------|----------|--------|
| `01000230010002` | `nulle viens nulle nulle nulle divi trīs nulle nulle viens nulle nulle nulle divi` | ✅ |
| `kadastra apzīmējums: 01000230010002` | `kadastra apzīmējums: nulle viens nulle nulle nulle divi trīs nulle nulle viens nulle nulle nulle divi` | ✅ |
| `1234567890` | `viens divi trīs četri pieci seši septiņi astoņi deviņi nulle` | ✅ |
| `123456789 eiro` | `simt divdesmit trīs miljoni četrsimt piecdesmit seši tūkstoši septiņsimt astoņdesmit deviņi eiro` | ✅ |
| `0` | `nulle` | ✅ |
| `05.05.2026` | `pieci komats nulle pieci.divtūkstoš divdesmit seši` | ✅ |

## Billions

| Input | Expected | Result |
|-------|----------|--------|
| `n=1000000000` | `viens miljards` | ✅ |
| `n=2500000000` | `divi miljardi piecsimt miljoni` | ✅ |
| `n=1000000` | `viens miljons` | ✅ |

## Units Before Closing Punctuation

| Input | Expected | Result |
|-------|----------|--------|
| `“5km”` | `“pieci kilometri”` | ✅ |
| `(5 km)` | `(pieci kilometri)` | ✅ |
| `5km!` | `pieci kilometri!` | ✅ |
| `5 km?` | `pieci kilometri?` | ✅ |
| `5 km:` | `pieci kilometri:` | ✅ |
| `“2,5kg”` | `“divi komats pieci kilogrami”` | ✅ |
| `“10m²”` | `“desmit kvadrātmetru”` | ✅ |
| `“0–2mm”` | `“nulle līdz divi milimetri”` | ✅ |
| `“36°C”` | `“trīsdesmit seši grādi”` | ✅ |
| `“100 km/h”` | `“simts kilometru stundā”` | ✅ |
| `“5 m/s”` | `“pieci metri sekundē”` | ✅ |
| `“53T”` | `“piecdesmit trīs tonnas”` | ✅ |
| `“80–100 km/h”` | `“astoņdesmit līdz simts kilometru stundā”` | ✅ |
| `2026.gada»` | `divi tūkstoši divdesmit sestā gada»` | ✅ |
| `3.…` | `trešais…` | ✅ |
| `5 min` | `pieci min` | ✅ |
| `5min` | `piecimin` | ✅ |
| `5 kmh` | `pieci kmh` | ✅ |
| `2 mājas` | `divas mājas` | ✅ |
| `5. maijs` | `piektais maijs` | ✅ |

## Glued Units Full Line

| Input | Expected | Result |
|-------|----------|--------|
| `Pielipušas mērvienības: “5km”, “2,5kg”, “10m²”, “0–2mm”, “5lpp.” iepriekš deva “piecikm”. Saīsinājums pielipis pie cipara: “Nr.5” deva “numurpieci”.` | `Pielipušas mērvienības: “pieci kilometri”, “divi komats pieci kilogrami”, “desmit kvadrātmetru”, “nulle līdz divi milimetri”, “piecas lappuses” iepriekš deva “piecikm”. Saīsinājums pielipis pie cipara: “numur pieci” deva “numurpieci”.` | ✅ |

## Bucket Stops At Closing Quote

| Input | Expected | Result |
|-------|----------|--------|
| `“Nr.5” deva` | `“numur pieci” deva` | ✅ |
| `(Nr. 5) mājas` | `(numur pieci) mājas` | ✅ |
| `1., 2. un 3. vieta` | `pirmā, otrā un trešā vieta` | ✅ |
| `3.,4.vieta` | `trešā,ceturtā vieta` | ✅ |

## Identifier Codes Are Not Ranges

| Input | Expected | Result |
|-------|----------|--------|
| `BIS-BL-827846-114426` | `BIS-BL-astoņi divi septiņi astoņi četri seši-viens viens četri četri divi seši` | ✅ |
| `lieta BIS-BL-827846-114426, būvdarbu` | `lieta BIS-BL-astoņi divi septiņi astoņi četri seši-viens viens četri četri divi seši, būvdarbu` | ✅ |
| `“BIS-BL-827846-114426”` | `“BIS-BL-astoņi divi septiņi astoņi četri seši-viens viens četri četri divi seši”` | ✅ |
| `ISBN 978-9934-0-1234-5` | `ISBN deviņi septiņi astoņi-deviņi deviņi trīs četri-nulle-viens divi trīs četri-pieci` | ✅ |
| `1941–1945 gads` | `tūkstoš deviņsimt četrdesmit pirmais līdz tūkstoš deviņsimt četrdesmit piektais gads` | ✅ |
| `5–6 grādi` | `pieci līdz seši grādi` | ✅ |
| `0–2 mm` | `nulle līdz divi milimetri` | ✅ |
| `10-20 procenti` | `desmit līdz divdesmit procenti` | ✅ |
| `80–100 km/h` | `astoņdesmit līdz simts kilometru stundā` | ✅ |

## Hyphen After Letter Is Not Minus

| Input | Expected | Result |
|-------|----------|--------|
| `COVID-19` | `COVID-deviņpadsmit` | ✅ |
| `LV-1010` | `LV-tūkstoš desmit` | ✅ |
| `-5` | `mīnus pieci` | ✅ |
| `5 -3` | `piecus mīnus trīs` | ✅ |
| `(-5)` | `(mīnus pieci)` | ✅ |
| `-5°C` | `mīnus pieci grādi` | ✅ |
| `-5…-3°C` | `mīnus pieci līdz mīnus trīs grādi` | ✅ |
