# Atciparotājs

Latvian text preprocessor for TTS engines. Converts digits, numbers, and abbreviations to spoken Latvian words.

Numbers are inflected to agree in gender and grammatical case with the following noun — for example, `2 draugiem` → `diviem draugiem`.

## Features

- **Cardinal numbers** — `5 grami` → `pieci grami`
- **Ordinal numbers** — `5. maijs` → `piektais maijs`
- **Roman numerals** — `XIV gs.` → `četrpadsmitais gadsimts`
- **Decimals/fractions** — `21,5 grami` → `divdesmit viens komats pieci grami`
- **Abbreviation expansion** — `gs.` → `gadsimts`, `km.` → `kilometrs`, and more
- **Phone numbers** — spelled out digit by digit (see below)

## Installation

```bash
pip install atciparotajs
```

## Usage

### Python API

```python
from atciparotajs import convert

convert("5. maijs")          # → "piektais maijs"
convert("2 draugiem")        # → "diviem draugiem"
convert("XIV gs.")           # → "četrpadsmitais gadsimts"
convert("21,5 grami")        # → "divdesmit viens komats pieci grami"

# Disable abbreviation expansion
convert("14. gs.", expand_abbr=False)  # → "četrpadsmitais gs."
```

### Command line

```bash
# Direct argument
atciparotajs "5. maijs"

# Piped input
echo "2 draugiem" | atciparotajs

# Disable abbreviation expansion
atciparotajs --no-expand-abbr "14. gs."
```

### Phone numbers

Phone numbers are detected automatically and read digit by digit:

```bash
atciparotajs "tel. 67 030 638"      # → "seši septiņi nulle trīs nulle seši trīs astoņi"
atciparotajs "mob: 67030638"        # → "seši septiņi nulle trīs nulle seši trīs astoņi"
atciparotajs "+371 67 030 638"      # → "seši septiņi nulle trīs nulle seši trīs astoņi"
```

Recognized prefixes: `tel`, `tel.`, `tel:`, `mob`, `mob.`, `mob:`, and `+371`.

For plain digit strings that should be read as phone numbers rather than as a number,
use the explicit `{phone:…}` markup:

```bash
atciparotajs "{phone:67030638}"     # → "seši septiņi nulle trīs nulle seši trīs astoņi"
```

Without the markup, a bare `67030638` would be read as the cardinal number. 
Use `{phone:…}` whenever you want digit-by-digit pronunciation for a number that has 
no recognizable phone prefix.

## Running tests

```bash
pytest tests/test_numbers.py -v
```

For test cases covered see [test list](TESTS.md) 

## Testing with TTS
For real life TTS testing go to [Latvian-Piper-TTS](https://huggingface.co/spaces/RaivisDejus/Latvian-Piper-TTS) 

## License

MIT
