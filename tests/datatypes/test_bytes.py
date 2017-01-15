from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class BytesTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            x.attr = 42
            print('Done.')
            """, exits_early=True)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            print(x.attr)
            print('Done.')
            """, exits_early=True)


class UnaryBytesOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
    ]


class BinaryBytesOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',

        'test_eq_class',
        'test_eq_frozenset',

        'test_ne_class',
        'test_ne_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_ge_class',
        'test_ge_frozenset',

        'test_gt_class',
        'test_gt_frozenset',

        'test_le_class',
        'test_le_frozenset',

        'test_lt_class',
        'test_lt_frozenset',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_bool',
        'test_modulo_bytearray',
        'test_modulo_bytes',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_slice',
        'test_modulo_str',
        'test_modulo_tuple',

        'test_multiply_class',
        'test_multiply_frozenset',

        'test_or_class',
        'test_or_frozenset',

        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

        'test_subscr_class',
        'test_subscr_frozenset',

        'test_subtract_class',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
    ]


class InplaceBytesOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

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

        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_bool',
        'test_modulo_bytearray',
        'test_modulo_bytes',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_slice',
        'test_modulo_str',
        'test_modulo_tuple',

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
