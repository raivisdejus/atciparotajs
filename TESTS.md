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

## Roman

| Input | Expected | Result |
|-------|----------|--------|
| `II pasaules karš` | `otrais pasaules karš` | ✅ |
| `XIV gs.` | `četrpadsmitais gadsimts` | ✅ |
| `V nodaļa` | `piektā nodaļa` | ✅ |
| `XIX gs.` | `deviņpadsmitais gadsimts` | ✅ |
| `XXI gs.` | `divdesmit pirmais gadsimts` | ✅ |
| `XX gadsimtā` | `divdesmitajā gadsimtā` | ✅ |

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
