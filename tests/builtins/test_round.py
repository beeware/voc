from .. utils import TranspileTestCase, BuiltinFunctionTestCase, BuiltinTwoargFunctionTestCase


class RoundTests(TranspileTestCase):
    pass


class BuiltinRoundFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["round"]


class BuiltinRoundTwoargFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["round"]

    not_implemented = [
        'test_obj_class'
    ]
