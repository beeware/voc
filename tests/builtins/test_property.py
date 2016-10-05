from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class PropertyTests(TranspileTestCase):
    pass


class BuiltinPropertyFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["property"]

    not_implemented = [
        'test_class',
        'test_complex',
        'test_frozenset',
    ]
