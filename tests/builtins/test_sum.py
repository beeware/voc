from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class SumTests(TranspileTestCase):
    pass


class BuiltinSumFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["sum"]

    not_implemented = []