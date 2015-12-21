import sys
from .transpiler import transpile


def main():
    if len(sys.argv) == 2:
        srcdir = '.'
        outdir = None
    elif len(sys.argv) == 3:
        srcdir = sys.argv[2]
        outdir = None
    elif len(sys.argv) == 4:
        srcdir = sys.argv[2]
        outdir = sys.argv[3]
    else:
        print("Usage: voc <path to .py file> [<input prefix>] [<output dir>]")
        print()
        print('  e.g.: voc tests/example.py src out')
        sys.exit(1)

    transpile(sys.argv[1], srcdir=srcdir, outdir=outdir)


if __name__ == "__main__":
    main()
