from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class ObjectTests(TranspileTestCase):
    pass


class BuiltinObjectFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["object"]

    not_implemented = [
    ]
