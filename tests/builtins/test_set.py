from .. utils import (
TranspileTestCase,
BuiltinFunctionTestCase,
SAMPLE_SUBSTITUTIONS
)


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

    substitutions = {
        "{3, 1.2, True}": [
            "{1.2, 3, True}", "{True, 1.2, 3}", "{True, 3, 1.2}", "{3, True, 1.2}", "{1.2, True, 3}"
        ]
    }
    substitutions.update(SAMPLE_SUBSTITUTIONS)
