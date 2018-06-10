from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class TupleTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = (1, 2, 3)
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = (1, 2, 3)
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)

    def test_creation(self):
        self.assertCodeExecution("""
            a = 1
            b = 2
            c = 3
            d = 4
            e = 5
            x = (a, b, c, d, e)
            print(x)
            """)

    def test_const_creation(self):
        self.assertCodeExecution("""
            x = (1, 2, 3, 4, 5)
            print(x)
            """)

    def test_const_creation_multitype(self):
        self.assertCodeExecution("""
            x = (1, 2.5, "3", True, 5)
            print(x)
            """)

    def test_getitem(self):
        # Simple positive index
        self.assertCodeExecution("""
            x = (1, 2, 3, 4, 5)
            print(x[2])
            """)

        # Simple negative index
        self.assertCodeExecution("""
            x = (1, 2, 3, 4, 5)
            print(x[-2])
            """)

        # Positive index out of range
        self.assertCodeExecution("""
            x = (1, 2, 3, 4, 5)
            try:
                print(x[10])
            except IndexError as err:
                print(err)
            """)

        # Negative index out of range
        self.assertCodeExecution("""
            x = (1, 2, 3, 4, 5)
            try:
                print(x[-10])
            except IndexError as err:
                print(err)
            """)

    def test_lt(self):
        self.assertCodeExecution("""
            pairs = [
                (1, 2, 3), (3, 2, 1),
                (1, 2, 1), (1, 2, 4),
                (1, 2, 3, 4), (1, 2, 3, 0)
            ]
            for p1 in pairs:
                for p2 in pairs:
                    print(p1, "<", p2, ":", p1 < p2)
            """, run_in_function=False)

    def test_immutable(self):
        self.assertCodeExecution("""
            x = (1, 2)
            try:
                x[0] = 3
            except TypeError as err:
                print(err)
            try:
                x[-1] = 3
            except TypeError as err:
                print(err)
            try:
                x[2] = 3
            except TypeError as err:
                print(err)
            """, run_in_function=False)

    def test_lt_reflected(self):
        self.assertCodeExecution("""
            class A:
                def __gt__(self, other):
                    return True

            x = A()
            y = A()

            # verify that A doesn't have __lt__()
            print(x.__lt__(x))

            # ensure rich comparison logic is used
            print((x,) < (x,)) # False, x is x and same size
            print((x,) < (y,)) # True, x is not y, reflected

            # when elements are non-identical, return that comparison, even if size is not
            print((x, y) < (y,)) # True, x is not y, reflected

            # ensure tie breaker by size is still used when identical elements
            print((x, y) < (x,)) # False, larger size
            print((x,) < (x, y)) # True, smaller size
            """)

    def test_le_reflected(self):
        self.assertCodeExecution("""
            class A:
                def __ge__(self, other):
                    return True

            x = A()
            y = A()

            # verify that A doesn't have __le__()
            print(x.__le__(x))

            # ensure rich comparison logic is used
            print((x,) <= (x,)) # False, x is x and same size
            print((x,) <= (y,)) # True, x is not y, reflected

            # when elements are non-identical, return that comparison, even if size is not
            print((x, y) <= (y,)) # True, x is not y, reflected

            # ensure tie breaker by size is still used when identical elements
            print((x, y) <= (x,)) # False, larger size
            print((x,) <= (x, y)) # True, smaller size
            """)

    def test_gt_reflected(self):
        self.assertCodeExecution("""
            class A:
                def __lt__(self, other):
                    return True

            x = A()
            y = A()

            # verify that A doesn't have __gt__()
            print(x.__gt__(x))

            # ensure rich comparison logic is used
            print((x,) > (x,)) # False, x is x and same size
            print((x,) > (y,)) # True, x is not y, reflected

            # when elements are non-identical, return that comparison, even if size is not
            print((x, y) > (y,)) # True, x is not y, reflected

            # ensure tie breaker by size is still used when identical elements
            print((x, y) > (x,)) # False, larger size
            print((x,) > (x, y)) # True, smaller size
            """)

    def test_ge_reflected(self):
        self.assertCodeExecution("""
            class A:
                def __le__(self, other):
                    return True

            x = A()
            y = A()

            # verify that A doesn't have __ge__()
            print(x.__ge__(x))

            # ensure rich comparison logic is used
            print((x,) >= (x,)) # False, x is x and same size
            print((x,) >= (y,)) # True, x is not y, reflected

            # when elements are non-identical, return that comparison, even if size is not
            print((x, y) >= (y,)) # True, x is not y, reflected

            # ensure tie breaker by size is still used when identical elements
            print((x, y) >= (x,)) # False, larger size
            print((x,) >= (x, y)) # True, smaller size
            """)

    def test_eq_reflected(self):
        self.assertCodeExecution("""
            class A:
                def __eq__(self, other):
                    return True

            class B:
                def __eq__(self, other):
                    return False

            x = A()
            y = B()

            print((x,) == (x,)) # True, identity implies equality
            print((x, x) == (x,)) # False, size not equal

            print((x,) == (y,)) # True, x is not y, x.__eq__(y)
            print((y,) == (x,)) # False, y is not x, y.__eq__(x)
            """)

    def test_iteration(self):
        self.assertCodeExecution("""
            a = (1, 2, 3, 4, 5)
            b = ()
            for x in a:
                print(x)
            for x in b:
                print(x)
            """)

    def test_index(self):
        # success
        self.assertCodeExecution("""
            a = (1, 2, 3, 4, 3)
            print(a.index(2))
            print(a.index(2,1))
            print(a.index(2,1,5))
            print(a.index(2,0,1000))
            print(a.index(2,-300))
            """)

        # raise exceptions
        self.assertCodeExecution("""
            a = (1, 2, 3, 4, 3)
            try:
                print(a.index('2'))
            except ValueError as err:
                print(err)
            try:
                print(a.index(2,0,-50))
            except ValueError as err:
                print(err)
            try:
                print(a.index(7,0,5))
            except ValueError as err:
                print(err)
            try:
                print(a.index())
            except TypeError as err:
                print(err)
            """)


class UnaryTupleOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'tuple'


class BinaryTupleOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'tuple'


class InplaceTupleOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'tuple'
