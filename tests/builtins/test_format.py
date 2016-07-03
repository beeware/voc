from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class FormatTests(TranspileTestCase):
    pass


class BuiltinFormatFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["format"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_frozenset',
        'test_slice',
    ]
