from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class OctTests(TranspileTestCase):
    pass


class BuiltinOctFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["oct"]

    not_implemented = [
        'test_class',
        'test_complex',
        'test_frozenset',
    ]
