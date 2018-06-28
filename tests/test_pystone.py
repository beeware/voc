import os

from .utils import *

__file__ = "pystone.py"
__thisdir__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = os.path.join(__thisdir__, "tests/", __file__)

class PystoneTest(TranspileTestCase):

    def test_pystone(self):
        file = open(__location__, "r")

        out = self.runAsJava(adjust(file.read()))
        print(out)

        file.close()
