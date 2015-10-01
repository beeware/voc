import sys
from .transpiler import transpile


def main():
    if len(sys.argv) not in (2, 3):
        print("Usage: voc <path to .py file> [<output dir>]")
        print()
        print('  e.g.: voc tests/example.py out')
        sys.exit(1)

    if len(sys.argv) == 2:
        outdir = None
    else:
        outdir = sys.argv[2]

    transpile(sys.argv[1], outdir=outdir)

if __name__ == "__main__":
    main()
