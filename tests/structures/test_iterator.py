from ..utils import TranspileTestCase


class IteratorTests(TranspileTestCase):
    def test_iterable(self):
        self.assertCodeExecution("""
            class TestSet:
                def __init__(self, values):
                    self.values = values
                    self.i = -1

                def __iter__(self):
                    return self

                def __next__(self):
                    try:
                        self.i += 1
                        if self.values[self.i] % 2 == 0:
                            return 'even'
                        else:
                            return self.values[self.i]
                    except IndexError:
                        raise StopIteration()

            s = TestSet([1, 2, 3, 4, 5])
            for val in s:
                print(val)

            """)

    def test_generator_as_iterable(self):
        self.assertCodeExecution("""
            class Interview:
                def __init__(self, start, stop):
                    self.start = start
                    self.stop = stop

                def __iter__(self):
                    for i in range(self.start, self.stop):
                        found = False
                        if i % 2 == 0:
                            yield 'fizz'
                            found = True
                        if i % 3 == 0:
                            yield 'buzz'
                            found = True
                        if not found:
                            yield i

            myinterview = Interview(1, 20)

            for i in myinterview:
                print(i)
            """)
