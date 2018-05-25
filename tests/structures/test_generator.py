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

    def test_chaining_yieldfrom(self):
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
