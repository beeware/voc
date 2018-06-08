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

    def test_generator_send(self):
        self.assertCodeExecution("""
            def gen():
                a = yield
                print(a)

            g = gen()
            next(g)
            try:
                g.send("Hello World")
                print("can't reach here")
            except StopIteration:
                print("StopIteration")
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
                print("can't reach here")
            except StopIteration:
                print("StopIteration")
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
                    print("can't reach here")
            except StopIteration:
                print("StopIteration")
            """)

    def test_generator_send_after_yield_stmt(self):
        self.assertCodeExecution("""
            def gen():
                yield "regular yield statement"
                a = yield "yield expression"
                print(a)

            g = gen()
            print(next(g))
            print(g.send("Hello World"))
            try:
                print(next(g))  # a is None
                print("can't reach here")
            except StopIteration:
                print("StopIteration")
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
                print("can't reach here")
            except StopIteration:
                print("StopIteration")
            """)

    def test_generator_yield_expr_return(self):
        self.assertCodeExecution("""
            def gen():
                return (yield)

            g = gen()
            g.send(None)
            try:
                g.send(1)
                print("can't reach here")
            except StopIteration:
                print("StopIteration")
            """)

    @expectedFailure
    def test_generator_yield_try_finally_special_case(self):
        """Output is 'finally' followed by 'Hello World'
        due to the way CPython handles garbage collection."""
        self.assertCodeExecution("""
            def gen():
                try:
                    yield 'Hello World'
                finally:
                    print('finally')

            print(next(gen()))
            """)

    def test_generator_throw_on_starting(self):
        self.assertCodeExecution("""
            def gen():
                yield "Hello World"

            g = gen()
            try:
                g.throw(ZeroDivisionError)
                print("can't reach here")
            except ZeroDivisionError:
                print("ZeroDivisionError")
            """)

    def test_generator_throw_other_exception(self):
        self.assertCodeExecution("""
            def gen():
                try:
                    yield
                    print("Hello World")
                except ZeroDivisionError:
                    raise TypeError

            g = gen()
            next(g)
            try:
                g.throw(ZeroDivisionError)
                print("can't reach here")
            except TypeError:
                print("TypeError")
            """)

    def test_generator_throw_exception_handling(self):
        self.assertCodeExecution("""
            def gen():
                try:
                    yield "from try block"
                except TypeError:
                    yield "from catch block"

                yield "from outside try-except"
                a = yield

            g = gen()
            print(next(g))
            print(g.throw(TypeError))
            print(next(g))
            print(g.send("message"))
            """)

    def test_generator_throw_on_close(self):
        self.assertCodeExecution("""
            def gen():
                yield "Hello World"

            g = gen()
            g.close()
            try:
                g.throw(ZeroDivisionError)
                print("can't reach here")
            except ZeroDivisionError:
                print("ZeroDivisionError")
            """)

    def test_generator_next_after_throw(self):
        self.assertCodeExecution("""
            def gen():
                yield 1
                yield 2

            g = gen()
            print(next(g))
            try:
                g.throw(TypeError)
                print("can't reach here")
            except TypeError:
                try:
                    print(next(g))
                    print("can't reach here")
                except StopIteration:
                    print("StopIteration")
            """)

    def test_generator_throw_args(self):
        self.assertCodeExecution("""
            def gen():
                yield 1

            g = gen()
            try:
                g.throw(TypeError, "Hello World")
                print("can't reach here")
            except TypeError as e:
                print(e.__str__())

            g = gen()
            try:
                g.throw(ZeroDivisionError, 100)
                print("can't reach here")
            except ZeroDivisionError as e:
                print(e.__str__())

            g = gen()
            try:
                g.throw(TypeError, (1, 2, 3, "Hello", "World"))
                print("can't reach here")
            except TypeError as e:
                print(e.args)
            """)

    @expectedFailure
    def test_generator_throw_kwargs(self):
        self.assertCodeExecution("""
            def gen():
                yield 1
            g = gen()
            try:
                g.throw(TypeError, {"Hello": 1, "World": 2})
                print("can't reach here")
            except TypeError as e:
                print(e.args)
            """)

    def test_generator_close(self):
        self.assertCodeExecution("""
            def gen():
                print("Hello world")
                try:
                    yield
                except TypeError:
                    pass
                except ZeroDivisionError:
                    pass

            g = gen()
            print(g.close())
            try:
                print(next(g))
                print("can't reach here")
            except StopIteration:
                print("StopIteration")
            """)

    def test_generator_close_ignore_exit(self):
        self.assertCodeExecution("""
            def gen():
                try:
                    yield
                except TypeError:
                    pass
                except GeneratorExit:
                    yield "exit ignored"

            g = gen()
            next(g)
            try:
                g.close()
                print("can't reach here")
            except RuntimeError:
                print(RuntimeError)
            """)

    def test_generator_close_exception_propagation(self):
        self.assertCodeExecution("""
            def gen():
                try:
                    yield
                except GeneratorExit:
                    raise OSError

            g = gen()
            next(g)
            try:
                g.close()
            except OSError:
                pass
            """)

    def test_generator_close_twice(self):
        self.assertCodeExecution("""
            def gen():
                yield 1
                yield 2

            g = gen()
            print(g.close())
            print(g.close())
            """)

    def test_generator_yield_try_suite(self):
        self.assertCodeExecution("""
            def gen():
                try:
                    yield "from try block"
                except:
                    yield "from except block"
                else:
                    yield "from else block"
                finally:
                    yield "from finally block"

            g = gen()
            print(next(g))
            print(g.throw(TypeError))
            print(next(g))

            g = gen()
            print(next(g))
            print(next(g))
            print(next(g))
            try:
                print(next(g))
                print("can't reach here")
            except StopIteration:
                print("StopIteration")
            """)

    def test_generator_yield_expr_try_suite(self):
        self.assertCodeExecution("""
            def gen():
                try:
                    yield "from try block"
                    a = yield
                except:
                    yield "from except block"
                    a = yield
                else:
                    a = yield "from else block"
                finally:
                    a = yield "from finally block"
                print(a)

            g = gen()
            print(next(g))
            print(g.throw(TypeError))
            print(next(g))
            print(g.send("except"))
            try:
                print(g.send("finally"))
                print("can't reach here")
            except StopIteration:
                print("StopIteration")

            g = gen()
            print(next(g))
            print(next(g))
            print(g.send("try"))
            try:
                print(g.send("finally"))
                print("can't reach here")
            except StopIteration:
                print("StopIteration")
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

    def test_generator_yieldfrom_generator_exit(self):
        self.assertCodeExecution("""
            def gen1():
                return [1, 2, 3]

            def gen2():
                v = yield from gen1()
                yield 1

            g = gen2()
            print(next(g))
            try:
                print(g.throw(GeneratorExit))
            except GeneratorExit:
                try:
                    print(next(g))
                except StopIteration:
                    print("StopIteration")
            """)

    def test_generator_yieldfrom_throw_propagation(self):
        self.assertCodeExecution("""
            def gen1():
                try:
                    yield 1
                except TypeError:
                    yield "TypeError"

            def gen2():
                yield from gen1()

            g = gen2()
            print(next(g))
            print(g.throw(TypeError))
            """)

    def test_generator_yieldfrom_send_propagation(self):
        self.assertCodeExecution("""
            def gen1():
                a = yield "gen1"
                print("value received: " + a)

            def gen2():
                yield from gen1()

            g = gen2()
            print(next(g))
            try:
                print(g.send("Hello World"))
            except StopIteration:
                print("StopIteration")
            """)

    def test_generator_stop_iteration_value(self):
        self.assertCodeExecution("""
            def gen():
                yield "Hello World"
                return "return value"

            g = gen()
            print(next(g))
            try:
                print(next(g))
            except StopIteration as e:
                print(e.value)

            def gen1():
                yield "Hello World"
                return "return value"

            def gen2():
                v = yield from gen1()
                print(v)

            g = gen2()
            print(next(g))
            try:
                print(next(g))
            except StopIteration:
                print("StopIteration")
            """)
