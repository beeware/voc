import contextlib
from io import StringIO, BytesIO
import os
import re
import subprocess
import sys
import traceback
from unittest import TestCase, expectedFailure

from voc.python.blocks import Block as PyBlock
from voc.python.modules import Module as PyModule
from voc.java.constants import ConstantPool, Utf8
from voc.java.klass import ClassFileReader, ClassFileWriter
from voc.java.attributes import Code as JavaCode
from voc.transpiler import Transpiler


@contextlib.contextmanager
def capture_output():
    oldout, olderr = sys.stdout, sys.stderr
    try:
        out = StringIO()
        sys.stdout = out
        sys.stderr = out
        yield out
    except:
        traceback.print_exc()
    finally:
        sys.stdout, sys.stderr = oldout, olderr


def adjust(text):
    """Adjust a code sample to remove leading whitespace."""
    lines = text.split('\n')
    if lines[0].strip() == '':
        lines = lines[1:]
    first_line = lines[0].lstrip()
    n_spaces = len(lines[0]) - len(first_line)
    return '\n'.join(line[n_spaces:] for line in lines)


def runAsJava(main_code, **extra):
    """Run a block of Python code as a Java program."""

    transpiler = Transpiler('org.pybee')
    with capture_output():
        transpiler.transpile_string("test.py", main_code)

        for name, code in extra.items():
            transpiler.transpile_string("%s.py" % name, code)

    transpiler.write(os.path.dirname(__file__), verbosity=0)

    proc = subprocess.Popen(
        ["java", "-classpath", "../python.jar:.", "-XX:-UseSplitVerifier", "org.pybee.test"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=os.path.dirname(__file__),
    )
    out = proc.communicate()
    return out[0].decode('utf8')


JAVA_EXCEPTION = re.compile('^Exception in thread "main" ([^\n]+\nCaused by: )?org\.python\.exceptions\.([\w]+): ([^\n]+)\n([^\n]+\n)+', re.MULTILINE)
PYTHON_EXCEPTION = re.compile('^Traceback \(most recent call last\):\n(  .*\n)+(.*): (.*)\n', re.MULTILINE)


def cleanse_java_exceptions(input):
    return JAVA_EXCEPTION.sub('### EXCEPTION ###\n\\2: \\3\n', input)


def cleanse_python_exceptions(input):
    return PYTHON_EXCEPTION.sub('### EXCEPTION ###\n\\2: \\3\n', input)


class TranspileTestCase(TestCase):
    def assertBlock(self, python, java):
        self.maxDiff = None
        dump = False

        py_block = PyBlock(parent=PyModule('test', 'test.py'))
        if python:
            python = adjust(python)
            code = compile(python, '<test>', 'exec')
            py_block.extract(code, debug=dump)

        java_code = py_block.transpile()

        out = BytesIO()
        constant_pool = ConstantPool()
        java_code.resolve(constant_pool)

        constant_pool.add(Utf8('test'))
        constant_pool.add(Utf8('Code'))
        constant_pool.add(Utf8('LineNumberTable'))

        writer = ClassFileWriter(out, constant_pool)
        java_code.write(writer)

        debug = StringIO()
        reader = ClassFileReader(BytesIO(out.getbuffer()), constant_pool, debug=debug)
        JavaCode.read(reader, dump=0)

        if dump:
            print(debug.getvalue())

        java = adjust(java)
        self.assertEqual(debug.getvalue(), java[1:])

    def assertCodeExecution(self, code):
        "Run code as native python, and under Java and check the output is identical"
        self.maxDiff = None
        code = adjust(code)

        java_out = runAsJava(code)

        with capture_output() as py_out:
            exec(code, {'__name__': '__main__'}, {})
        py_out = py_out.getvalue()

        # Cleanse the Python and Java exception output, producing a simple
        # normalized form.
        java_out = cleanse_java_exceptions(java_out)
        py_out = cleanse_python_exceptions(py_out)

        # Confirm that the output of the Java code is the same as the Python code.
        self.assertEqual(java_out, py_out)


class UnaryOperationTestCase:
    format = ''

    def assertUnaryOperator(self, **kwargs):
        self.assertCodeExecution("""
            x = %(x)s
            print(%(format)s%(operand)sx)
            """ % kwargs)

    def test_unary_positive(self):
        self.assertUnaryOperator(x=self.x, operand='+', format=self.format)

    def test_unary_negative(self):
        self.assertUnaryOperator(x=self.x, operand='-', format=self.format)

    def test_unary_not(self):
        self.assertUnaryOperator(x=self.x, operand='-', format=self.format)

    def test_unary_invert(self):
        self.assertUnaryOperator(x=self.x, operand='~', format=self.format)


SAMPLE_DATA = [
    ('bool_true', 'True'),
    ('bool_false', 'False'),
    # ('bytearray', 3),
    ('bytes', "b'This is another string of bytes'"),
    # ('class', ''),
    # ('complex', ''),
    ('dict', "{'a': 1, 'c': 2.3456, 'd': 'another'}"),
    ('float', '2.3456'),
    # ('frozenset', ),
    ('int', '3'),
    ('list', "[3, 4, 5]"),
    ('set', "{1, 2.3456, 'another'}"),
    ('str', '"This is another string"'),
    ('tuple', "(1, 2.3456, 'another')"),
]


class BinaryOperationTestCase:
    format = ''
    y = 3

    def assertBinaryOperation(self, **kwargs):
        self.assertCodeExecution("""
            x = %(x)s
            y = %(y)s
            print(%(format)s%(operation)s)
            """ % kwargs)


def _binary_test(operation, value):
    def func(self):
        self.assertBinaryOperation(x=self.x, y=value, operation=operation, format=self.format)
    return func

for datatype, example in SAMPLE_DATA:
    setattr(BinaryOperationTestCase, 'test_add_%s' % datatype, _binary_test('x + y', example))
    setattr(BinaryOperationTestCase, 'test_subtract_%s' % datatype, _binary_test('x - y', example))
    setattr(BinaryOperationTestCase, 'test_multiply_%s' % datatype, _binary_test('x * y', example))
    setattr(BinaryOperationTestCase, 'test_floor_divide_%s' % datatype, _binary_test('x // y', example))
    setattr(BinaryOperationTestCase, 'test_true_divide_%s' % datatype, _binary_test('x / y', example))
    setattr(BinaryOperationTestCase, 'test_modulo_%s' % datatype, _binary_test('x % y', example))
    setattr(BinaryOperationTestCase, 'test_power_%s' % datatype, _binary_test('x ** y', example))
    setattr(BinaryOperationTestCase, 'test_subscr_%s' % datatype, _binary_test('x[y]', example))
    setattr(BinaryOperationTestCase, 'test_lshift_%s' % datatype, _binary_test('x << y', example))
    setattr(BinaryOperationTestCase, 'test_rshift_%s' % datatype, _binary_test('x >> y', example))
    setattr(BinaryOperationTestCase, 'test_and_%s' % datatype, _binary_test('x & y', example))
    setattr(BinaryOperationTestCase, 'test_xor_%s' % datatype, _binary_test('x ^ y', example))
    setattr(BinaryOperationTestCase, 'test_or_%s' % datatype, _binary_test('x | y', example))


class InplaceOperationTestCase:
    format = ''
    y = 3

    def assertInplaceOperation(self, **kwargs):
        self.assertCodeExecution("""
            x = %(x)s
            y = %(y)s
            %(operation)s
            print(%(format)sx)
            """ % kwargs)


def _inplace_test(operation, value):
    def func(self):
        self.assertInplaceOperation(x=self.x, y=value, operation=operation, format=self.format)
    return func

for datatype, example in SAMPLE_DATA:
    setattr(InplaceOperationTestCase, 'test_add_%s' % datatype, _inplace_test('x += y', example))
    setattr(InplaceOperationTestCase, 'test_subtract_%s' % datatype, _inplace_test('x -= y', example))
    setattr(InplaceOperationTestCase, 'test_multiply_%s' % datatype, _inplace_test('x *= y', example))
    setattr(InplaceOperationTestCase, 'test_floor_divide_%s' % datatype, _inplace_test('x //= y', example))
    setattr(InplaceOperationTestCase, 'test_true_divide_%s' % datatype, _inplace_test('x /= y', example))
    setattr(InplaceOperationTestCase, 'test_modulo_%s' % datatype, _inplace_test('x %= y', example))
    setattr(InplaceOperationTestCase, 'test_power_%s' % datatype, _inplace_test('x **= y', example))
    setattr(InplaceOperationTestCase, 'test_lshift_%s' % datatype, _inplace_test('x <<= y', example))
    setattr(InplaceOperationTestCase, 'test_rshift_%s' % datatype, _inplace_test('x >>= y', example))
    setattr(InplaceOperationTestCase, 'test_and_%s' % datatype, _inplace_test('x &= y', example))
    setattr(InplaceOperationTestCase, 'test_xor_%s' % datatype, _inplace_test('x ^= y', example))
    setattr(InplaceOperationTestCase, 'test_or_%s' % datatype, _inplace_test('x |= y', example))
