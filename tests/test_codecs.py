import codecs
import unittest

from voc.java import mutf_8


codecs.register(mutf_8.search_function)

try:
    # For some reason, Debian feels a need to strip out the test module
    # from packaged versions of Python. It can be manually installed
    # with:
    #   apt-get install libpython3.4-testsuite
    # but if that library hasn't been installed, we can vendor in the
    # required parts.
    from test.test_codecs import ReadTest
except ImportError:
    import io

    class Queue(object):
        """
        queue: write bytes at one end, read bytes from the other end
        """
        def __init__(self, buffer):
            self._buffer = buffer

        def write(self, chars):
            self._buffer += chars

        def read(self, size=-1):
            if size < 0:
                s = self._buffer
                self._buffer = self._buffer[:0]  # make empty
                return s
            else:
                s = self._buffer[:size]
                self._buffer = self._buffer[size:]
                return s

    class MixInCheckStateHandling:
        def check_state_handling_decode(self, encoding, u, s):
            for i in range(len(s)+1):
                d = codecs.getincrementaldecoder(encoding)()
                part1 = d.decode(s[:i])
                state = d.getstate()
                self.assertIsInstance(state[1], int)
                # Check that the condition stated in the documentation for
                # IncrementalDecoder.getstate() holds
                if not state[1]:
                    # reset decoder to the default state without anything buffered
                    d.setstate((state[0][:0], 0))
                    # Feeding the previous input may not produce any output
                    self.assertTrue(not d.decode(state[0]))
                    # The decoder must return to the same state
                    self.assertEqual(state, d.getstate())
                # Create a new decoder and set it to the state
                # we extracted from the old one
                d = codecs.getincrementaldecoder(encoding)()
                d.setstate(state)
                part2 = d.decode(s[i:], True)
                self.assertEqual(u, part1+part2)

        def check_state_handling_encode(self, encoding, u, s):
            for i in range(len(u)+1):
                d = codecs.getincrementalencoder(encoding)()
                part1 = d.encode(u[:i])
                state = d.getstate()
                d = codecs.getincrementalencoder(encoding)()
                d.setstate(state)
                part2 = d.encode(u[i:], True)
                self.assertEqual(s, part1+part2)

    class ReadTest(MixInCheckStateHandling):
        def check_partial(self, input, partialresults):
            # get a StreamReader for the encoding and feed the bytestring version
            # of input to the reader byte by byte. Read everything available from
            # the StreamReader and check that the results equal the appropriate
            # entries from partialresults.
            q = Queue(b"")
            r = codecs.getreader(self.encoding)(q)
            result = ""
            for (c, partialresult) in zip(input.encode(self.encoding), partialresults):
                q.write(bytes([c]))
                result += r.read()
                self.assertEqual(result, partialresult)
            # check that there's nothing left in the buffers
            self.assertEqual(r.read(), "")
            self.assertEqual(r.bytebuffer, b"")

            # do the check again, this time using an incremental decoder
            d = codecs.getincrementaldecoder(self.encoding)()
            result = ""
            for (c, partialresult) in zip(input.encode(self.encoding), partialresults):
                result += d.decode(bytes([c]))
                self.assertEqual(result, partialresult)
            # check that there's nothing left in the buffers
            self.assertEqual(d.decode(b"", True), "")
            self.assertEqual(d.buffer, b"")

            # Check whether the reset method works properly
            d.reset()
            result = ""
            for (c, partialresult) in zip(input.encode(self.encoding), partialresults):
                result += d.decode(bytes([c]))
                self.assertEqual(result, partialresult)
            # check that there's nothing left in the buffers
            self.assertEqual(d.decode(b"", True), "")
            self.assertEqual(d.buffer, b"")

            # check iterdecode()
            encoded = input.encode(self.encoding)
            self.assertEqual(
                input,
                "".join(codecs.iterdecode([bytes([c]) for c in encoded], self.encoding))
            )

        def test_readline(self):
            def getreader(input):
                stream = io.BytesIO(input.encode(self.encoding))
                return codecs.getreader(self.encoding)(stream)

            def readalllines(input, keepends=True, size=None):
                reader = getreader(input)
                lines = []
                while True:
                    line = reader.readline(size=size, keepends=keepends)
                    if not line:
                        break
                    lines.append(line)
                return "|".join(lines)

            s = "foo\nbar\r\nbaz\rspam\u2028eggs"
            sexpected = "foo\n|bar\r\n|baz\r|spam\u2028|eggs"
            sexpectednoends = "foo|bar|baz|spam|eggs"
            self.assertEqual(readalllines(s, True), sexpected)
            self.assertEqual(readalllines(s, False), sexpectednoends)
            self.assertEqual(readalllines(s, True, 10), sexpected)
            self.assertEqual(readalllines(s, False, 10), sexpectednoends)

            lineends = ("\n", "\r\n", "\r", "\u2028")
            # Test long lines (multiple calls to read() in readline())
            vw = []
            vwo = []
            for (i, lineend) in enumerate(lineends):
                vw.append((i*200+200)*"\u3042" + lineend)
                vwo.append((i*200+200)*"\u3042")
            self.assertEqual(readalllines("".join(vw), True), "|".join(vw))
            self.assertEqual(readalllines("".join(vw), False), "|".join(vwo))

            # Test lines where the first read might end with \r, so the
            # reader has to look ahead whether this is a lone \r or a \r\n
            for size in range(80):
                for lineend in lineends:
                    s = 10*(size*"a" + lineend + "xxx\n")
                    reader = getreader(s)
                    for i in range(10):
                        self.assertEqual(
                            reader.readline(keepends=True),
                            size*"a" + lineend,
                        )
                        self.assertEqual(
                            reader.readline(keepends=True),
                            "xxx\n",
                        )
                    reader = getreader(s)
                    for i in range(10):
                        self.assertEqual(
                            reader.readline(keepends=False),
                            size*"a",
                        )
                        self.assertEqual(
                            reader.readline(keepends=False),
                            "xxx",
                        )

        def test_mixed_readline_and_read(self):
            lines = ["Humpty Dumpty sat on a wall,\n",
                     "Humpty Dumpty had a great fall.\r\n",
                     "All the king's horses and all the king's men\r",
                     "Couldn't put Humpty together again."]
            data = ''.join(lines)

            def getreader():
                stream = io.BytesIO(data.encode(self.encoding))
                return codecs.getreader(self.encoding)(stream)

            # Issue #8260: Test readline() followed by read()
            f = getreader()
            self.assertEqual(f.readline(), lines[0])
            self.assertEqual(f.read(), ''.join(lines[1:]))
            self.assertEqual(f.read(), '')

            # Issue #16636: Test readline() followed by readlines()
            f = getreader()
            self.assertEqual(f.readline(), lines[0])
            self.assertEqual(f.readlines(), lines[1:])
            self.assertEqual(f.read(), '')

            # Test read() followed by read()
            f = getreader()
            self.assertEqual(f.read(size=40, chars=5), data[:5])
            self.assertEqual(f.read(), data[5:])
            self.assertEqual(f.read(), '')

            # Issue #12446: Test read() followed by readlines()
            f = getreader()
            self.assertEqual(f.read(size=40, chars=5), data[:5])
            self.assertEqual(f.readlines(), [lines[0][5:]] + lines[1:])
            self.assertEqual(f.read(), '')

        def test_bug1175396(self):
            s = [
                '<%!--===================================================\r\n',
                '    BLOG index page: show recent articles,\r\n',
                '    today\'s articles, or articles of a specific date.\r\n',
                '========================================================--%>\r\n',
                '<%@inputencoding="ISO-8859-1"%>\r\n',
                '<%@pagetemplate=TEMPLATE.y%>\r\n',
                '<%@import=import frog.util, frog%>\r\n',
                '<%@import=import frog.objects%>\r\n',
                '<%@import=from frog.storageerrors import StorageError%>\r\n',
                '<%\r\n',
                '\r\n',
                'import logging\r\n',
                'log=logging.getLogger("Snakelets.logger")\r\n',
                '\r\n',
                '\r\n',
                'user=self.SessionCtx.user\r\n',
                'storageEngine=self.SessionCtx.storageEngine\r\n',
                '\r\n',
                '\r\n',
                'def readArticlesFromDate(date, count=None):\r\n',
                '    entryids=storageEngine.listBlogEntries(date)\r\n',
                '    entryids.reverse() # descending\r\n',
                '    if count:\r\n',
                '        entryids=entryids[:count]\r\n',
                '    try:\r\n',
                '        return [ frog.objects.BlogEntry.load(storageEngine, date, Id) for Id in entryids ]\r\n',
                '    except StorageError,x:\r\n',
                '        log.error("Error loading articles: "+str(x))\r\n',
                '        self.abort("cannot load articles")\r\n',
                '\r\n',
                'showdate=None\r\n',
                '\r\n',
                'arg=self.Request.getArg()\r\n',
                'if arg=="today":\r\n',
                '    #-------------------- TODAY\'S ARTICLES\r\n',
                '    self.write("<h2>Today\'s articles</h2>")\r\n',
                '    showdate = frog.util.isodatestr() \r\n',
                '    entries = readArticlesFromDate(showdate)\r\n',
                'elif arg=="active":\r\n',
                '    #-------------------- ACTIVE ARTICLES redirect\r\n',
                '    self.Yredirect("active.y")\r\n',
                'elif arg=="login":\r\n',
                '    #-------------------- LOGIN PAGE redirect\r\n',
                '    self.Yredirect("login.y")\r\n',
                'elif arg=="date":\r\n',
                '    #-------------------- ARTICLES OF A SPECIFIC DATE\r\n',
                '    showdate = self.Request.getParameter("date")\r\n',
                '    self.write("<h2>Articles written on %s</h2>"% frog.util.mediumdatestr(showdate))\r\n',
                '    entries = readArticlesFromDate(showdate)\r\n',
                'else:\r\n',
                '    #-------------------- RECENT ARTICLES\r\n',
                '    self.write("<h2>Recent articles</h2>")\r\n',
                '    dates=storageEngine.listBlogEntryDates()\r\n',
                '    if dates:\r\n',
                '        entries=[]\r\n',
                '        SHOWAMOUNT=10\r\n',
                '        for showdate in dates:\r\n',
                '            entries.extend( readArticlesFromDate(showdate, SHOWAMOUNT-len(entries)) )\r\n',
                '            if len(entries)>=SHOWAMOUNT:\r\n',
                '                break\r\n',
                '                \r\n',
            ]
            stream = io.BytesIO("".join(s).encode(self.encoding))
            reader = codecs.getreader(self.encoding)(stream)
            for (i, line) in enumerate(reader):
                self.assertEqual(line, s[i])

        def test_readlinequeue(self):
            q = Queue(b"")
            writer = codecs.getwriter(self.encoding)(q)
            reader = codecs.getreader(self.encoding)(q)

            # No lineends
            writer.write("foo\r")
            self.assertEqual(reader.readline(keepends=False), "foo")
            writer.write("\nbar\r")
            self.assertEqual(reader.readline(keepends=False), "")
            self.assertEqual(reader.readline(keepends=False), "bar")
            writer.write("baz")
            self.assertEqual(reader.readline(keepends=False), "baz")
            self.assertEqual(reader.readline(keepends=False), "")

            # Lineends
            writer.write("foo\r")
            self.assertEqual(reader.readline(keepends=True), "foo\r")
            writer.write("\nbar\r")
            self.assertEqual(reader.readline(keepends=True), "\n")
            self.assertEqual(reader.readline(keepends=True), "bar\r")
            writer.write("baz")
            self.assertEqual(reader.readline(keepends=True), "baz")
            self.assertEqual(reader.readline(keepends=True), "")
            writer.write("foo\r\n")
            self.assertEqual(reader.readline(keepends=True), "foo\r\n")

        def test_bug1098990_a(self):
            s1 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\r\n"
            s2 = "offending line: ladfj askldfj klasdj fskla dfzaskdj fasklfj laskd fjasklfzzzzaa%whereisthis!!!\r\n"
            s3 = "next line.\r\n"

            s = (s1+s2+s3).encode(self.encoding)
            stream = io.BytesIO(s)
            reader = codecs.getreader(self.encoding)(stream)
            self.assertEqual(reader.readline(), s1)
            self.assertEqual(reader.readline(), s2)
            self.assertEqual(reader.readline(), s3)
            self.assertEqual(reader.readline(), "")

        def test_bug1098990_b(self):
            s1 = "aaaaaaaaaaaaaaaaaaaaaaaa\r\n"
            s2 = "bbbbbbbbbbbbbbbbbbbbbbbb\r\n"
            s3 = "stillokay:bbbbxx\r\n"
            s4 = "broken!!!!badbad\r\n"
            s5 = "againokay.\r\n"

            s = (s1+s2+s3+s4+s5).encode(self.encoding)
            stream = io.BytesIO(s)
            reader = codecs.getreader(self.encoding)(stream)
            self.assertEqual(reader.readline(), s1)
            self.assertEqual(reader.readline(), s2)
            self.assertEqual(reader.readline(), s3)
            self.assertEqual(reader.readline(), s4)
            self.assertEqual(reader.readline(), s5)
            self.assertEqual(reader.readline(), "")

        ill_formed_sequence_replace = "\ufffd"

        def test_lone_surrogates(self):
            self.assertRaises(UnicodeEncodeError, "\ud800".encode, self.encoding)
            self.assertEqual("[\uDC80]".encode(self.encoding, "backslashreplace"),
                             "[\\udc80]".encode(self.encoding))
            self.assertEqual("[\uDC80]".encode(self.encoding, "namereplace"),
                             "[\\udc80]".encode(self.encoding))
            self.assertEqual("[\uDC80]".encode(self.encoding, "xmlcharrefreplace"),
                             "[&#56448;]".encode(self.encoding))
            self.assertEqual("[\uDC80]".encode(self.encoding, "ignore"),
                             "[]".encode(self.encoding))
            self.assertEqual("[\uDC80]".encode(self.encoding, "replace"),
                             "[?]".encode(self.encoding))

            # sequential surrogate characters
            self.assertEqual("[\uD800\uDC80]".encode(self.encoding, "ignore"),
                             "[]".encode(self.encoding))
            self.assertEqual("[\uD800\uDC80]".encode(self.encoding, "replace"),
                             "[??]".encode(self.encoding))

            bom = "".encode(self.encoding)
            for before, after in [("\U00010fff", "A"), ("[", "]"),
                                  ("A", "\U00010fff")]:
                before_sequence = before.encode(self.encoding)[len(bom):]
                after_sequence = after.encode(self.encoding)[len(bom):]
                test_string = before + "\uDC80" + after
                test_sequence = (bom + before_sequence +
                                 self.ill_formed_sequence + after_sequence)
                self.assertRaises(UnicodeDecodeError, test_sequence.decode,
                                  self.encoding)
                self.assertEqual(test_string.encode(self.encoding,
                                                    "surrogatepass"),
                                 test_sequence)
                self.assertEqual(test_sequence.decode(self.encoding,
                                                      "surrogatepass"),
                                 test_string)
                self.assertEqual(test_sequence.decode(self.encoding, "ignore"),
                                 before + after)
                self.assertEqual(test_sequence.decode(self.encoding, "replace"),
                                 before + self.ill_formed_sequence_replace + after)
                backslashreplace = ''.join('\\x%02x' % b
                                           for b in self.ill_formed_sequence)
                self.assertEqual(test_sequence.decode(self.encoding, "backslashreplace"),
                                 before + backslashreplace + after)


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
        self.assertEqual(
            'Hot \U00010400iggity'.encode(self.encoding),
            b'Hot \xed\xa0\x81\xed\xb0\x80iggity',
            'no match'
        )
        self.assertEqual(
            'How \u0205ccentric'.encode(self.encoding),
            b'How \xc8\x85ccentric'
        )

        self.assertEqual(
            b'Hot \xed\xa0\x81\xed\xb0\x80iggity'.decode(self.encoding),
            'Hot \U00010400iggity',
            'no match'
        )
        self.assertEqual(
            b'How \xc8\x85ccentric'.decode(self.encoding),
            'How \u0205ccentric'
        )
