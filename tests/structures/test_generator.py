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

    def test_simplest_yieldfrom(self):
        self.assertCodeExecution("""
            def gen1():
                yield 1
                yield 2
                yield 3

            def gen2():
                yield from gen1()

            for i in gen2():
                print(i)
        """)

    def test_yieldfrom_list(self):
        self.assertCodeExecution("""
            def gen():
                yield from [1, 2, 3]

            for i in gen():
                print(i)
        """)

    def test_chainning_yieldfrom(self):
        self.assertCodeExecution("""
            def gen1():
                yield 'a'
                yield 'b'

            def gen2():
                yield from gen1()
                yield 'gen2'

            def gen3():
                yield from gen2()

            for i in gen3():
                print(i)
        """)

    def test_yield_from_used(self):
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

    def test_generator_yield_expr_call(self):
        self.assertCodeExecution("""
            def gen():
                while True:
                    x = print((yield))

            g = gen()
            g.send(None)
            g.send("Hello World")
            """)

    def test_generator_yield_expr_unary_op(self):
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

    def test_generator_yield_expr_bool_op(self):
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

    def test_generator_yield_expr_binary_op(self):
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

    def test_generator_yield_expr_aug_assign(self):
        self.assertCodeExecution("""
            def gen():
                while True:
                    x = 2
                    x += (yield)
                    yield x

            g = gen()
            g.send(None)
            g.send(1)
            g.send(2)
            """)

    def test_generator_yield_expr_compare(self):
        self.assertCodeExecution("""
            def gen():
                while True:
                    x = 1 <= (yield) < 5
                    yield x

            g = gen()
            g.send(None)
            g.send(1)
            g.send(100)
            """)

    def test_generator_yield_expr_if(self):
        self.assertCodeExecution("""
            def gen():
                if (yield):
                    print("Hello world")

            g = gen()
            g.send(None)
            try:
                g.send(1)
            except StopIteration:
                pass
            """)

    @expectedFailure
    def test_generator_yield_expr_return(self):
        self.assertCodeExecution("""
            def gen():
                return (yield)

            g = gen()
            g.send(None)
            g.send(1)  # for some reason the generator keeps returning value
            g.send(100) # without raising StopIteration error
            """)
