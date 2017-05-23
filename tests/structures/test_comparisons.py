from ..utils import TranspileTestCase

from unittest import expectedFailure


class ComparisonTests(TranspileTestCase):
    def test_bool(self):
        self.assertCodeExecution("""
            x = 1234
            if x:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = object()
            if x:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = None
            if x:
                print('True')
            else:
                print('False')
            """)

    def test_is(self):
        self.assertCodeExecution("""
            x = 1234
            if x is 1234:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 1234
            if x is 2345:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = None
            if x is None:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 1234
            if x is None:
                print('True')
            else:
                print('False')
            """)

    def test_is_not(self):
        self.assertCodeExecution("""
            x = 1234
            if x is not 2345:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 1234
            if x is not 1234:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 1234
            if x is not None:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = None
            if x is not None:
                print('True')
            else:
                print('False')
            """)

    def test_lt(self):
        self.assertCodeExecution("""
            x = 1
            if x < 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 5
            if x < 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 10
            if x < 5:
                print('True')
            else:
                print('False')
            """)

    def test_le(self):
        self.assertCodeExecution("""
            x = 1
            if x <= 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 5
            if x <= 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 10
            if x <= 5:
                print('True')
            else:
                print('False')
            """)

    def test_gt(self):
        self.assertCodeExecution("""
            x = 10
            if x > 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 5
            if x > 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 1
            if x > 5:
                print('True')
            else:
                print('False')
            """)

    def test_ge(self):
        self.assertCodeExecution("""
            x = 10
            if x >= 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 5
            if x >= 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 1
            if x >= 5:
                print('True')
            else:
                print('False')
            """)

    def test_eq(self):
        self.assertCodeExecution("""
            x = 10
            if x == 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 5
            if x == 5:
                print('True')
            else:
                print('False')
            """)

    def test_ne(self):
        self.assertCodeExecution("""
            x = 5
            if x != 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 10
            if x != 5:
                print('True')
            else:
                print('False')
            """)

    def test_eq_empty_class(self):
        self.assertCodeExecution("""
            class A:
                pass
            x = A()
            y = A()
            # fallback to object identity
            print(x == x)
            print(x == y)
            print(x.__eq__(x))
            print(x.__eq__(y))
            print(y.__eq__(x))
            """)

    def test_ne_empty_class(self):
        self.assertCodeExecution("""
            class A:
                pass
            x = A()
            y = A()
            print(x != x)
            print(x != y)
            print(x.__ne__(x))
            print(x.__ne__(y))
            print(y.__ne__(x))
            """)

    def test_eq_non_bool(self):
        self.assertCodeExecution("""
            class A:
                def __init__(self, num):
                    self.num = num
                def __eq__(self, other):
                    return self.num
            x = A(0)
            y = A(1)
            print(x == x) # 0
            print(x == y) # __eq__() returns 0 => False
            print(y == x) # __eq__() returns 1 => True
            print(x.__eq__(x)) # 0
            print(x.__eq__(y)) # 0
            print(y.__eq__(x)) # 1

            # test evaluation by ==
            if (x == x):
                print('A')
            if (x == y):
                print('B')
            if (y == x):
                print('C')
            """)

    def test_ne_non_bool(self):
        self.assertCodeExecution("""
            class A:
                def __init__(self, num):
                    self.num = num
                def __ne__(self, other):
                    return self.num
            x = A(0)
            y = A(1)
            print(x != x) # 0
            print(x != y) # __eq__() returns 0 => False
            print(y != x) # __eq__() returns 1 => True
            print(x.__ne__(x)) # 0
            print(x.__ne__(y)) # 0
            print(y.__ne__(x)) # 1

            # test evaluation by !=
            if (x != x):
                print('A')
            if (x != y):
                print('B')
            if (y != x):
                print('C')
            """)

    def test_eq_ne_notimplemented(self):
        self.assertCodeExecution("""
            class A:
                def __eq__(self, other):
                    return NotImplemented
                def __ne__(self, other):
                    return NotImplemented
            x = A()

            # == and != are special, should fallback to testing for object equality
            # instead of TypeError
            print(x == x) # True, same object
            print(x != x) # False, same object
            """)

    def test_eq_within_datatypes(self):
        self.assertCodeExecution("""
            class F:
                def __init__(self, v):
                    self.v = v
                def __eq__(self, other):
                    return self.v == other.v + 1
            k = F(5)
            l = F(6)

            print(k == k) # False
            print([k] == [k]) # True as identity tested first before trying __eq__()
            print({'hi': k} == {'hi': k})
            print((k,) == (k,))

            print(k == l) # False as 5 == 6 + 1
            print(l == k) # True as 6 == 5 + 1
            print([l] == [k]) # True
            print({'hi': l} == {'hi': k}) # True
            print((l,) == (k,))
            """)

    def test_eq_reflected_within_datatypes(self):
        self.assertCodeExecution("""
            class F:
                def __init__(self, v):
                    self.v = v
                def __eq__(self, other):
                    return NotImplemented
            class G:
                def __init__(self, v):
                    self.v = v
                def __eq__(self, other):
                    return self.v == other.v + 1
            f = F(5)
            g = G(6)

            print([f] == [g]) # True (reflected)
            print([g] == [f]) # True (not reflected)
            print({'hi': f} == {'hi': g})
            print({'hi': g} == {'hi': f})
            print((f,) == (g,))
            print((g,) == (f,))
            """)

    def test_ne_within_datatypes(self):
        self.assertCodeExecution("""
            class F:
                def __init__(self, v):
                    self.v = v
                def __ne__(self, other):
                    return self.v == other.v + 1
            k = F(5)
            l = F(6)

            print(k != k) # False
            print([k] != [k]) # True as identity tested first before trying __eq__()
            print({'hi': k} != {'hi': k})
            print((k,) != (k,))

            print(k != l) # False as 5 != 6 + 1
            print(l != k) # True as 6 != 5 + 1
            print([l] != [k]) # True
            print({'hi': l} != {'hi': k}) # True
            print((l,) != (k,))
            """)

    def test_ne_reflected_within_datatypes(self):
        self.assertCodeExecution("""
            class F:
                def __init__(self, v):
                    self.v = v
                def __eq__(self, other):
                    return NotImplemented
            class G:
                def __init__(self, v):
                    self.v = v
                def __ne__(self, other):
                    return self.v != other.v + 1
            f = F(5)
            g = G(6)

            print([f] != [g]) # True (reflected)
            print([g] != [f]) # True (not reflected)
            print({'hi': f} != {'hi': g})
            print({'hi': g} != {'hi': f})
            print((f,) != (g,))
            print((g,) != (f,))
            """)

    def test_cmp_notimplemented(self):
        self.assertCodeExecution("""
            class A:
                pass
            x = A()

            # NotImplemented, not NotImplementedError
            print(x.__le__(x))
            print(x.__lt__(x))
            print(x.__ge__(x))
            print(x.__gt__(x))
            """)

    # next few tests from cpython's Lib/test/test_compare.py @ v3.6.0
    def test_comparisons(self):
        self.assertCodeExecution("""
            class Cmp:
                def __init__(self,arg):
                    self.arg = arg
                def __repr__(self):
                    return '<Cmp %s>' % self.arg
                def __eq__(self, other):
                    return self.arg == other
            class Empty:
                def __repr__(self):
                    return '<Empty>'

            set1 = [2, 2.0, 2+0j, Cmp(2.0)]
            set2 = [[1], (3,), None, Empty()]
            candidates = set1 + set2
            for a in candidates:
                for b in candidates:
                    print(a == b)
            """)

    # list object does not have insert() implemented yet
    @expectedFailure
    def test_id_comparisons(self):
        self.assertCodeExecution("""
            class Empty:
                def __repr__(self):
                    return '<Empty>'

            # Ensure default comparison compares id() of args
            L = []
            for i in range(10):
                L.insert(len(L)//2, Empty())
            for a in L:
                for b in L:
                    print(a == b, id(a) == id(b), 'a=%r, b=%r' % (a, b))
            """)

    def test_ne_defaults_to_not_eq(self):
        self.assertCodeExecution("""
            class Cmp:
                def __init__(self,arg):
                    self.arg = arg

                def __repr__(self):
                    return '<Cmp %s>' % self.arg

                def __eq__(self, other):
                    return self.arg == other

            a = Cmp(1)
            b = Cmp(1)
            c = Cmp(2)
            print(a == b) # True
            print(a != b) # False
            print(a != c) # True
            """)

    def test_ne_high_priority(self):
        self.assertCodeExecution("""
            # object.__ne__() should allow reflected __ne__() to be tried
            class Left:
                # Inherits object.__ne__()
                def __eq__(self, *args):
                    print('Left.__eq__')
                    return NotImplemented
            class Right:
                def __eq__(self, *args):
                    print('Right.__eq__')
                    return NotImplemented
                def __ne__(self, *args):
                    print('Right.__ne__')
                    return NotImplemented
            Left() != Right()
            """)

    def test_ne_low_priority(self):
        self.assertCodeExecution("""
            # object.__ne__() should not invoke reflected __eq__()
            class Base:
                # Inherits object.__ne__()
                def __eq__(self, *args):
                    print('Base.__eq__')
                    return NotImplemented
            class Derived(Base):  # Subclassing forces higher priority
                def __eq__(self, *args):
                    print('Derived.__eq__')
                    return NotImplemented
                def __ne__(self, *args):
                    print('Derived.__ne__')
                    return NotImplemented
            print(Base() != Derived())
            """)

    @expectedFailure
    # failing because class C not recreated on each loop
    def test_other_delegation(self):
        self.assertCodeExecution("""
            # No default delegation between operations except __ne__()
            ops = (
                ('__eq__', lambda a, b: a == b),
                ('__lt__', lambda a, b: a < b),
                ('__le__', lambda a, b: a <= b),
                ('__gt__', lambda a, b: a > b),
                ('__ge__', lambda a, b: a >= b),
            )
            for name, func in ops:
                def unexpected(*args):
                    print('Unexpected operator method called')
                class C:
                    __ne__ = unexpected
                for other, _ in ops:
                    if other != name:
                        setattr(C, other, unexpected)
                if name == '__eq__':
                    print(func(C(), object())) # False
                else:
                    try:
                        print(func(C(), object()))
                    except TypeError as err:
                        print(err)
            """)

    def test_issue_1393(self):
        self.assertCodeExecution("""
            class Anything:
                def __eq__(self, other):
                    return True

                def __ne__(self, other):
                    return False

            x = lambda: None
            print(x == Anything())
            print(Anything() == x)
            y = object()
            print(y == Anything())
            print(Anything() == y)
            """)

    def test_multiple_comparisons(self):
        self.assertCodeExecution("""
            print(1 == 1 == 1 == 1)
            print(1 > 2 > 3)
            print(1 == 1 == 2)
            print(1 == 1 != 2)
            print(1 == 1 < 2)
            print(3 == 3 < 2)
            print(1 < 2 < 3 > 2)
            print(0 == 0 == 0 == 0)
            print('abc' == '123' != '123')
            print('abc' == '123' == '123')
            print('abc' != '123' == '123')
            print(len('abcd') == 4 == len('1234'))
            x = 100
            print(x == (50 + 50) < 2000)
            print(x == (50 + 50) > 2000)
            """)
