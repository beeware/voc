from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class ComplexTests(TranspileTestCase):
    def test_conjugate(self):
        self.assertCodeExecution("""
            x = complex(1.5, 1)
            print(x.conjugate())
            """)

    def test_real_imag(self):
        self.assertCodeExecution("""
            x = complex(1, 2.0)
            print(x.real)
            print(x.imag)
            """)

    def test_equality_with_numbers_when_zero_imag(self):
        self.assertCodeExecution("""
            x = 2
            y = complex(2, 0)
            print(x == y)
            print(y.__eq__(x))
            print(x != y)
            print(y.__ne__(x))

            x = 2.0
            y = complex(3, 0)
            print(x == y)
            print(y.__eq__(x))
            print(x != y)
            print(y.__ne__(x))

            x = True
            y = complex(1, 0)
            print(x == y)
            print(y.__eq__(x))
            print(x != y)
            print(y.__ne__(x))
            """)


class UnaryComplexOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'complex'


class BinaryComplexOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'complex'

    substitutions = {
        "(-161.18751321137705+195.77962956590406j)": [
            "(-161.18751321137705+195.77962956590403j)"
        ],
        "(2.6460893340172016e-18+0.04321391826377225j)": [
            "(2.6460019439688186e-18+0.04321391826377225j)"
        ],
        "(-9.8368221286278e-14-535.4916555247646j)": [
            "(-9.836497256617357e-14-535.4916555247646j)"
        ]
    }

    is_flakey = [
        'test_power_complex',
        'test_power_float',
    ]


class InplaceComplexOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'complex'

    not_implemented = [
        'test_eq_None',
        'test_eq_NotImplemented',
        'test_eq_slice',
        'test_eq_range',
        'test_eq_bool',
        'test_eq_bytearray',
        'test_eq_bytes',
        'test_eq_class',
        'test_eq_complex',
        'test_eq_dict',
        'test_eq_float',
        'test_eq_frozenset',
        'test_eq_int',
        'test_eq_list',
        'test_eq_none',
        'test_eq_set',
        'test_eq_str',
        'test_eq_tuple',

        'test_floor_divide_None',
        'test_floor_divide_NotImplemented',
        'test_floor_divide_slice',
        'test_floor_divide_range',
        'test_floor_divide_bool',
        'test_floor_divide_bytearray',
        'test_floor_divide_bytes',
        'test_floor_divide_class',
        'test_floor_divide_dict',
        'test_floor_divide_float',
        'test_floor_divide_frozenset',
        'test_floor_divide_int',
        'test_floor_divide_list',
        'test_floor_divide_none',
        'test_floor_divide_set',
        'test_floor_divide_str',
        'test_floor_divide_tuple',

        'test_ge_None',
        'test_ge_NotImplemented',
        'test_ge_slice',
        'test_ge_range',
        'test_ge_bool',
        'test_ge_bytearray',
        'test_ge_bytes',
        'test_ge_class',
        'test_ge_complex',
        'test_ge_dict',
        'test_ge_float',
        'test_ge_frozenset',
        'test_ge_int',
        'test_ge_list',
        'test_ge_none',
        'test_ge_set',
        'test_ge_str',
        'test_ge_tuple',

        'test_gt_None',
        'test_gt_NotImplemented',
        'test_gt_slice',
        'test_gt_range',
        'test_gt_bool',
        'test_gt_bytearray',
        'test_gt_bytes',
        'test_gt_class',
        'test_gt_complex',
        'test_gt_dict',
        'test_gt_float',
        'test_gt_frozenset',
        'test_gt_int',
        'test_gt_list',
        'test_gt_none',
        'test_gt_set',
        'test_gt_str',
        'test_gt_tuple',

        'test_le_None',
        'test_le_NotImplemented',
        'test_le_slice',
        'test_le_range',
        'test_le_bool',
        'test_le_bytearray',
        'test_le_bytes',
        'test_le_class',
        'test_le_complex',
        'test_le_dict',
        'test_le_float',
        'test_le_frozenset',
        'test_le_int',
        'test_le_list',
        'test_le_none',
        'test_le_set',
        'test_le_str',
        'test_le_tuple',

        'test_lshift_none',

        'test_lt_None',
        'test_lt_NotImplemented',
        'test_lt_slice',
        'test_lt_range',
        'test_lt_bool',
        'test_lt_bytearray',
        'test_lt_bytes',
        'test_lt_class',
        'test_lt_complex',
        'test_lt_dict',
        'test_lt_float',
        'test_lt_frozenset',
        'test_lt_int',
        'test_lt_list',
        'test_lt_none',
        'test_lt_set',
        'test_lt_str',
        'test_lt_tuple',

        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_slice',
        'test_modulo_range',
        'test_modulo_bool',
        'test_modulo_bytearray',
        'test_modulo_bytes',
        'test_modulo_class',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_none',
        'test_modulo_set',
        'test_modulo_str',
        'test_modulo_tuple',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_list',
        'test_multiply_none',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_ne_None',
        'test_ne_NotImplemented',
        'test_ne_slice',
        'test_ne_range',
        'test_ne_bool',
        'test_ne_bytearray',
        'test_ne_bytes',
        'test_ne_class',
        'test_ne_complex',
        'test_ne_dict',
        'test_ne_float',
        'test_ne_frozenset',
        'test_ne_int',
        'test_ne_list',
        'test_ne_none',
        'test_ne_set',
        'test_ne_str',
        'test_ne_tuple',

        'test_power_complex',
        'test_power_none',

        'test_rshift_none',

        'test_subscr_None',
        'test_subscr_NotImplemented',
        'test_subscr_slice',
        'test_subscr_range',
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
        'test_subscr_none',
        'test_subscr_set',
        'test_subscr_str',
        'test_subscr_tuple',

        'test_true_divide_none',
    ]
