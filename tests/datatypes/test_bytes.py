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

    def test_islower(self):
        self.assertCodeExecution("""
            print(b'abc'.islower())
            print(b''.islower())
            print(b'Abccc'.islower())
            print(b'HELLO WORD'.islower())
            print(b'@#$%!'.islower())
            print(b'hello world'.islower())
            print(b'hello world   '.islower())
            # TODO: uncomment when adding support for literal hex bytes
            #print(b'\xf0'.islower())

        """)
        # self.assertCodeExecution("""""")

    def test_isupper(self):
        self.assertCodeExecution("""
            print(b'abc'.isupper())
            print(b''.isupper())
            print(b'Abccc'.isupper())
            print(b'HELLO WORD'.isupper())
            print(b'@#$%!'.isupper())
            print(b'hello world'.isupper())
            print(b'hello world   '.isupper())
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

    def test_partition(self):
        self.assertCodeExecution(r"""
            print(b'hello, world'.partition(b','))
            print(b'hello, world'.partition(b'h'))
            print(b'hello, world'.partition(b'd'))
            print(b'hello, world'.partition(b', '))
            print(b'hello, world'.partition(b'l'))
            print(b'2015638687'.partition(b'a'))
            print(b'\xc8'.partition(b' '))
        """)
        # self.assertCodeExecution(r"""
        #     print(b'hello, world'.partition(None))
        # """, exits_early=True)

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

    def test_contains(self):
        self.assertCodeExecution("""
            print(b'py' in b'pybee')
            print(b'bee' in b'pybee')
            print(b'ybe' in b'pybee')
            print(b'test' in b'pybee')
            print(101 in b'pybee')
        """)
        self.assertCodeExecution("""
            print(300 in b'pybee') #Test ValueError invalid integer range
        """, exits_early=True)
        self.assertCodeExecution("""
            print(['b', 'e'] in b'pybee') #Test TypeError invalid byte array
        """, exits_early=True)

    def test_isalnum(self):
        self.assertCodeExecution("""
            print(b'w1thnumb3r2'.isalnum())
            print(b'withoutnumber'.isalnum())
            print(b'with spaces'.isalnum())
            print(b'666'.isalnum())
            print(b'66.6'.isalnum())
            print(b' '.isalnum())
            print(b''.isalnum())
            print(b'/@. test'.isalnum())
            print(b'\x46\x55\x43\x4B'.isalnum())
        """)

    def test_isalpha(self):
        self.assertCodeExecution("""
            print(b'testalpha'.isalpha())
            print(b'TestAlpha'.isalpha())
            print(b'test alpha'.isalpha())
            print(b'666'.isalpha())
            print(b'66.6'.isalpha())
            print(b' '.isalpha())
            print(b''.isalpha())
            print(b'/@. test'.isalpha())
            print(b'\x46\x55\x43\x4B'.isalpha())
        """)

    def test_isdigit(self):
        self.assertCodeExecution("""
            print(b'testdigit'.isdigit())
            print(b'TestDigit'.isdigit())
            print(b'test digit'.isdigit())
            print(b'666'.isdigit())
            print(b'66.6'.isdigit())
            print(b' '.isdigit())
            print(b''.isdigit())
            print(b'/@. test'.isdigit())
            print(b'\x46\x55\x43\x4B'.isdigit())
        """)

    def test_center(self):
        self.assertCodeExecution("""
            print(b'pybee'.center(12))
            print(b'pybee'.center(13))
            print(b'pybee'.center(2))
            print(b'pybee'.center(2, b'a'))
            print(b'pybee'.center(12, b'a'))
            print(b'pybee'.center(13, b'a'))
            print(b'pybee'.center(-5))
            print(b''.center(5))
            print(b'pybee'.center(True, b'a'))
            print(b'pybee'.center(True, bytearray(b'a')))
        """)
        self.assertCodeExecution("""
            print(b'pybee'.center('5'))
        """, exits_early=True)
        self.assertCodeExecution("""
            print(b'pybee'.center(12, b'as'))
        """, exits_early=True)
        self.assertCodeExecution("""
            print(b'pybee'.center(12, 'a'))
        """, exits_early=True)

    def test_upper(self):
        self.assertCodeExecution("""
            print(b'testupper'.upper())
            print(b'TestUpper'.upper())
            print(b'test upper'.upper())
            print(b'666'.upper())
            print(b' '.upper())
            print(b''.upper())
            print(b'/@. test'.upper())
            print(b'\x46\x55\x43\x4B'.upper())
        """)

    def test_lower(self):
        self.assertCodeExecution("""
            print(b"abc".lower())
            print(b"HELLO WORLD!".lower())
            print(b"hElLO wOrLd".lower())
            print(b"[Hello] World".lower())
            """)

    def test_swapcase(self):
        self.assertCodeExecution("""
            print(b"abc".swapcase())
            print(b"ABC".swapcase())
            print(b"HELLO WORLD!".swapcase())
            print(b"hElLO wOrLd".swapcase())
            print(b"[Hello] World".swapcase())
            """)

    def test_isspace(self):
        self.assertCodeExecution("""
            print(b'testisspace'.isspace())
            print(b'test isspace'.isspace())
            print(b' '.isspace())
            print(b''.isspace())
            print(b' \x46'.isspace())
            print(b'   \t\t'.isspace())
            print(b' \x0b'.isspace())
            print(b' \f'.isspace())
            print(b' \\n'.isspace())
            print(b' \\r'.isspace())
        """)

    def test_endswith(self):
        self.assertCodeExecution("""
            print(b"abc".endswith(b"c"))
            print(b"abc".endswith(b"bc"))
            print(b"abc".endswith(b"d"))
            print(b"".endswith(b"a"))
            print(b"abc".endswith(b""))
            print(b"abcde".endswith(b"de"))
            print(b"abcde".endswith(b"de", 2))
            print(b"abcde".endswith(b"de", 4))
            print(b"abcde".endswith(b"bc", 0, 3))
            print(b"abcde".endswith(b"abc", 0, 3))
            print(b"abcde".endswith(b"abc", 0, 4))
            print(b"abcde".endswith(b"abc", 1, 3))
            print(b"abcde".endswith(b"abc", 1, 4))
            print(b"abcde".endswith(b"abc", -1, 4))
            print(b"abcde".endswith(b"abc", 1, -1))
            print(b"abcde".endswith(b"abc", -6, -2))
            print(b"abcde".endswith((b"abc",)))
            print(b"abcde".endswith((b"abc", b"de")))
            print(b"abcde".endswith((b"abc", b"de", b"c")))
            print(b"abcde".endswith((b"de", b"d"), -4))
            print(b"abcde".endswith((b"de", b"d"), -4, 0))
            print(b"abcde".endswith((b"de", b"d"), -4, -1))
            print(b"abcde".endswith((b"da", b"aaa"), -4))
        """)

    def test_startswith(self):
        self.assertCodeExecution("""
            print(b"abc".startswith(b"a"))
            print(b"abc".startswith(b"bc"))
            print(b"abc".startswith(b"ab"))
            print(b"abc".startswith(b"d"))
            print(b"".startswith(b"a"))
            print(b"abc".startswith(b""))
            print(b"abcde".startswith(b"ab"))
            print(b"abcde".startswith(b"de", 3))
            print(b"abcde".startswith(b"abc", 3))
            print(b"abcde".startswith(b"de", 2))
            print(b"abcde".startswith(b"bc", 1, 7))
            print(b"abcde".startswith(b"abc", 0, 3))
            print(b"abcde".startswith(b"abc", 0, 4))
            print(b"abcde".startswith(b"abc", -10, 4))
            print(b"abcde".startswith(b"abc", -5, 4))
            print(b"abcde".startswith(b"abc", -4, 4))
            print(b"abcde".startswith(b"abc", 1, -1))
            print(b"abcde".startswith(b"abc", -6, -2))
            print(b"abcde".startswith((b"abc",)))
            print(b"abcde".startswith((b"abc", b"de")))
            print(b"abcde".startswith((b"de",)))
            print(b"abcde".startswith((b"de", b"c")))
            print(b"abcde".startswith((b"de", b"c", b"b", b"ab")))
            print(b"abcde".startswith((b"de", b"d"), -2))
            print(b"abcde".startswith((b"de", b"d"), -2, 0))
            print(b"abcde".startswith((b"de"), -2))
            print(b"abcde".startswith((b"de", b"d"), -2, -1))
            print(b"abcde".startswith((b"da", b"aaa"), -4))
        """)

    def test_strip(self):
        self.assertCodeExecution(r"""
            print(b"abcde".lstrip())
            print(b"      abcde".lstrip())
            print(b"\n   \t  abcde".lstrip())
            print(b"abcde".rstrip())
            print(b"abcde      ".rstrip())
            print(b"abcde   \t  \n".rstrip())
            print(b"abcde".strip())
            print(b"abcde      ".strip())
            print(b"    abcde   \t  \n".strip())
            print(b"".strip())
            print(b" \n".strip())
        """)

    def test_title(self):
        self.assertCodeExecution(r"""
            print(b"".title())
            print(b"abcd".title())
            print(b"NOT".title())
            print(b"coca cola".title())
            print(b"they are from UK, are they not?".title())
            print(b'/@.'.title())
            print(b'\x46\x55\x43\x4B'.title())
            print(b"py.bee".title())
        """)

    def test_istitle(self):
        self.assertCodeExecution(r"""
            print(b"".istitle())
            print(b"abcd".istitle())
            print(b"NOT".istitle())
            print(b"coca cola".istitle())
            print(b"they are from UK, are they not?".istitle())
            print(b'/@.'.istitle())
            print(b'\x46\x55\x43\x4B'.istitle())
            print(b"py.bee".title())
        """)


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

    is_flakey = [
        'test_modulo_dict',
    ]
