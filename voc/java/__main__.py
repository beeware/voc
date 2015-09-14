import sys

from .klass import Class


def dump(filename):
    with open(filename, 'rb') as infile:
        Class.read(infile, debug=sys.stdout)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: voc.java <path to .class file>")
        print()
        print('  e.g.: voc.java org/pybee/example.class')
        sys.exit(1)

    dump(sys.argv[1])
