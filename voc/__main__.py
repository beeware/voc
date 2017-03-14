import voc
import argparse

from .transpiler import transpile


def main():
    parser = argparse.ArgumentParser(
        prog='voc',
        description='Transpiles Python code to Java class files.'
    )

    parser.add_argument(
        '-o', '--output',
        help='The directory where class files should be output.',
        default='.'
    )
    parser.add_argument(
        '-p', '--prefix',
        help='The prefix to strip from all source file paths.',
        default='.'
    )
    parser.add_argument(
        '-n', '--namespace',
        help='The namespace for the generated Java classfiles.',
        default='python'
    )
    parser.add_argument(
        '-v', '--verbosity',
        action='count',
        default=0
    )
    parser.add_argument(
        '--version',
        action='version',
        version='voc %s' % voc.__version__,
    )
    parser.add_argument(
        'input',
        metavar='source file',
        nargs='+',
        help='The source file or directory to compile'
    )

    args = parser.parse_args()

    transpile(
        input=args.input,
        prefix=args.prefix,
        outdir=args.output,
        namespace=args.namespace,
        verbosity=args.verbosity
    )


if __name__ == '__main__':
    main()
