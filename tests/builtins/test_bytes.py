from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class BytesTests(TranspileTestCase):
    pass


class BuiltinBytesFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["bytes"]
