from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class HexTests(TranspileTestCase):
    pass


class BuiltinHexFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["hex"]

    not_implemented = [
    ]
