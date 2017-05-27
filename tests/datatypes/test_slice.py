from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class SliceTests(TranspileTestCase):
    def test_slice_list(self):
        self.assertCodeExecution("""
            x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            print("x[:] = ", x[:])
            print("x[5:] = ", x[5:])
            print("x[:5] = ", x[:5])
            print("x[2:8] = ", x[2:8])

            print("x[::2] = ", x[::2])
            print("x[5::2] = ", x[5::2])
            print("x[:5:2] = ", x[:5:2])
            print("x[2:8:2] = ", x[2:8:2])
            """)

    def test_slice_range(self):
        self.assertCodeExecution("""
            x = range(0, 10)
            print("x[:] = ", x[:])
            print("x[5:] = ", x[5:])
            print("x[:5] = ", x[:5])
            print("x[2:8] = ", x[2:8])

            print("x[::2] = ", x[::2])
            print("x[5::2] = ", x[5::2])
            print("x[:5:2] = ", x[:5:2])
            print("x[2:8:2] = ", x[2:8:2])
            """)

    def test_slice_string(self):
        self.assertCodeExecution("""
            x = "0123456789a"
            print("x[:] = ", x[:])
            print("x[5:] = ", x[5:])
            print("x[:5] = ", x[:5])
            print("x[2:8] = ", x[2:8])

            print("x[::2] = ", x[::2])
            print("x[5::2] = ", x[5::2])
            print("x[:5:2] = ", x[:5:2])
            print("x[2:8:2] = ", x[2:8:2])
            """)

    def test_slice_tuple(self):
        self.assertCodeExecution("""
            x = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
            print("x[:] = ", x[:])
            print("x[5:] = ", x[5:])
            print("x[:5] = ", x[:5])
            print("x[2:8] = ", x[2:8])

            print("x[::2] = ", x[::2])
            print("x[5::2] = ", x[5::2])
            print("x[:5:2] = ", x[:5:2])
            print("x[2:8:2] = ", x[2:8:2])
            """)

    def test_slice_index(self):
        self.assertCodeExecution("""
            class C(object):
                def __init__(self, value):
                    self._value = value
                def __index__(self):
                    return self._value
            x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            print("x[:] = ", x[:])
            print("x[C(5):] = ", x[C(5):])
            print("x[:C(5)] = ", x[:C(5)])
            print("x[C(2):C(8)] = ", x[C(2):C(8)])
            print("x[::C(2)] = ", x[::C(2)])
            print("x[C(5)::C(2)] = ", x[C(5)::C(2)])
            print("x[:C(5):C(2] = ", x[:C(5):C(2)])
            print("x[C(2):C(8):C(2)] = ", x[C(2):C(8):C(2)])
            """)
        self.assertCodeExecution("""
            class D(object):
                def __init__(self, value):
                    self._value = value
            x = b"0123456789"
            print("x[D(1)::1] = ", x[D(1)::1])
        """, exits_early=True)
        self.assertCodeExecution("""
            class D(object):
                def __init__(self, value):
                    self._value = value
            x = b"0123456789"
            print("x[:D(10):1] = ", x[:D(10):1])
        """, exits_early=True)
        self.assertCodeExecution("""
            class D(object):
                def __init__(self, value):
                    self._value = value
            x = b"0123456789"
            print("x[::D(1)] = ", x[::D(1)])
        """, exits_early=True)

    def test_slice_bytes(self):
        self.assertCodeExecution("""
            x = b"0123456789"
            print("x[:] = ", x[:])
            print("x[5:] = ", x[5:])
            print("x[:5] = ", x[:5])
            print("x[2:8] = ", x[2:8])

            print("x[::2] = ", x[::2])
            print("x[5::2] = ", x[5::2])
            print("x[:5:2] = ", x[:5:2])
            print("x[2:8:2] = ", x[2:8:2])

            print("x[:] = ", x[:])
            print("x[-5:] = ", x[-5:])
            print("x[:-5] = ", x[:-5])
            print("x[-2:-8] = ", x[-2:-8])

            print("x[::-2] = ", x[::-2])
            print("x[-5::-2] = ", x[-5::-2])
            print("x[:-5:-2] = ", x[:-5:-2])
            print("x[-2:-8:-2] = ", x[-2:-8:-2])
            """)

    def test_negative_indexing(self):
        self.assertCodeExecution("""
            x = b"0123456789"
            print("x[:] = ", x[:])
            print("x[-5:] = ", x[-5:])
            print("x[:-5] = ", x[:-5])
            print("x[-2:-8] = ", x[-2:-8])

            print("x[::-2] = ", x[::-2])
            print("x[-5::-2] = ", x[-5::-2])
            print("x[:-5:-2] = ", x[:-5:-2])
            print("x[-2:-8:-2] = ", x[-2:-8:-2])
            """)


class UnarySliceOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'slice'

    not_implemented = [
        'test_unary_invert',
        'test_unary_negative',
        'test_unary_not',
        'test_unary_positive',
    ]


class BinarySliceOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'slice'

    not_implemented = [



        'test_direct_eq_slice',
        'test_direct_ge_slice',
        'test_direct_gt_slice',
        'test_direct_le_slice',
        'test_direct_lt_slice',
        'test_direct_ne_slice',

        'test_eq_slice',

        'test_ge_class',
        'test_ge_slice',

        'test_gt_class',
        'test_gt_slice',

        'test_le_class',
        'test_le_slice',


        'test_lt_class',
        'test_lt_slice',

        'test_modulo_complex',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_list',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_ne_slice',




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



    ]


class InplaceSliceOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'slice'

    not_implemented = [



        'test_modulo_complex',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_list',
        'test_multiply_str',
        'test_multiply_tuple',






    ]
