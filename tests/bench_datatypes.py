import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from utils import *

def test_small_integers(test_case):
    test_case.runAndBenchAsJava("test_small_integers", """
        for i in range(10000):
            x = -5
            for i in range(-5, 257):
                x = x + 1
        """)

def test_booleans(test_case):
    test_case.runAndBenchAsJava("test_booleans", """
        x = True
        y = False
        for i in range(10000):
            x = (not x and y)
            y = x != y
        """)

def main():
    test_case = TranspileTestCase()
    test_case.setUpClass()
    test_small_integers(test_case)
    test_booleans(test_case)

if __name__== "__main__":
  main()
