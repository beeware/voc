from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class SetTests(TranspileTestCase):
    pass


class BuiltinSetFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["set"]

    not_implemented = [
        'test_bytes',
        'test_str',
    ]

    not_implemented_versions = {
    }

    is_flakey = [
        'test_dict',
    ]
