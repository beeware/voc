import sys
import argparse
import voc

from .klass import Class


def dump(filename):
    with open(filename, 'rb') as infile:
        Class.read(infile, debug=sys.stdout)


def main():
    parser = argparse.ArgumentParser(
        prog='vod',
        description='Debugging tool to decompile class files.'
    )

    parser.add_argument(
        '--version', '-v',
        action='version',
        version='voc %s' % voc.__version__,
    )

    parser.add_argument(
        'file',
    )

    args = parser.parse_args()
    dump(vars(args)['file'])


if __name__ == "__main__":
    main()
