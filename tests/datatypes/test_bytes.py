from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class BytesTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)

    def test_capitalize(self):
        self.assertCodeExecution(r"""
            print(b'hello, world'.capitalize())
            print(b'helloWORLD'.capitalize())
            print(b'HELLO WORLD'.capitalize())
            print(b'2015638687'.capitalize())
            print(b'\xc8'.capitalize())
        """)

    def test_repr(self):
        self.assertCodeExecution(r"""
            print(repr(b'\xc8'))
            print(repr(b'abcdef \xc8 abcdef'))
            print(repr(b'abcdef \xc8 abcdef\n\r\t'))
            print(b'abcdef \xc8 abcdef\n\r\t')
        """)

    def test_iter(self):
        self.assertCodeExecution("""
            print([b for b in b''])
            print([b for b in b'hello world'])
        """)

    def test_getitem(self):

        self.assertCodeExecution("""
            x = b'0123456789'
            print("x[0] = ", x[0])
            print("x[-10] = ", x[-10])
            print("x[9] = ", x[9])
            #Start/Stop Empty w/Step +/-
            print("x[:] = ", x[:])
            print("x[::1] = ", x[::1])
            print("x[::2] = ", x[::2])
            print("x[::3] = ", x[::3])
            print("x[::-1] = ", x[::-1])
            print("x[::-2] = ", x[::-2])
            print("x[::-3] = ", x[::-3])
            #Empty Start Tests With Stop Bounds checks
            print("x[:9:1] = ", x[:9:1])
            print("x[:10:1] = ", x[:10:1])
            print("x[:11:1] = ", x[:11:1])
            print("x[:-9:1] = ", x[:-9:1])
            print("x[:-10:1] = ", x[:-10:1])
            print("x[:-11:1] = ", x[:-11:1])
            print("x[:9:2] = ", x[:9:2])
            print("x[:10:2] = ", x[:10:2])
            print("x[:11:2] = ", x[:11:2])
            print("x[:-9:2] = ", x[:-9:2])
            print("x[:-10:2] = ", x[:-10:2])
            print("x[:-11:2] = ", x[:-11:2])
            print("x[:9:3] = ", x[:9:3])
            print("x[:10:3] = ", x[:10:3])
            print("x[:11:3] = ", x[:11:3])
            print("x[:-9:3] = ", x[:-9:3])
            print("x[:-10:3] = ", x[:-10:3])
            print("x[:-11:3] = ", x[:-11:3])
            print("x[:9:-1] = ", x[:9:-1])
            print("x[:10:-1] = ", x[:10:-1])
            print("x[:11:-1] = ", x[:11:-1])
            print("x[:-9:-1] = ", x[:-9:-1])
            print("x[:-10:-1] = ", x[:-10:-1])
            print("x[:-11:-1] = ", x[:-11:-1])
            print("x[:9:-2] = ", x[:9:-2])
            print("x[:10:-2] = ", x[:10:-2])
            print("x[:11:-2] = ", x[:11:-2])
            print("x[:-9:-2] = ", x[:-9:-2])
            print("x[:-10:-2] = ", x[:-10:-2])
            print("x[:-11:-2] = ", x[:-11:-2])
            print("x[:9:-3] = ", x[:9:-3])
            print("x[:10:-3] = ", x[:10:-3])
            print("x[:11:-3] = ", x[:11:-3])
            print("x[:-9:-3] = ", x[:-9:-3])
            print("x[:-10:-3] = ", x[:-10:-3])
            print("x[:-11:-3] = ", x[:-11:-3])
            #Empty stop tests with stop bounds checks
            print("x[9::1] = ", x[9::1])
            print("x[10::1] = ", x[10::1])
            print("x[11::1] = ", x[11::1])
            print("x[-9::1] = ", x[-9::1])
            print("x[-10::1] = ", x[-10::1])
            print("x[-11::1] = ", x[-11::1])
            print("x[9::2] = ", x[9::2])
            print("x[10::2] = ", x[10::2])
            print("x[11::2] = ", x[11::2])
            print("x[-9::2] = ", x[-9::2])
            print("x[-10::2] = ", x[-10::2])
            print("x[-11::2] = ", x[-11::2])
            print("x[9::3] = ", x[9::3])
            print("x[10::3] = ", x[10::3])
            print("x[11::3] = ", x[11::3])
            print("x[-9::3] = ", x[-9::3])
            print("x[-10::3] = ", x[-10::3])
            print("x[-11::3] = ", x[-11::3])
            print("x[9::-1] = ", x[9::-1])
            print("x[10::-1] = ", x[10::-1])
            print("x[11::-1] = ", x[11::-1])
            print("x[-9::-1] = ", x[-9::-1])
            print("x[-10::-1] = ", x[-10::-1])
            print("x[-11::-1] = ", x[-11::-1])
            print("x[9::-2] = ", x[9::-2])
            print("x[10::-2] = ", x[10::-2])
            print("x[11::-2] = ", x[11::-2])
            print("x[-9::-2] = ", x[-9::-2])
            print("x[-10::-2] = ", x[-10::-2])
            print("x[-11::-2] = ", x[-11::-2])
            print("x[9::-3] = ", x[9::-3])
            print("x[10::-3] = ", x[10::-3])
            print("x[11::-3] = ", x[11::-3])
            print("x[-9::-3] = ", x[-9::-3])
            print("x[-10::-3] = ", x[-10::-3])
            print("x[-11::-3] = ", x[-11::-3])
            #other tests
            print("x[-5:] = ", x[-5:])
            print("x[:-5] = ", x[:-5])
            print("x[-2:-8] = ", x[-2:-8])
            print("x[100::-1] = ", x[100::-1])
            print("x[100:-100:-1] = ", x[100:-100:-1])
            print("x[:-100:-1] = ", x[:-100:-1])
            print("x[::-1] = ", x[::-1])
            print("x[::-2] = ", x[::-2])
            print("x[::-3] = ", x[::-3])
            print("x[:0:-1] = ", x[:0:-1])
            print("x[-5::-2] = ", x[-5::-2])
            print("x[:-5:-2] = ", x[:-5:-2])
            print("x[-2:-8:-2] = ", x[-2:-8:-2])
            print("x[0:9] = ", x[0:9])
            print("x[0:10:1] = ", x[0:10:1] )
            print("x[10:0] = ", x[10:0])
            print("x[10:0:-1] = ", x[10:0:-1])
            print("x[10:-10:-1] = ", x[10:-10:-1])
            print("x[10:-11:-1] = ", x[10:-11:-1])
            """)

    def test_count(self):
        self.assertCodeExecution("""
            print(b'abcabca'.count(97))
            print(b'abcabca'.count(b'abc'))
            print(b'qqq'.count(b'q'))
            print(b'qqq'.count(b'qq'))
            print(b'qqq'.count(b'qqq'))
            print(b'qqq'.count(b'qqqq'))
            print(b'abcdefgh'.count(b'bc',-7, -5))
            print(b'abcdefgh'.count(b'bc',1, -5))
            print(b'abcdefgh'.count(b'bc',0, 3))
            print(b'abcdefgh'.count(b'bc',-7, 500))
            print(b'qqaqqbqqqcqqqdqqqqeqqqqf'.count(b'qq'),1)
            print(b''.count(b'q'),0)
        """)
        self.assertCodeExecution("""
            b'abcabc'.count([]) #Test TypeError invalid byte array
        """, exits_early=True)
        self.assertCodeExecution("""
            b'abcabc'.count(256) #Test ValueError invalid integer range
        """, exits_early=True)
        self.assertCodeExecution("""
            print(b'abcabca'.count(97, [], 3)) #Test Slicing Error on Start
        """, exits_early=True)
        self.assertCodeExecution("""
            print(b'abcabca'.count(97, 3, [])) #Test Slicing Error on End
        """, exits_early=True)

    def test_find(self):
        self.assertCodeExecution("""
            print(b''.find(b'a'))
            print(b'abcd'.find(b''))
            print(b'abcd'.find(b'...'))
            print(b'abcd'.find(b'a'))
            print(b'abcd'.find(b'b'))
            print(b'abcd'.find(b'c'))
            print(b'abcd'.find(b'd'))
            print(b'abcd'.find(b'ab'))
            print(b'abcd'.find(b'bc'))
            print(b'abcd'.find(b'cd'))
            print(b'abcd'.find(b'cd', 2))
            print(b'abcd'.find(b'ab', 3))
            print(b'abcd'.find(b'cd', 2, 3))
            print(b'abcd'.find(b'ab', 3, 4))
        """)

    def test_index(self):
        self.assertCodeExecution("""
            print(b'abcd'.index(b'ab'))
            print(b'abcd'.index(b'bc'))
            print(b'abcd'.index(b'cd'))
            print(b'abcd'.find(b'cd', 2))
            print(b'abcd'.find(b'cd', 2, 3))
        """)
        self.assertCodeExecution("""
            print(b''.index(b'a'))
            print(b'abcd'.index(b''))
            print(b'abcd'.index(b'...'))
            print(b'abcd'.find(b'ab', 3))
            print(b'abcd'.find(b'ab', 3, 4))
        """, exits_early=True)


class UnaryBytesOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
    ]


class BinaryBytesOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
        'test_direct_eq_bytearray',
        'test_direct_eq_none',

        'test_direct_ge_bytearray',
        'test_direct_ge_none',

        'test_direct_gt_bytearray',
        'test_direct_gt_none',

        'test_direct_le_bytearray',
        'test_direct_le_none',

        'test_direct_lt_bytearray',
        'test_direct_lt_none',

        'test_direct_ne_bytearray',
        'test_direct_ne_none',

        'test_modulo_complex',
        'test_modulo_dict',
    ]

    not_implemented_versions = {
        'test_modulo_None': (3.5, 3.6),
        'test_modulo_NotImplemented': (3.5, 3.6),
        'test_modulo_bool': (3.5, 3.6),
        'test_modulo_bytearray': (3.5, 3.6),
        'test_modulo_bytes': (3.5, 3.6),
        'test_modulo_class': (3.5, 3.6),
        'test_modulo_float': (3.5, 3.6),
        'test_modulo_frozenset': (3.5, 3.6),
        'test_modulo_int': (3.5, 3.6),
        'test_modulo_list': (3.5, 3.6),
        'test_modulo_range': (3.5, 3.6),
        'test_modulo_set': (3.5, 3.6),
        'test_modulo_slice': (3.5, 3.6),
        'test_modulo_str': (3.5, 3.6),
        'test_modulo_tuple': (3.5, 3.6),
    }


class InplaceBytesOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
        'test_modulo_complex',
        'test_modulo_dict',
    ]

    not_implemented_versions = {
        'test_modulo_None': (3.5, 3.6),
        'test_modulo_NotImplemented': (3.5, 3.6),
        'test_modulo_bool': (3.5, 3.6),
        'test_modulo_bytearray': (3.5, 3.6),
        'test_modulo_bytes': (3.5, 3.6),
        'test_modulo_class': (3.5, 3.6),
        'test_modulo_float': (3.5, 3.6),
        'test_modulo_frozenset': (3.5, 3.6),
        'test_modulo_int': (3.5, 3.6),
        'test_modulo_list': (3.5, 3.6),
        'test_modulo_range': (3.5, 3.6),
        'test_modulo_set': (3.5, 3.6),
        'test_modulo_slice': (3.5, 3.6),
        'test_modulo_str': (3.5, 3.6),
        'test_modulo_tuple': (3.5, 3.6),
    }
