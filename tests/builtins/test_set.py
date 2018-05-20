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
             'test_tuple': (3.4, 3.5, 3.6)
    }

    is_flakey = [
        'test_dict',
    ]
