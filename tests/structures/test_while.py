
from ..utils import TranspileTestCase


class WhileLoopTests(TranspileTestCase):
    def test_while(self):
        self.assertCodeExecution("""
            i = 0
            total = 0
            while i < 10:
                i += 1
                total += i
                print(i, total)
            """)

    def test_break(self):
        self.assertCodeExecution("""
            i = 0
            while i < 10:
                i = i + 1
                print(i, i % 5)
                if i % 5 == 0:
                    break
                print("after")
            """)

    def test_continue(self):
        self.assertCodeExecution("""
            i = 0
            while i < 10:
                i = i + 1
                print(i, i % 5)
                if i % 5 == 0:
                    continue
                print("after")
            """)

    def test_nested(self):
        self.assertCodeExecution("""
            i = 1
            j = 10
            while i < j:
                k = 0
                while k < i:
                    print(i, j)
                    k = k + 1
                print("While done")
                i = i + 1
            """)

    def test_while_forever(self):
        self.assertCodeExecution("""
            i = 0
            while 1:
                print("Loop", i)
                i = i + 1
                if i == 10:
                    break
            """)

    def test_while_forever_with_if_not(self):
        self.assertCodeExecution("""
            i = 0
            while 1:
                print("Loop", i)
                i = i + 1
                if not i < 10:
                    break
            """)

    def test_while_not_forever(self):
        self.assertCodeExecution("""
            while not 0:
                print("Loop")
                break
            """)

    def test_while_else(self):
        self.assertCodeExecution("""
            i = 1
            j = 4
            while i < j:
                print(i)
                i = i + 1
            else:
                print("Else")
            """)

    def test_while_else_break(self):
        self.assertCodeExecution("""
            i = 1
            j = 4
            while i < j:
                print(i)
                i = i + 1
                break
            else:
                print("Else")
            """)

    def test_while_forever_inside_try(self):
        self.assertCodeExecution("""
            i = 0
            try:
                while 1:
                    print("Loop", i)
                    i = i + 1
                    if i == 10:
                        break
            finally:
                print("Done")
            """)
