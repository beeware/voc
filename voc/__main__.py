import sys
from .transpiler import transpile


def main():
    if len(sys.argv) != 3:
        print("Usage: voc <path to .py file> <namespace>")
        print()
        print('  e.g.: voc tests/example.py org.pybee')
        sys.exit(1)

    transpile(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
