import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from utils import *

def test_small_integers(test_case):
    print("Running", "test_small_integers")
    test_case.runAsJava(adjust("""
        for i in range(100):
            for j in range(100):
                x = -5
                for k in range(-5, 257):
                    x = x + 1
        """), timed=True)

def test_booleans(test_case):
    print("Running", "test_booleans")
    test_case.runAsJava(adjust("""
        for i in range(100000):
            x = True
            y = False

            x = (not x and y)
            y = x != y

            x = True and True and True
            y = x or False

            x = not True or (not x) or True
            y = y == y

            x = y != (not x)
            y = False or True or (not y)

            x = (x != x) or (not False)
            y = y and y and (not x)

            x = False or False or False or False
            y = True and True and True and True

            x = 1 != 0
            y = (not (not (not (not (not (not (not x)))))))

            x = ((not y) and y) == ((not (not x)) or y or (not y))
            y = False or False or (not True) or (not True) or (not True)

            x = True and (not False) and True and (not False) and False
            y = (False != False) != False
        """), timed=True)

def test_global_var_load(test_case):
    print("Running", "test_global_var_load")
    test_case.runAsJava(adjust("""
        x = 1
        y = 2

        for i in range(100000):
            print(x)
            print(y)
            print(x+y)
            print(x-y)
            print(x)
            print(y)
            print(x*y)
            print(x/y)
            print(x)
            print(y)
    """), timed=True)

def test_class_var_load(test_case):
    print("Running", "test_class_var_load")
    test_case.runAsJava(adjust("""
        class Animal:
            def __init__(self, name, sound):
                self.name = name
                self.sound = sound

            def speak(self):
                print(self.name)
                print(self.sound)
                print(self.name)
                print(self.sound)
                print(self.name)
                print(self.sound)

        lapo = Animal("Lapo", "Bow Wow")
        for i in range(100000):
            lapo.speak()
            lapo.speak()
            lapo.speak()

    """), timed=True)

def test_function_var_load(test_case):
    print("Running", "test_function_var_load")
    test_case.runAsJava(adjust("""
        def foo():
            x = 1
            y = 2
            print(x)
            print(y)
            print(x+y)
            print(x-y)
            print(x)
            print(y)
            print(x*y)
            print(x/y)
            print(x)
            print(y)

        for i in range(100000):
            foo()
    """), timed=True)

def test_code(test_case):
    print("Running", "test_code")
    test_case.runAsJava(adjust("""
        def main(n):
            def foo(n):
                return n + 1
            def bar(n):
                return n + 1
            def baz(n):
                return n + 1
            def buzz(n):
                return n + 1
            def bizz(n):
                return n + 1
            def bozz(n):
                return n + 1
            def yam(n):
                return n + 1
            def yarn(n):
                return n + 1
            return foo(bar(baz(buzz(bizz(bozz(yam(yarn(n))))))))
        for i in range(100000):
            main(i)
    """), timed=True)

def test_cmp(test_case):
    print("Running", "test_cmp")
    test_case.runAsJava(adjust("""
        x = None
        s = "mary had a little lamb"
        t = "humpty dumpty sat on a wall"

        for i in range(1000):
            for j in range(1000):
                x = s < t
                x = s <= t
                x = s == t
                x = s != t
                x = s > t
                x = s >= t

                x = 3 < 5
                x = 3 <= 5
                x = 3 == 5
                x = 3 != 5
                x = 3 > 5
                x = 3 >= 5

                x = 3 < True
                x = 3.0 <= 5
                x = None == 5
                x = [3] != 5.0
                x = [3] > [5]
                x = [3.0] > [5.0]
    """), timed=True)

def test_loops(test_case):
    print("Running", "test_loops")
    test_case.runAsJava(adjust("""
        for x in range(100):
            for y in range(100):
                for z in range(100):
                    for a in range(100):
                        pass
    """), timed=True)

def test_dict_get(test_case):
    print("Running", "test_dictionary_get")
    test_case.runAsJava(adjust("""
        dict = {1 : 2, "a" : "b"}
        for i in range(1000000):
            dict.get(i)
            dict.get(1)
            dict.get("a")
            dict.get(i)
            dict.get(1)
            dict.get("a")
    """), timed=True)

def test_method(test_case):
    print("Running, test_method")
    test_case.runAsJava(adjust("""
        class MyClass:

            def A(self):
                print("A!")

            def B(self):
                print("B!")

            def C(self):
                print("C!")

        obj = MyClass()

        for i in range(1000000):
            obj.A()
            obj.B()
            obj.C()
    """), timed=True)

def main():
    test_case = TranspileTestCase()
    test_case.setUpClass()
    test_small_integers(test_case)
    test_booleans(test_case)
    test_global_var_load(test_case)
    test_class_var_load(test_case)
    test_function_var_load(test_case)
    test_code(test_case)
    test_loops(test_case)
    test_cmp(test_case)
    test_dict_get(test_case)
    test_method(test_case)

if __name__== "__main__":
  main()
