r"""
This file defines a codec called "mutf-8", or Modified UTF-8. This is the codec
that Java uses as an on-the-wire format for JNI and class files.

The format is a combination of CESU-8, the encoding formed by layering UTF-8 on
top of UTF-16, as well as encoding NUL (codepoint 0) as a two byte sequence.
"""

from __future__ import unicode_literals

import codecs
import re
from encodings import normalize_encoding
from encodings.utf_8 import (
    IncrementalDecoder as UTF8IncrementalDecoder,
    IncrementalEncoder as UTF8IncrementalEncoder,
)

# Match 6-byte CESU-9 sequences
CESU8_RE = re.compile(b'\xed[\xa0-\xaf][\x80-\xbf]\xed[\xb0-\xbf][\x80-\xbf]')


class IncrementalDecoder(UTF8IncrementalDecoder):
    def _buffer_decode(self, input, errors, final):
        pieces = []
        position = 0
        while True:
            # Consume a chunk
            decoded, consumed = self._buffer_decode_chunk(
                input[position:],
                errors,
                final
            )
            # if we consumed nothing, it's probably the end of
            # the stream.
            if consumed == 0:
                break

            # Append the decoded text to the list, and update our position.
            pieces.append(decoded)
            position += consumed

        if final:
            # Check that we've consumed everything.
            assert position == len(input)

        return ''.join(pieces), position

    def _buffer_decode_chunk(self, input, errors, final):
        # CESU-8 sequences start with 0xed
        # Java NULLs start with 0xc0.
        index1 = input.find(b'\xed')
        index2 = input.find(b'\xc0')

        # Set `index` to whichever index comes first.
        if index1 != -1 and index2 != -1:
            index = min(index1, index2)
        elif index1 != -1:
            index = index1
        elif index2 != -1:
            index = index2
        else:
            # None of the marker characters were found, so
            # encode the entire input as normal UTF-8
            return super()._buffer_decode(input, errors, final)

        if index1 == 0:
            # Decode a six-byte CESU-8 sequence
            return self._buffer_decode_surrogates(input, errors, final)
        elif index2 == 0:
            # Decode a Java NULL
            return self._buffer_decode_null(input, errors, final)
        else:
            # Decode the bytes up until the next weird thing as UTF-8.
            # Set final=True because 0xc0 and 0xed don't make sense in the
            # middle of a sequence, in any variant.
            return super()._buffer_decode(input[:index], errors, True)

    def _buffer_decode_null(self, input, errors, final):
        """
        Decode the bytes 0xc0 0x80 as U+0000, like Java does.
        """
        nextbyte = input[1:2]
        if nextbyte == b'':
            if final:
                # We found 0xc0 at the end of the stream, which is an error.
                # Delegate to the superclass method to handle that error.
                return super()._buffer_decode(input, errors, final)
            else:
                # We found 0xc0 and we don't know what comes next, so consume
                # no bytes and wait.
                return '', 0
        elif nextbyte == b'\x80':
            # We found the usual 0xc0 0x80 sequence, so decode it and consume
            # two bytes.
            return '\u0000', 2
        else:
            # We found 0xc0 followed by something else, which is an error.
            # Whatever should happen is equivalent to what happens when the
            # superclass is given just the byte 0xc0, with final=True.
            return super()._buffer_decode(b'\xc0', errors, True)

    def _buffer_decode_surrogates(self, input, errors, final):
        """
        When we have improperly encoded surrogates, we can still see the
        bits that they were meant to represent.
        The surrogates were meant to encode a 20-bit number, to which we
        add 0x10000 to get a codepoint. That 20-bit number now appears in
        this form:
          11101101 1010abcd 10efghij 11101101 1011klmn 10opqrst
        The CESU8_RE above matches byte sequences of this form. Then we need
        to extract the bits and assemble a codepoint number from them.
        """
        if len(input) < 6:
            if final:
                # We found 0xed near the end of the stream, and there aren't
                # six bytes to decode. Delegate to the superclass method to
                # handle it as normal UTF-8. It might be a Hangul character
                # or an error.
                return super()._buffer_decode(input, errors, final)
            else:
                # We found 0xed, the stream isn't over yet, and we don't know
                # enough of the following bytes to decode anything, so consume
                # zero bytes and wait.
                return '', 0
        else:
            if CESU8_RE.match(input):
                # If this is a CESU-8 sequence, do some math to pull out
                # the intended 20-bit value, and consume six bytes.
                bytenums = input[:6]
                codepoint = (
                    ((bytenums[1] & 0x0f) << 16) +
                    ((bytenums[2] & 0x3f) << 10) +
                    ((bytenums[4] & 0x0f) << 6) +
                    (bytenums[5] & 0x3f) +
                    0x10000
                )
                return chr(codepoint), 6
            else:
                # This looked like a CESU-8 sequence, but it wasn't one.
                # 0xed indicates the start of a three-byte sequence, so give
                # three bytes to the superclass to decode as usual -- except
                # for working around the Python 2 discrepancy as before.
                return super()._buffer_decode(input[:3], errors, False)


