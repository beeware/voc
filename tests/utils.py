import contextlib
from io import StringIO, BytesIO
import os
import re
import shutil
import subprocess
import sys
import traceback
from unittest import TestCase

from voc.python.blocks import Block as PyBlock
from voc.python.modules import Module as PyModule
from voc.java.constants import ConstantPool, Utf8
from voc.java.klass import ClassFileReader, ClassFileWriter
from voc.java.attributes import Code as JavaCode
from voc.transpiler import Transpiler


@contextlib.contextmanager
def capture_output(redirect_stderr=True):
    oldout, olderr = sys.stdout, sys.stderr
    try:
        out = StringIO()
        sys.stdout = out
        if redirect_stderr:
            sys.stderr = out
        else:
            sys.stderr = StringIO()
        yield out
    except:
        if redirect_stderr:
            traceback.print_exc()
        else:
            raise
    finally:
        sys.stdout, sys.stderr = oldout, olderr


def adjust(text):
    """Adjust a code sample to remove leading whitespace."""
    lines = text.split('\n')
    if len(lines) == 1:
        return text

    if lines[0].strip() == '':
        lines = lines[1:]
    first_line = lines[0].lstrip()
    n_spaces = len(lines[0]) - len(first_line)

    return '\n'.join(line[n_spaces:] for line in lines)


