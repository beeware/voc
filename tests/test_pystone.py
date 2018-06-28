import os

from .utils import *

FILENAME = "pystone.py"
THISDIR = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
LOCATION = os.path.join(__thisdir__, "tests/", __file__)

class PystoneTest(TranspileTestCase):

    def test_pystone(self):
        file = open(LOCATION, "r")

        out = self.runAsJava(adjust(file.read()))
        print(out)

        file.close()
