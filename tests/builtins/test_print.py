from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class PrintTests(TranspileTestCase):
    def test_fileobj(self):
        self.assertCodeExecution("""
            class FileLikeObject:
                def __init__(self):
                    self.buffer = ''

                def write(self, content):
                    self.buffer = self.buffer + (content * 2)

            out = FileLikeObject()

            print('hello', 'world', file=out)
            print('goodbye', 'world', file=out)
            print()
            """)

    def test_sep(self):
        self.assertCodeExecution("""
            print('hello world', 'goodbye world', sep='-')
            print()
            """)

    def test_end(self):
        self.assertCodeExecution("""
            print('hello world', 'goodbye world', end='-')
            print()
            """)

    def test_flush(self):
        self.assertCodeExecution("""
            print('hello world', 'goodbye world', flush=True)
            print()
            """)

    def test_combined(self):
        self.assertCodeExecution("""
            class FileLikeObject:
                def __init__(self):
                    self.buffer = ''

                def write(self, content):
                    self.buffer = self.buffer + (content * 2)

                def flush(self):
                    self.buffer = self.buffer + '<<<'

            out = FileLikeObject()

            print('hello', 'world', sep='*', end='-', file=out, flush=True)
            print('goodbye', 'world', file=out, sep='-', end='*')
            print()
            """)


class BuiltinPrintFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["print"]

    not_implemented = [
        'test_class',
    ]
