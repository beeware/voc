from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class ReversedTests(TranspileTestCase):
    pass


class BuiltinReversedFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["reversed"]

    not_implemented = [
        'test_range',
    ]
