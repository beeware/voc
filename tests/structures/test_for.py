from unittest import expectedFailure

from ..utils import TranspileTestCase


class ForLoopTests(TranspileTestCase):
    def test_for_over_range(self):
        # Normal range
        self.assertCodeExecution("""
            total = 0
            for i in range(0, 5):
                total = total + i
                print(i, total)
            """)

        # Empty range
        self.assertCodeExecution("""
            total = 0
            for i in range(0, 0):
                total = total + i
                print(i, total)
            """)

        # Stepped range
        self.assertCodeExecution("""
            total = 0
            for i in range(0, 10, 2):
                total = total + i
                print(i, total)
            """)

        # Reverse range
        self.assertCodeExecution("""
            total = 0
            for i in range(5, 0, -1):
                total = total + i
                print(i, total)
            """)

    def test_for_over_iterable(self):
        self.assertCodeExecution("""
            total = 0
            for i in [1, 2, 3, 5]:
                total = total + i
                print(i, total)
            """)

        self.assertCodeExecution("""
            total = 0
            for i in []:
                total = total + i
                print(i, total)
            """)

    def test_for_else(self):
        self.assertCodeExecution("""
            total = 0
            for i in []:
                total = total + i
            else:
                total = -999
            print(total)
            """)

    def test_for_else_break(self):
        self.assertCodeExecution("""
            total = 0
            for i in []:
                total = total + i
                break
            else:
                total = -999
            print(total)
            """)

    def test_break(self):
        self.assertCodeExecution("""
            for i in range(1, 10):
                print(i, i % 5)
                if i % 5 == 0:
                    break
                print("after")
            """)

    def test_continue(self):
        self.assertCodeExecution("""
            for i in range(1, 10):
                print(i, i % 5)
                if i % 5 == 0:
                    continue
                print("after")
            """)

    def test_nested(self):
        self.assertCodeExecution("""
            i = 1
            j = 10
            for i in range(1, 10):
                for k in range(0, i):
                    print(i, j)
            """)

    def test_multiple_values(self):
        self.assertCodeExecution("""
            values = [
                (1, 2, 3),
                (4, 5, 6),
                (7, 8, 9),
            ]
            for x, y, z, in values:
                print(x, y, z)
            """)

    def test_multiple_values_iterator(self):
        self.assertCodeExecution("""
            values = {
                'a': 1,
                'b': 2,
                'c': 3,
            }
            for k, v in sorted(values.items()):
                print(k, v)
            print('And once again...')
            for item in sorted(values.items()):
                print(item[0], item[1])
            """)

    def test_recursive(self):
        self.assertCodeExecution("""
            def process(data):
                print('process: ', data)
                for datum in data:
                    process(datum)
                print('data processed: ', data)

            data = [[], [[], [], []], [[]]]

            process(data)
            """, run_in_function=False)

    # FIXME: this is the same as the previous test, but the in-function
    # version fails because recursive functions defined *in* a function
    # don't work. Once they *do* work, the previous test can be used
    # without the run_in_function=False qualifier, and this test can be
    # deleted.
    @expectedFailure
    def test_recursive_in_function(self):
        self.assertCodeExecution("""
            def process(data):
                print('process: ', data)
                for datum in data:
                    process(datum)
                print('data processed: ', data)

            data = [[], [[], [], []], [[]]]

            process(data)
            """)
