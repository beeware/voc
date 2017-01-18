from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class DictTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = {}
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = {}
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)

    def test_creation(self):
        # Empty dict
        self.assertCodeExecution("""
            x = {}
            print(x)
            """)

        self.assertCodeExecution("""
            x = {'a': 1}
            print(x)
            """)

    def test_getitem(self):
        # Simple existent key
        self.assertCodeExecution("""
            y = 37
            x = {'a': 1, 'b': 2, 'c': y}
            print('a' in x)
            print('a' not in x)
            print(x['a'])
            """)

        # Simple non-existent key
        self.assertCodeExecution("""
            x = {'a': 1, 'b': 2}
            print('c' in x)
            print('c' not in x)
            try:
                print(x['c'])
            except KeyError as err:
                print(err)
            """)

    def test_clear(self):
        # Clear a dictionary
        self.assertCodeExecution("""
            x = {'a': 1, 'b': 2}
            print('a' in x)
            print(x.clear())
            print('a' not in x)
            print(x)
            """)

        # Clear an already empty dict
        self.assertCodeExecution("""
            x = {}
            print('a' not in x)
            print(x.clear())
            print('a' not in x)
            print(x)
            """)

    def test_builtin_constructor(self):
        # Construct a dictionary using the dict builtin
        self.assertCodeExecution("""
            x = dict()
            print(x)
            print('a' in x)

            # List of tuples
            x = dict([('a', 1), ('b', 2)])
            print('a' in x)
            print(x['a'])
            print('c' in x)

            # List of lists
            x = dict([['a', 3], ['b', 4]])
            print('a' in x)
            print(x['a'])
            print('c' in x)

            # Tuple of lists
            x = dict((['a', 5], ['b', 6]))
            print('a' in x)
            print(x['a'])
            print('c' in x)

            # Tuple of tuples
            x = dict((('a', 5), ('b', 6)))
            print('a' in x)
            print(x['a'])
            print('c' in x)

            # Test __contains__ throws unhashable exception
            try:
                print([] in x)
            except TypeError as err:
                print(err)
            try:
                print([] not in x)
            except TypeError as err:
                print(err)
        """)

    def test_builtin_non_2_tuples(self):
        # One of the elements isn't a 2-tuple
        self.assertCodeExecution("""
            try:
                x = dict([('a', 1), ('b', 2, False)])
            except ValueError as err:
                print(err)
            """)

    def test_builtin_non_sequence(self):
        # One of the elements isn't a sequence
        self.assertCodeExecution("""
            try:
                x = dict([('a', 1), False, ('b', 2)])
            except TypeError as err:
                print(err)
            """)

    def test_method_popitem(self):
        self.assertCodeExecution("""
            ITEMS = [(1, 2), (3, ("4", 5))]
            x = dict(ITEMS)

            popped_1 = x.popitem()
            print(popped_1 in ITEMS)

            popped_2 = x.popitem()
            print(popped_2 in ITEMS and popped_2 != popped_1)

            # Check for exception
            try:
                print(x.popitem())
            except KeyError as err:
                print(err)
            """)

    def test_method_setdefault(self):
        self.assertCodeExecution("""
            x = {42: 'Babel'}
            print(x.setdefault(42)) # should return Babel

            print(x.setdefault(1)) # should return None
            print(x[1] == None) # should be True

            print(x.setdefault('David', 'Gilmour')) # should return 'Gilmour'

            # Check unhashable exceptions
            try:
                x.setdefault([], 42)
            except TypeError as err:
                print(err)
            """)

    def test_method_get(self):
        self.assertCodeExecution("""
            x = {1: 2}
            print(x.get(1))
            print(x.get(2))
            print(x.get(3,4))
            """)

        # check for unhashable type errors
        self.assertCodeExecution("""
            x = {1: 2}
            try:
                print(x.get([]))
            except TypeError as err:
                print(err)
            try:
                print(x.get([], 1))
            except TypeError as err:
                print(err)
            """)


class UnaryDictOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'dict'


class BinaryDictOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'dict'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',

        'test_eq_class',
        'test_eq_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_ge_class',
        'test_ge_frozenset',

        'test_gt_class',
        'test_gt_frozenset',

        'test_le_class',
        'test_le_frozenset',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_lt_class',
        'test_lt_frozenset',

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_bytearray',
        'test_multiply_class',
        'test_multiply_frozenset',

        'test_ne_class',
        'test_ne_frozenset',

        'test_or_class',
        'test_or_frozenset',

        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

        'test_subscr_bytearray',
        'test_subscr_class',
        'test_subscr_complex',
        'test_subscr_frozenset',
        'test_subscr_slice',

        'test_subtract_class',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
    ]


class InplaceDictOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'dict'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_class',
        'test_multiply_frozenset',

        'test_or_class',
        'test_or_frozenset',

        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

        'test_subtract_class',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
    ]
