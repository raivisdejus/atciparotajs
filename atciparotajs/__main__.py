import sys
import argparse
from atciparotajs import convert


def main():
    parser = argparse.ArgumentParser(description="Latvian number-to-words converter")
    parser.add_argument("text", nargs="?", help="Text to convert")
    parser.add_argument("--no-expand-abbr", action="store_true")
    parser.add_argument("--no-roman", action="store_true")
    args = parser.parse_args()

    if args.text:
        text = args.text
    elif not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    else:
        parser.print_help()
        sys.exit(1)

    print(convert(text, expand_abbr=not args.no_expand_abbr, no_roman=args.no_roman))


if __name__ == "__main__":
    main()
