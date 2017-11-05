
from unittest import expectedFailure

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
        self.assertCodeExecution(r"""
            for s in ['\x1f \v \f \n \t \r', ' ', '\x85\xa0', '\u2007', '\u202f',
            '\u180e', '\t\tnope\t\t', '']:
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
        self.assertCodeExecution(r"""
            print("".istitle())
            print("abcd".istitle())
            print("NOT".istitle())
            print("coca cola".istitle())
            print("they are from UK, are they not?".istitle())
            print("/@.".istitle())
            print("\u00c4".istitle())
            print("\x41".istitle())
            print("py.bee".istitle())
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
        self.assertCodeExecution(r"""
            for s in ['\vhello,        world', '\nHEllo, WORLD\f', 'átomo', '']:
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
        self.assertCodeExecution(r"""
            print("".title())
            print("abcd".title())
            print("NOT".title())
            print("coca cola".title())
            print("they are from UK, are they not?".title())
            print("/@.".title())
            print("\u00c4".title())
            print("\x41".title())
            print("py.bee".title())
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
            str = "\t\t   gggfoo "
            print(str.lstrip('h'))
            print(str.lstrip())
            print(str.lstrip(None))
            print(str.lstrip(''))
            print(str.lstrip('\t '))
            print(str.lstrip('\t gf'))
            print(str.lstrip('\t\t   gggfoo '))
            try:
                print(str.lstrip(6))
            except TypeError as err:
                print(err)
            """)

        self.assertCodeExecution("""
            str="abbaccdcbbs"
            print(str.lstrip('ab'))
            str=""
            print(str.lstrip())
            print(str.lstrip('ab'))
            """)

        self.assertCodeExecution(r"""
            str="\u180eabc"
            print(str.lstrip())
            str="\x85abc"
            print(str.lstrip())
            """)

    def test_rstrip(self):
        self.assertCodeExecution("""
            str = " fooggg\t\t   "
            print(str.rstrip('h'))
            print(str.rstrip())
            print(str.rstrip(None))
            print(str.rstrip(''))
            print(str.rstrip('\t '))
            print(str.rstrip('\t og'))
            print(str.rstrip(' fooggg\t\t   '))
            try:
                print(str.rstrip(6))
            except TypeError as err:
                print(err)
            """)

        self.assertCodeExecution("""
            str="abbaccdcbbsabba"
            print(str.rstrip('ab'))
            str=""
            print(str.rstrip())
            print(str.rstrip('ab'))
            """)

        self.assertCodeExecution(r"""
            str="abc\u180e"
            print(str.rstrip())
            str="abc\x85"
            print(str.rstrip())
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

    def test_strip(self):
        self.assertCodeExecution("""
            s = "\t\t   hello "
            try:
                print(s.strip(6))
            except TypeError as e:
                print(e)
            print(s.strip())
            print(s.strip(None))
            print(s.strip(''))
            print(s.strip('a'))
            print(s.strip(' '))
            print(s.strip('\t '))
            print(s.strip('\t ho'))
            print(s.strip('\t hello '))
            """)

        self.assertCodeExecution("""
            str="abbaccdcbbsabba"
            print(str.strip('abs'))
            print(str.strip())
            str=""
            print(str.strip())
            print(str.strip('ab'))
            """)

    def test_casefold(self):
        self.assertCodeExecution("""
            print("ÅAÆΣß".casefold())
            print("ß.nfG".casefold())
            print("HeLlo_worldʃ!".casefold())
            """)

    def test_replace(self):
        self.assertCodeExecution("""
            s="abc abc abc abc abc abcd mm       "
            print(s.replace('','k'))
            print(s.replace(' ','k'))
            print(s.replace(' ','fm'))
            print(s.replace('ab','bc'))
            try:
                print(s.replace(45,'bc'))
            except TypeError as err:
                print(err)
            try:
                print(s.replace('kk',45))
            except TypeError as err:
                print(err)
            """)

    def test_rpartition(self):
        self.assertCodeExecution("""
            st = "Hello World!"
            print(st.rpartition("H"))
            print(st.rpartition(" "))
            print(st.rpartition("l"))
            print(st.rpartition("q"))
            print(st.rpartition("lo"))
            print(st.rpartition("!"))
            print(st.rpartition("ld!"))
            print("voc".rpartition("foobar"))
            print("".rpartition("oi"))
            class str2:
                def __str__(self):
                    return "abc"
            try:
                print(st.rpartition(str2()))
            except TypeError as err:
                print(err)
            try:
                print(st.rpartition(""))
            except ValueError as err:
                print(err)
            try:
                print(st.rpartition(4))
            except TypeError as err:
                print(err)
            try:
                print(st.rpartition(7.8))
            except TypeError as err:
                print(err)
            try:
                print(st.rpartition())
            except TypeError as err:
                print(err)
            """)

    def test_isnumeric(self):
        self.assertCodeExecution("""
        for str_ in ['123', '123.4', 'abc', '', ' ', 'ABCD', 'ABCD ', '12323445',
        '123.', '.12', '1A', 'A1', '!@#', 'A1@#']:
            print(str_.isnumeric())
            """)

    def test_isidentifier(self):
        self.assertCodeExecution("""
        for str_ in ['_sjkd', 'abc', 'ABC', 'b13s', 'foo_bar', 'eÃⱣỉ', 'ÃⱣỉ', "22222", " ", "", "/",
        "4a2a", "*", "ab cd", "!z", "&a", "@", "%"]:
            print(str_, str_.isidentifier())
            """)

    def test_isprintable(self):
        self.assertCodeExecution("""
        for str_ in [chr(i) for i in range(33)] + ['AAA', 'bcd', '1234', 'eÃⱣỉ', 'ÃⱣỉ', '', '\x07' + 'foo', '\u2029']:
            print(str_.isprintable())
            """)

    @expectedFailure
    def test_isprintable_missing_cases(self):
        self.assertCodeExecution(r"""
        tests = ['\u2028']:
        for test in tests:
            print(test.isprintable())
        """)

    def test_repr(self):
        self.assertCodeExecution(r"""
        tests = ["\r\n", "áéíóú", "\u000B", "\u2029", "\\", "'", "\"", "\"'"]
        for test in tests:
            print(repr(test))
        """)

    def test_splitlines(self):
        self.assertCodeExecution(r"""
        str_ = "aaa\nbbb\rccc\r\nddd\n\reee"

        print(str_.splitlines())
        print(str_.splitlines(True))
        print("Don't Panic\n".splitlines())
        print('\n'.splitlines())
        print(''.splitlines())

        s1 = '\r\n\r\n\v\f\x0b\x0c\u2029\x1c\x1d\x1e\x85'
        print(s1.splitlines())
        print(s1.splitlines(True))
        """)


class UnaryStrOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'str'


class BinaryStrOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'str'

    not_implemented = [
        'test_modulo_class',

        'test_subscr_bool',
        'test_subscr_slice',
    ]


class InplaceStrOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'str'

    not_implemented = [
        'test_modulo_class',
    ]
