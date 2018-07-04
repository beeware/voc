import os

from .utils import *

TESTDIR = os.path.dirname(__file__)

class PystoneTest(TranspileTestCase):

    def test_pystone(self):
        with open(os.path.join(TESTDIR, "pystone.py")) as javafile:
            out = self.runAsJava(adjust(javafile.read()), args=["10"])

            self.assertEqual(out, 'something...')
