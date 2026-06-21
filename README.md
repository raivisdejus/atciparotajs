# Atciparotājs

Latvian text preprocessor for TTS engines. Converts digits, numbers, and abbreviations to spoken Latvian words.

Numbers are inflected to agree in gender and grammatical case with the following noun — for example, `2 draugiem` → `diviem draugiem`.

## Features

- **Cardinal numbers** — `5 grami` → `pieci grami`
- **Ordinal numbers** — `5. maijs` → `piektais maijs`
- **Roman numerals** — `XIV gs.` → `četrpadsmitais gadsimts`
- **Decimals/fractions** — `21,5 grami` → `divdesmit viens komats pieci grami`
- **Abbreviation expansion** — `gs.` → `gadsimts`, `km.` → `kilometrs`, and more

## Installation

```bash
git clone https://github.com/raivisdejus/atciparotajs
cd atciparotajs
pip install -e .
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
python -m atciparotajs "5. maijs"

# Piped input
echo "2 draugiem" | python -m atciparotajs

# Disable abbreviation expansion
python -m atciparotajs --no-expand-abbr "14. gs."
```

### Standalone binary

Build a single binary with no Python dependency:

```bash
bash build_binary.sh
./dist/atciparotajs "5. maijs"
```

## Running tests

```bash
pytest tests/test_numbers.py -v
```

The test file is designed to be readable by non-technical Latvian speakers for validation and to add new cases.

## License

MIT
