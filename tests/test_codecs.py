import codecs
from test.test_codecs import ReadTest
import unittest

from voc.java import mutf_8


codecs.register(mutf_8.search_function)


class MUTF8Test(ReadTest, unittest.TestCase):
    encoding = 'mutf-8'

    def test_decoder_state(self):
        u = "\x00\x7f\x80\xff\u0100\u07ff\u0800\uffff\U0010ffff"
        self.check_state_handling_decode(self.encoding,
                                         u, u.encode(self.encoding))

    def test_lone_surrogates(self):
        self.assertRaises(UnicodeEncodeError, "\ud800".encode, self.encoding)
        self.assertRaises(UnicodeDecodeError, b"\xed\xa0\x80".decode, self.encoding)
        self.assertEqual("[\uDC80]".encode(self.encoding, "backslashreplace"),
                         b'[\\udc80]')
        self.assertEqual("[\uDC80]".encode(self.encoding, "xmlcharrefreplace"),
                         b'[&#56448;]')
        self.assertEqual("[\uDC80]".encode(self.encoding, "surrogateescape"),
                         b'[\x80]')
        self.assertEqual("[\uDC80]".encode(self.encoding, "ignore"),
                         b'[]')
        self.assertEqual("[\uDC80]".encode(self.encoding, "replace"),
                         b'[?]')

    def test_surrogatepass_handler(self):
        self.assertEqual("abc\ud800def".encode(self.encoding, "surrogatepass"),
                         b"abc\xed\xa0\x80def")
        self.assertEqual(b"abc\xed\xa0\x80def".decode(self.encoding, "surrogatepass"),
                         "abc\ud800def")
        self.assertTrue(codecs.lookup_error("surrogatepass"))

    def test_invalid(self):
        for invalid in (
            b'\xC0\x81',
            b'\xC0\xFF',
            b'\xC1\x10',
            b'\xC1\x80',
        ):
            with self.assertRaises(UnicodeDecodeError):
                invalid.decode(self.encoding)

    def test_partial(self):
        self.check_partial(
            "\x00\xff\u07ff\u0800\uffff",
            [
                "",
                "\x00",
                "\x00",
                "\x00\xff",
                "\x00\xff",
                "\x00\xff\u07ff",
                "\x00\xff\u07ff",
                "\x00\xff\u07ff",
                "\x00\xff\u07ff\u0800",
                "\x00\xff\u07ff\u0800",
                "\x00\xff\u07ff\u0800",
                "\x00\xff\u07ff\u0800\uffff",
            ]
        )

    def test_null_byte(self):
        self.assertEqual(b'a\xc0\x80b'.decode(self.encoding), 'a\x00b')
        self.assertEqual('a\x00b'.encode(self.encoding), b'a\xc0\x80b')

    def test_surrogates(self):
        self.assertEqual('Hot \U00010400iggity'.encode(self.encoding), b'Hot \xed\xa0\x81\xed\xb0\x80iggity', 'no match')
        self.assertEqual('How \u0205ccentric'.encode(self.encoding), b'How \xc8\x85ccentric')

        self.assertEqual(b'Hot \xed\xa0\x81\xed\xb0\x80iggity'.decode(self.encoding), 'Hot \U00010400iggity', 'no match')
        self.assertEqual(b'How \xc8\x85ccentric'.decode(self.encoding), 'How \u0205ccentric')
