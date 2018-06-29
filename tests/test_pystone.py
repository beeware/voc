import os

from .utils import *

FILENAME = "pystone.py"
THISDIR = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(FILENAME)))
LOCATION = os.path.join(THISDIR, "tests/", FILENAME)

class PystoneTest(TranspileTestCase):

    def test_pystone(self):
        file = open(LOCATION, "r")

        out = self.runAsJava(adjust(file.read()))
        print(out)

        file.close()
