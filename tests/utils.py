import contextlib
from io import StringIO, BytesIO
import os
import re
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