class IncrementalEncoder(UTF8IncrementalEncoder):
    def encode(self, input, final=False):
        # encode input (taking the buffer into account)
        data = self.buffer + input
        (result, consumed) = self._buffer_encode(data, self.errors, final)
        # keep unencoded input until the next call
        self.buffer = data[consumed:]
        return result

    def _buffer_encode(self, input, errors, final):
        encoded_segments = []
        position = 0
        while True:
            encoded, consumed = self._buffer_encode_codepoint(
                input[position:],
                final
            )
            if consumed == 0:
                # Either there's nothing left to encode, or we need to wait
                # for more input. Either way, we're done for now.
                break

            # Append the encoded text to the list, and update our position.
            encoded_segments.append(encoded)
            position += consumed

        if final:
            # _buffer_decode_chunk must consume all the bytes when `final` is
            # true.
            assert position == len(input)

        return b''.join(encoded_segments), position

    def _buffer_encode_codepoint(self, input, final):
        # Find the next byte position that indicates a variant of UTF-8.
        # CESU-8 sequences always start with 0xed,
        # Java nulls always start with 0xc0.

        index1 = 0
        try:
            while ord(input[index1]) <= 0xffff:
                index1 += 1
        except IndexError:
            index1 = -1
        index2 = input.find('\x00')

        # Set `index` to whichever index comes first.
        if index1 != -1 and index2 != -1:
            index = min(index1, index2)
        elif index1 != -1:
            index = index1
        elif index2 != -1:
            index = index2
        else:
            # No special characters found; encode the remaining
            # input as standard UTF-8
            return codecs.utf_8_encode(input, self.errors)

        if index1 == 0:
            # Encode a six-byte sequence starting with 0xed.
            return bytes(bytearray([
                    0xED,
                    0xA0 | (((ord(input[0]) >> 16) - 1) & 0x0f),
                    0x80 | ((ord(input[0]) >> 10) & 0x3f),
                    0xED,
                    0xB0 | ((ord(input[0]) >> 6) & 0x0f),
                    0x80 | (ord(input[0]) & 0x3f),
                ])), 1
        elif index2 == 0:
            # Encode a two-byte sequence, 0xc0 0x80.
            return b'\xc0\x80', 1
        else:
            # Encode the bytes up until the next weird thing as UTF-8.
            return codecs.utf_8_encode(input[:index], self.errors)


# Everything below here is boilerplate that matches the modules in the
# built-in `encodings` package.
def encode(input, errors='strict', final=True):
    return IncrementalEncoder(errors).encode(input, final=final), len(input)


def decode(input, errors='strict', final=True):
    return IncrementalDecoder(errors).decode(input, final=final), len(input)


class StreamWriter(codecs.StreamWriter):
    def __init__(self, stream, errors='strict', mapping=None):
        super().__init__(stream, errors)
        self.encoder = IncrementalEncoder(errors)

    def encode(self, input, errors='strict'):
        return self.encoder.encode(input, final=False), len(input)


class StreamReader(codecs.StreamReader):
    def __init__(self, stream, errors='strict', mapping=None):
        super().__init__(stream, errors)
        self.decoder = IncrementalDecoder(errors)

    def decode(self, input, errors='strict'):
        return self.decoder.decode(input, final=False), len(input)


# encodings module API

def search_function(encoding):
    if normalize_encoding(encoding) == 'mutf_8':
        return codecs.CodecInfo(
            name='mutf-8',
            encode=encode,
            decode=decode,
            incrementalencoder=IncrementalEncoder,
            incrementaldecoder=IncrementalDecoder,
            streamreader=StreamReader,
            streamwriter=StreamWriter,
        )
    else:
        return None
