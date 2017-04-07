import unittest

from voc.transpiler import Transpiler
from voc.python.blocks import BlockCodeTooLarge
from voc.python.methods import MethodCodeTooLarge


class LargeCodeTest(unittest.TestCase):

    def test_block_large_code(self):
        "Test exception for large code of an anonymous block."
        large_code = 'print(1 + 2)\n' * 3000
        transpiler = Transpiler(verbosity=0)
        self.assertRaises(BlockCodeTooLarge, transpiler.transpile_string,
                          "test.py", large_code)

    def test_method_large_code(self):
        "Test exception for large code of a method."
        large_code = 'def test():\n' + '    print(1 + 2)\n' * 3000
        transpiler = Transpiler(verbosity=0)
        self.assertRaises(MethodCodeTooLarge, transpiler.transpile_string,
                          "test.py", large_code)
