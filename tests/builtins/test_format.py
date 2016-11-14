from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class FormatTests(TranspileTestCase):
    pass


class BuiltinFormatFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["format"]

    not_implemented = [
        'test_class',
        'test_complex',
        'test_frozenset',
        'test_slice',
    ]