def runAsPython(test_dir, main_code, extra_code=None):
    """Run a block of Python code with the Python interpreter."""
    # Output source code into test directory
    with open(os.path.join(test_dir, 'test.py'), 'w') as py_source:
        py_source.write(adjust(main_code))

    if extra_code:
        for name, code in extra_code.items():
            path = name.split('.')
            path[-1] = path[-1] + '.py'
            if len(path) != 1:
                try:
                    os.makedirs(os.path.join(test_dir, *path[:-1]))
                except FileExistsError:
                    pass
            with open(os.path.join(test_dir, *path), 'w') as py_source:
                py_source.write(adjust(code))

    proc = subprocess.Popen(
        ["python", "test.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=test_dir,
    )
    out = proc.communicate()

    return out[0].decode('utf8')


def runAsJava(test_dir, main_code, extra_code=None):
    """Run a block of Python code as a Java program."""
    # Output source code into test directory
    transpiler = Transpiler()

    # Don't redirect stderr; we want to see any errors from the transpiler
    # as top level test failures.
    with capture_output(redirect_stderr=False):
        transpiler.transpile_string("test.py", adjust(main_code))

        if extra_code:
            for name, code in extra_code.items():
                transpiler.transpile_string("%s.py" % name, adjust(code))

    transpiler.write(test_dir, verbosity=0)

    proc = subprocess.Popen(
        ["java", "-classpath", "../../python.jar:.", "-XX:-UseSplitVerifier", "python.test"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=test_dir,
    )
    out = proc.communicate()

    return out[0].decode('utf8')


JAVA_EXCEPTION = re.compile('^Exception in thread "main" ([^\n]+\nCaused by: )?org\.python\.exceptions\.([\w]+): ([^\n]+)\n([^\n]+\n)+', re.MULTILINE)
JAVA_FLOAT = re.compile('(\d+)E(-)?(\d+)')

PYTHON_EXCEPTION = re.compile('^Traceback \(most recent call last\):\n(  .*\n)+(.*): (.*)\n', re.MULTILINE)
PYTHON_FLOAT = re.compile('(\d+)e(-)?0?(\d+)')


def cleanse_java(input):
    out = JAVA_EXCEPTION.sub('### EXCEPTION ###\n\\2: \\3\n', input)
    return JAVA_FLOAT.sub('\\1e\\2\\3', out)


def cleanse_python(input):
    out = PYTHON_EXCEPTION.sub('### EXCEPTION ###\n\\2: \\3\n', input)
    return PYTHON_FLOAT.sub('\\1e\\2\\3', out)


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

    def assertCodeExecution(self, code, message=None, extra_code=None):
        "Run code as native python, and under Java and check the output is identical"
        self.maxDiff = None
        try:
            # Create the temp directory into which code will be placed
            test_dir = os.path.join(os.path.dirname(__file__), 'temp')
            try:
                os.mkdir(test_dir)
            except FileExistsError:
                pass

            # Run the code as Python and as Java.
            py_out = runAsPython(test_dir, code, extra_code)
            java_out = runAsJava(test_dir, code, extra_code)
        except Exception as e:
            self.fail(e)
        finally:
            # Clean up the test directory where the class file was written.
            shutil.rmtree(test_dir)

        # Cleanse the Python and Java output, producing a simple
        # normalized format for exceptions, floats etc.
        java_out = cleanse_java(java_out)
        py_out = cleanse_python(py_out)

        # Confirm that the output of the Java code is the same as the Python code.
        self.assertEqual(java_out, py_out, message)


def _unary_test(test_name, operation):
    def func(self):
        for value in self.values:
            self.assertUnaryOperation(x=value, operation=operation, format=self.format)
    return func


class UnaryOperationTestCase:
    format = ''

    def run(self, result=None):
        # Override the run method to inject the "expectingFailure" marker
        # when the test case runs.
        for test_name in dir(self):
            if test_name.startswith('test_'):
                getattr(self, test_name).__dict__['__unittest_expecting_failure__'] = test_name in self.not_implemented
        return super().run(result=result)

    def assertUnaryOperator(self, **kwargs):
        self.assertCodeExecution("""
            x = %(x)s
            print(%(format)s%(operand)sx)
            """ % kwargs)

    test_unary_positive = _unary_test('test_unary_positive', '+')
    test_unary_negative = _unary_test('test_unary_negative', '-')
    test_unary_not = _unary_test('test_unary_not', 'not ')
    test_unary_invert = _unary_test('test_unary_invert', '~')


SAMPLE_DATA = [
    ('bool', ['True', 'False']),
    # ('bytearray', [3]),
    ('bytes', ["b''", "b'This is another string of bytes'"]),
    # ('class', ['']),
    # ('complex', ['']),
    ('dict', ["{}", "{'a': 1, 'c': 2.3456, 'd': 'another'}"]),
    ('float', ['2.3456', '0.0', '-3.14159']),
    # ('frozenset', ),
    ('int', ['3', '0', '-5']),
    ('list', ["[]", "[3, 4, 5]"]),
    ('set', ["set()", "{1, 2.3456, 'another'}"]),
    ('str', ['""', '"This is another string"']),
    ('tuple', ["(1, 2.3456, 'another')"]),
]


def _binary_test(test_name, operation, examples):
    def func(self):
        for value in self.values:
            for example in examples:
                self.assertBinaryOperation(x=value, y=example, operation=operation, format=self.format)
    return func


class BinaryOperationTestCase:
    format = ''
    y = 3

    def run(self, result=None):
        # Override the run method to inject the "expectingFailure" marker
        # when the test case runs.
        for test_name in dir(self):
            if test_name.startswith('test_'):
                getattr(self, test_name).__dict__['__unittest_expecting_failure__'] = test_name in self.not_implemented
        return super().run(result=result)

    def assertBinaryOperation(self, **kwargs):
        self.assertCodeExecution("""
            x = %(x)s
            y = %(y)s
            print(%(format)s%(operation)s)
            """ % kwargs, "Error running %(operation)s with x=%(x)s and y=%(y)s" % kwargs)

    for datatype, examples in SAMPLE_DATA:
        vars()['test_add_%s' % datatype] = _binary_test('test_add_%s' % datatype, 'x + y', examples)
        vars()['test_subtract_%s' % datatype] = _binary_test('test_subtract_%s' % datatype, 'x - y', examples)
        vars()['test_multiply_%s' % datatype] = _binary_test('test_multiply_%s' % datatype, 'x * y', examples)
        vars()['test_floor_divide_%s' % datatype] = _binary_test('test_floor_divide_%s' % datatype, 'x // y', examples)
        vars()['test_true_divide_%s' % datatype] = _binary_test('test_true_divide_%s' % datatype, 'x / y', examples)
        vars()['test_modulo_%s' % datatype] = _binary_test('test_modulo_%s' % datatype, 'x % y', examples)
        vars()['test_power_%s' % datatype] = _binary_test('test_power_%s' % datatype, 'x ** y', examples)
        vars()['test_subscr_%s' % datatype] = _binary_test('test_subscr_%s' % datatype, 'x[y]', examples)
        vars()['test_lshift_%s' % datatype] = _binary_test('test_lshift_%s' % datatype, 'x << y', examples)
        vars()['test_rshift_%s' % datatype] = _binary_test('test_rshift_%s' % datatype, 'x >> y', examples)
        vars()['test_and_%s' % datatype] = _binary_test('test_and_%s' % datatype, 'x & y', examples)
        vars()['test_xor_%s' % datatype] = _binary_test('test_xor_%s' % datatype, 'x ^ y', examples)
        vars()['test_or_%s' % datatype] = _binary_test('test_or_%s' % datatype, 'x | y', examples)


def _inplace_test(test_name, operation, examples):
    def func(self):
        for value in self.values:
            for example in self.examples:
                self.assertInplaceOperation(x=value, y=example, operation=operation, format=self.format)
    return func


class InplaceOperationTestCase:
    format = ''
    y = 3

    def run(self, result=None):
        # Override the run method to inject the "expectingFailure" marker
        # when the test case runs.
        for test_name in dir(self):
            if test_name.startswith('test_'):
                getattr(self, test_name).__dict__['__unittest_expecting_failure__'] = test_name in self.not_implemented
        return super().run(result=result)

    def assertInplaceOperation(self, **kwargs):
        self.assertCodeExecution("""
            x = %(x)s
            y = %(y)s
            %(operation)s
            print(%(format)sx)
            """ % kwargs, "Error running %(operation)s with x=%(x)s and y=%(y)s" % kwargs)

    for datatype, examples in SAMPLE_DATA:
        vars()['test_add_%s' % datatype] = _inplace_test('test_add_%s' % datatype, 'x += y', examples)
        vars()['test_subtract_%s' % datatype] = _inplace_test('test_subtract_%s' % datatype, 'x -= y', examples)
        vars()['test_multiply_%s' % datatype] = _inplace_test('test_multiply_%s' % datatype, 'x *= y', examples)
        vars()['test_floor_divide_%s' % datatype] = _inplace_test('test_floor_divide_%s' % datatype, 'x //= y', examples)
        vars()['test_true_divide_%s' % datatype] = _inplace_test('test_true_divide_%s' % datatype, 'x /= y', examples)
        vars()['test_modulo_%s' % datatype] = _inplace_test('test_modulo_%s' % datatype, 'x %= y', examples)
        vars()['test_power_%s' % datatype] = _inplace_test('test_power_%s' % datatype, 'x **= y', examples)
        vars()['test_lshift_%s' % datatype] = _inplace_test('test_lshift_%s' % datatype, 'x <<= y', examples)
        vars()['test_rshift_%s' % datatype] = _inplace_test('test_rshift_%s' % datatype, 'x >>= y', examples)
        vars()['test_and_%s' % datatype] = _inplace_test('test_and_%s' % datatype, 'x &= y', examples)
        vars()['test_xor_%s' % datatype] = _inplace_test('test_xor_%s' % datatype, 'x ^= y', examples)
        vars()['test_or_%s' % datatype] = _inplace_test('test_or_%s' % datatype, 'x |= y', examples)
