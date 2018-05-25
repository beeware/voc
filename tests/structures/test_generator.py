from unittest import expectedFailure

from ..utils import TranspileTestCase


class GeneratorTests(TranspileTestCase):
    def test_simple_generator(self):
        self.assertCodeExecution("""
            def multiplier(first, second):
                y = first * second
                yield y
                y *= second
                yield y
                y *= second
                yield y
                y *= second
                yield y

            print(list(multiplier(1, 20)))
            """)

    def test_loop_generator(self):
        self.assertCodeExecution("""
            def fizz_buzz(start, stop):
                for i in range(start, stop):
                    found = False
                    if i % 2 == 0:
                        yield 'fizz'
                        found = True
                    if i % 3 == 0:
                        yield 'buzz'
                        found = True
                    if not found:
                        yield i

            print(list(fizz_buzz(1, 20)))
            """)

    def test_simplest_generator(self):
        self.assertCodeExecution("""
            def somegen():
                yield 1
                yield 2
                yield 3

            for i in somegen():
                print(i)
            """)

    def test_generator_method(self):
        self.assertCodeExecution("""
            class Interview:
                def __init__(self, start, stop):
                    self.start = start
                    self.stop = stop

                def fizz_buzz(self):
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

            for i in myinterview.fizz_buzz():
                print(i)
            """)

    def test_yield_from_not_used(self):
        """Yield from is currently not implemented.
        Unused yield from statements must not break
        the program compilation, but only ensue a warning."""
        self.assertCodeExecution("""

            def unused():
                yield from range(5)

            print('Hello, world!')
            """)

    @expectedFailure
    def test_yield_from_used(self):
        """Yield from is currently not implemented.
        Yield from statements become NotImplementedErrors at runtime."""
        self.assertCodeExecution("""

            def using_yieldfrom():
                yield from range(5)

            for i in using_yieldfrom():
                print(i)
            """)

    def test_generator_send(self):
        self.assertCodeExecution("""
            def gen():
                a = yield
                print(a)

            g = gen()
            next(g)
            try:
                g.send("Hello World")
            except StopIteration:
                pass
            """)

    def test_generator_multi_send(self):
        self.assertCodeExecution("""
            def gen():
                a = yield 1
                print(a)
                b = yield 2
                print(b)

            g = gen()
            next(g)
            try:
                print(g.send("a"))
                print(g.send("b"))
            except StopIteration:
                pass
            """)

    def test_generator_power_generator(self):
        self.assertCodeExecution("""
            def gen():
                while True:
                    x = yield 1
                    yield x ** 2

            g = gen()
            next(g)
            print(g.send(6))
            next(g)
            print(g.send(-1))
            """)

    def test_generator_send_loop(self):
        self.assertCodeExecution("""
            def gen():
                for i in range(1, 5):
                    a = yield i
                    print("printing from generator " + str(a))

            g = gen()
            g.send(None)
            try:
                while True:
                    b = g.send(1)
                    print("printing from user " + str(b))
            except StopIteration:
                pass
            """)

    def test_generator_yield_call(self):
        self.assertCodeExecution("""
            def gen():
                while True:
                    x = print((yield))

            g = gen()
            g.send(None)
            g.send("Hello World")
            """)

    def test_generator_unary_op(self):
        self.assertCodeExecution("""
            def gen():
                while True:
                    x = -(yield)
                    yield x

            g = gen()
            g.send(None)
            g.send(2)
            g.send(-1)
            """)

    def test_generator_bool_op(self):
        self.assertCodeExecution("""
            def gen():
                while True:
                    x = not (yield)
                    yield x

            g = gen()
            g.send(None)
            g.send(True)
            g.send(False)
            """)

    def test_generator_binary_op(self):
        self.assertCodeExecution("""
            def gen():
                while True:
                    x = 2 + (yield)
                    yield x

            def gen2():
                while True:
                    x = (yield) * 2
                    yield x

            def gen3():
                while True:
                    x = (yield) ** 2
                    yield x

            g = gen()
            g.send(None)
            g.send(2)
            g.send(-1)

            g = gen2()
            g.send(None)
            g.send(100)
            g.send(20)

            g = gen3()
            next(g)
            g.send(2)
            g.send(0)
            """)
