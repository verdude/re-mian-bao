from brittle.scanner import Scanner
import argparse
import sys


def parse_options():
    parser = argparse.ArgumentParser(description="Send Text", add_help=True)

    parser.add_argument("-d", "--debug", action="store_true", help="set logging to debug")
    parser.add_argument("-q", "--quiet", action="store_true", help="set logging to quiet")
    return parser.parse_args()

def get_filename():
    if len(sys.argv) <= 1:
        print("Missing filename")
        sys.exit(1)

    return sys.argv[1]

def main(filename):
    scanner = Scanner(filename)
    tokens = scanner.scan()

if __name__ == "__main__":
    filename = get_filename()
    #options = parse_options()
    main(filename)
