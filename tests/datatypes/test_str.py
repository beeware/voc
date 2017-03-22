from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class StrTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = "Hello, world"
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_iscase(self):
        self.assertCodeExecution("""
            for s in ['hello, World!', 'HELLO, WORLD.', 'ello? world', '']:
                print(s.islower())
                print(s.isupper())
            """)

    def test_isdigit(self):
        self.assertCodeExecution("""
            for s in ['112358132134', '3.14159', '12312344df', '']:
                print(s.isdigit())
            """)

    def test_isspace(self):
        self.assertCodeExecution("""
            for s in ['''  \t \r''', ' ', '\t\tnope\t\t', '']:
                print(s.isspace())
            """)

    def test_isalnum(self):
        self.assertCodeExecution("""
            for word in ["", "12", "abc", "abc12", "\u00c4", "\x41", "a@g", "äÆ",
            "12.2", "'Hi'", "Hello!!", "HELLO", "V0c", "A A"]:
                print(word.isalnum())
            """)

    def test_isalpha(self):
        self.assertCodeExecution("""
            for s in ['Hello World', 'hello wORLd.', 'Hello world.', '', 'hello1',
            'this', 'this is string example....wow!!!', 'átomo', 'CasesLikeTheseWithoutSpaces']:
                print(s.isalpha())
            """)

    def test_isdecimal(self):
        self.assertCodeExecution("""
            for word in ["", "12", "abc", "abc12", "\u0037", "\x31", "0101b",
            "-13", "12.2", "'7'"]:
                print(word.isdecimal())
            """)

    def test_istitle(self):
        self.assertCodeExecution("""
            for s in ['Hello World', 'hello wORLd.', 'Hello world.', '']:
                print(s.istitle())
            """)

    def test_join(self):
        self.assertCodeExecution("""
            print(','.join(None))
            """, exits_early=True)
        self.assertCodeExecution("""
            print(','.join(12))
            """, exits_early=True)
        self.assertCodeExecution("""
            print(','.join(['1', '2', '3']))
            print(','.join([]))
            print('asdf'.join(','))
            """)

    def test_endswith(self):
        self.assertCodeExecution("""
            s = "abracadabra"
            suffix = "abra"
            print(s.endswith(suffix))
            """)

        self.assertCodeExecution("""
            s = "abracadabra"
            suffix = "ABRA"
            print(s.endswith(suffix))
            """)

        self.assertCodeExecution("""
            s = "ABRACADABRA"
            suffix = "abra"
            print(s.endswith(suffix))
            """)

        self.assertCodeExecution("""
            print('abracadabra'.endswith('abra',0,5))
            """)

        self.assertCodeExecution("""
            s = "ABRACADABRA"
            suffix = ""
            print(s.endswith(suffix,3))
            """)

    def test_startswith(self):
        self.assertCodeExecution("""
            s = "abracadabra"
            suffix = "abra"
            print(s.startswith(suffix))
            """)

        self.assertCodeExecution("""
            s = "abracadabra"
            suffix = "ABRA"
            print(s.startswith(suffix))
            """)

        self.assertCodeExecution("""
            s = "ABRACADABRA"
            suffix = "abra"
            print(s.startswith(suffix))
            """)

        self.assertCodeExecution("""
            print('abracadabra'.startswith('abra',0,5))
            """)

        self.assertCodeExecution("""
            s = "ABRACADABRA"
            suffix = ""
            print(s.startswith(suffix,3))
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = "Hello, world"
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)

    def test_getitem(self):
        # Simple positive index
        self.assertCodeExecution("""
            x = "12345"
            print(x[2])
            """)

        # Simple negative index
        self.assertCodeExecution("""
            x = "12345"
            print(x[-2])
            """)

        # Positive index out of range
        self.assertCodeExecution("""
            x = "12345"
            try:
                print(x[10])
            except IndexError as err:
                print(err)
            """)

        # Negative index out of range
        self.assertCodeExecution("""
            x = "12345"
            try:
                print(x[-10])
            except IndexError as err:
                print(err)
            """)

    def test_slice(self):
        # Full slice
        self.assertCodeExecution("""
            x = "12345"
            print(x[:])
            """)

        # Left bound slice
        self.assertCodeExecution("""
            x = "12345"
            print(x[1:])
            """)

        # Right bound slice
        self.assertCodeExecution("""
            x = "12345"
            print(x[:4])
            """)

        # Slice bound in both directions
        self.assertCodeExecution("""
            x = "12345"
            print(x[1:4])
            """)

        # Slice bound in both directions with end out of bounds
        self.assertCodeExecution("""
            x = "12345"
            print(x[1:6])
            """)

        # Slice bound in both directions with start out of bounds
        self.assertCodeExecution("""
            x = "12345"
            print(x[6:7])
            """)

        # Slice bound in both directions with start larger than end
        self.assertCodeExecution("""
            x = "12345"
            print(x[4:1])
            """)

        # Slice bound in both directions with start and end out of bounds
        self.assertCodeExecution("""
            x = "12345"
            print(x[-10:10])
            """)

    def test_case_changes(self):
        self.assertCodeExecution("""
            for s in ['hello, world', 'HEllo, WORLD', 'átomo', '']:
                print(s.capitalize())
                print(s.lower())
                print(s.swapcase())
                print(s.title())
                print(s.upper())
            """)

    def test_split(self):
        self.assertCodeExecution("""
            for s in ['hello, world', 'HEllo, WORLD', 'átomo', '']:
                print(s.split())
                print(s.split("o"))
                print(s.split(maxsplit=2))
                print(s.split("l",maxsplit=0))
                try:
                    print(s.split(5))
                except TypeError as err:
                    print(err)
            """)

    def test_index(self):
        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.index('hell'))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            try:
                print(s.index('world'))
            except ValueError as err:
                print(err)
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.index('hell', 1))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            try:
                print(s.index('hell', 1, 3))
            except ValueError as err:
                print(err)
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.index('hell', 1, 100))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            try:
                print(s.index('hell', 1, -1))
            except ValueError as err:
                print(err)
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.index('hell', -4))
            """)

    def test_count(self):
        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('e'))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('a'))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('ll'))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('ll', 3))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('ll', 3, 4))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('ll', 0, 4))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('ll', 0, 100))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('hell', 1, -1))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('hell', -4))
            """)

    def test_find(self):
        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.find('hell'))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.find('world'))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.find('hell', 1))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.find('hell', 1, 3))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.find('hell', 1, 100))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.find('hell', 1, -1))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.find('hell', -4))
            """)

    def test_expand(self):
        self.assertCodeExecution("""
            print('\\t'.expandtabs())
            print('a\\t'.expandtabs())
            print('aa\\t'.expandtabs())
            print('aaa\\t'.expandtabs())
            print('aaaaaaaa\\t'.expandtabs())
            print('a\\naa\\t'.expandtabs())
            print('\\t'.expandtabs(3))
            print('a\\t'.expandtabs(3))
            print('aa\\t'.expandtabs(7))
            print('aaa\\t'.expandtabs(4))
            print('aaaaaaaa\\t'.expandtabs(4))
            print('a\\naa\\t'.expandtabs(4))
            """)

    def test_title(self):
        self.assertCodeExecution("""
            s = ' foo  bar    baz '
            print(s.title())
        """)

    def test_len(self):
        self.assertCodeExecution("""
            s = ' foo  bar    baz '
            print(len(s))
        """)

    def test_center(self):
        # test ok
        self.assertCodeExecution("""
            s = "abc"
            print(s.center(10, "-"))
            print(s.center(10))
            print(s.center(2,"-"))
            print(s.center(True,"-"))
            try:
                print(s.center(10,"-*"))
            except TypeError as err:
                print(err)
            s = 123
            try:
                print(s.center(10,"-"))
            except AttributeError as err:
                print(err)
            """)

    def test_ljust(self):
        self.assertCodeExecution("""
            s = "abc"
            print(s.ljust(5, "P"))
            print(s.ljust(2))
            print(s.ljust(15, "0"))
            print(s.ljust(20, "ã"))
            try:
                print(s.ljust(5, b'_'))
            except TypeError as err:
                print(TypeError)
            try:
                print(s.ljust(5.0, "P"))
            except TypeError as err:
                print(err)
                """)

    def test_partition(self):
        self.assertCodeExecution("""
            s = "foobar"
            print(s.partition("ob"))
            print(s.partition("o"))
            print(s.partition("f"))
            print(s.partition("r"))
            print(s.partition("x"))
            try:
                print(s.partition(""))
            except ValueError as err:
                print(err)
            """)

    def test_lstrip(self):
        self.assertCodeExecution("""
            str = "gggfoo"
            print(str.lstrip('g'))
            print(str.lstrip('h'))
            str = "   foo"
            print(str.lstrip())
            print("foot".lstrip("foobar"))
            try:
                print("kk".lstrip(6))
            except TypeError as err:
                print(err)
            """)

    def test_rstrip(self):
        self.assertCodeExecution("""
            str = "fooggg"
            print(str.rstrip('g'))
            print(str.rstrip('h'))
            str = "foo   "
            print(str.rstrip())
            print("boo".rstrip("foo"))
            try:
                print("kk".lstrip(6))
            except TypeError as err:
                print(err)
            """)

    def test_rfind(self):
        # test cases to generate outout
        self.assertCodeExecution("""
            st="a good cook could cook good"
            print(st.rfind('cook'))
            print(st.rfind('cook',10))
            print(st.rfind('book',1,10))
            """)

        # test cases with indices more than the string length
        self.assertCodeExecution("""
            st="a good cook could cook good"
            print(st.rfind('cook',100,200))
            print(st.rfind('cook',1000))
            print(st.rfind('cook',-1))
            """)

        # test cases with empty find string
        self.assertCodeExecution("""
            st="a good cook could cook good"
            try:
                print(st.rfind())
            except TypeError as err:
                print(err)
            """)

    def test_rindex(self):
        # test cases to generate outout
        self.assertCodeExecution("""
            st="a good cook could cook good"
            try:
                print(st.rindex('cook'))
            except ValueError as err:
                print(err)
            try:
                print(st.rindex('cook',10))
            except ValueError as err:
                print(err)
            try:
                print(st.rindex('cook',1,10))
            except ValueError as err:
                print(err)
            """)

        # test cases with indices more than the string length
        self.assertCodeExecution("""
            st="a good cook could cook good"
            try:
                print(st.rindex('cook',100,200))
            except ValueError as err:
                print(err)
            try:
                print(st.rindex('cook',1000))
            except ValueError as err:
                print(err)
            try:
                print(st.rindex('cook',-1))
            except ValueError as err:
                print(err)
            """)

        # test cases with empty find string
        self.assertCodeExecution("""
            st="a good cook could cook good"
            try:
                print(st.rindex())
            except TypeError as err:
                print(err)
            """)

    def test_rjust(self):
        # test cases to generate valid outout
        self.assertCodeExecution("""
            st="a good cook could cook good"
            print(st.rjust(100))
            print(st.rjust(100, 'X'))
            print(st.rjust(10, 'X'))

            """)

        # test cases to generate exception
        self.assertCodeExecution("""
            st="a good cook could cook good"
            try:
                print(st.rjust(-20, 'X'))
            except TypeError as err:
                print(err)
            try:
                print(st.rjust(100, 'cook'))
            except TypeError as err:
                print(err)
            try:
                print(st.rjust())
            except TypeError as err:
                print(err)
            try:
                print(st.rjust(20.5, 'X'))
            except TypeError as err:
                print(err)
            """)


class UnaryStrOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'str'

    not_implemented = [
    ]


class BinaryStrOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'str'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',

        'test_direct_eq_bytes',
        'test_direct_ge_bytes',
        'test_direct_gt_bytes',
        'test_direct_le_bytes',
        'test_direct_lt_bytes',
        'test_direct_ne_bytes',

        'test_direct_eq_frozenset',
        'test_direct_ge_frozenset',
        'test_direct_gt_frozenset',
        'test_direct_le_frozenset',
        'test_direct_lt_frozenset',
        'test_direct_ne_frozenset',

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

        'test_modulo_bool',
        'test_modulo_bytes',
        'test_modulo_bytearray',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_slice',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_str',
        'test_modulo_tuple',

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

        'test_subscr_bool',
        'test_subscr_class',
        'test_subscr_frozenset',
        'test_subscr_slice',

        'test_subtract_class',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
    ]


class InplaceStrOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'str'

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

        'test_modulo_bool',
        'test_modulo_bytes',
        'test_modulo_bytearray',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_slice',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_range',
        'test_modulo_set',
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
