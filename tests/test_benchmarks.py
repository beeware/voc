import os

from .utils import *

TESTDIR = os.path.dirname(__file__)

class BenchmarkTests(TranspileTestCase):

    def test_binary_trees(self):
        with open(os.path.join(TESTDIR + "/benchmarks/", "binary-trees.py")) as javafile:
            out = self.runAsJava(adjust(javafile.read()), args=["5", "5"], timed=True)

            self.assertIn("stretch tree of depth", out)

    def test_call_simple(self):
        with open(os.path.join(TESTDIR + "/benchmarks/", "call_simple.py")) as javafile:
            out = self.runAsJava(adjust(javafile.read()), args=["2"])

            self.assertIn("Time elapsed: ", out)

    def test_unpack_sequence(self):
        with open(os.path.join(TESTDIR + "/benchmarks/", "unpack_sequence.py")) as javafile:
            out = self.runAsJava(adjust(javafile.read()), args=["10"])
            
            self.assertIn("Time elapsed: ", out)

    def test_pystone(self):
        with open(os.path.join(TESTDIR + "/benchmarks/", "pystone.py")) as javafile:
            out = self.runAsJava(adjust(javafile.read()), args=["10"])

            self.assertIn("Pystone(1.2) time for 10 passes = ", out)
