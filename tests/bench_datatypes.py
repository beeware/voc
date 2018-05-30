import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from utils import *

def test_small_integers(test_case):
    print("Running", "test_small_integers")
    test_case.runAsJava(adjust("""
        for i in range(10000):
            x = -5
            for i in range(-5, 257):
                x = x + 1
        """), timed=True)

def test_booleans(test_case):
    print("Running", "test_booleans")
    test_case.runAsJava(adjust("""
        x = True
        y = False
        for i in range(10000):
            x = (not x and y)
            y = x != y
        """), timed=True)

def main():
    test_case = TranspileTestCase()
    test_case.setUpClass()
    test_small_integers(test_case)
    test_booleans(test_case)

if __name__== "__main__":
  main()
