from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class FloatTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = 3.14159
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = 3.14159
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)

    def test_repr(self):
        self.assertCodeExecution("""
            x = 350000000000000000.0
            print(x)
            x = 3500.0
            print(x)
            x = 35.0
            print(x)
            x = 3.5
            print(x)
            x = 0.35
            print(x)
            x = 0.035
            print(x)
            x = 0.0035
            print(x)
            x = 0.00035
            print(x)
            x = 0.000035
            print(x)
            x = 0.0000035
            print(x)
            x = 0.00000000000000035
            print(x)

            x = 0.0
            print(x)
            x = float('-0.0')
            print(x)
            x = float('nan')
            print(x)
            x = float('inf')
            print(x)
            x = float('-inf')
            print(x)
            """)

    def test_negative_zero_constant(self):
        self.assertCodeExecution("""
            x = -0.0
            y = 0.0
            print(x, y)
            """)

    def test_is_integer(self):
        self.assertCodeExecution("""
            x = 0.0
            print(x.is_integer())
            x = 3.14
            print(x.is_integer())
            x = -1.0
            print(x.is_integer())
            x = -62.5
            print(x.is_integer())
            x = float('nan')
            print(x.is_integer())
            x = float('inf')
            print(x.is_integer())
            x = float('-inf')
            print(x.is_integer())
            """)

    def test_hex(self):
        numbers = [
            0e0, -0e0, 10000152587890625e-16, -566e85,
            -87336362425182547697e-280, 4.9406564584124654e-324,
            'nan', 'inf', '-inf'
        ]
        template = """
            x = float('{}')
            print(x.hex())
            """
        code = '\n'.join(template.format(number) for number in numbers)
        self.assertCodeExecution(code)


class UnaryFloatOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'float'

    not_implemented = [
    ]


class BinaryFloatOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'float'

    not_implemented = [
        'test_modulo_complex',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_frozenset',
        'test_multiply_NotImplemented',
        'test_multiply_range',

        'test_power_complex',
        'test_power_float',

        'test_subscr_bool',
        'test_subscr_bytearray',
        'test_subscr_bytes',
        'test_subscr_class',
        'test_subscr_complex',
        'test_subscr_dict',
        'test_subscr_float',
        'test_subscr_frozenset',
        'test_subscr_int',
        'test_subscr_list',
        'test_subscr_None',
        'test_subscr_NotImplemented',
        'test_subscr_range',
        'test_subscr_set',
        'test_subscr_slice',
        'test_subscr_str',
        'test_subscr_tuple',

        'test_true_divide_complex',
    ]


class InplaceFloatOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'float'

    not_implemented = [
        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_frozenset',
        'test_multiply_list',
        'test_multiply_NotImplemented',
        'test_multiply_range',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_power_complex',
        'test_power_float',

        'test_true_divide_complex',
    ]
