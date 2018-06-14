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

    substitutions = {
        # output, keyed to all possible inputs
        "{3, 1.2, True}": [
            "{1.2, 3, True}", "{True, 1.2, 3}", "{True, 3, 1.2}", "{3, True, 1.2}", "{1.2, True, 3}"
        ],
        "{1, 2.3456, 'another'}": [
            "{1, 'another', 2.3456}", "{'another', 1, 2.3456}", "{'another', 2.3456, 1}", "{2.3456, 'another', 1}",
            "{2.3456, 1, 'another'}"
        ],
        "{'on', 'to', 'an'}": [
            "{'on', 'an', 'to'}", "{'to', 'an', 'on'}", "{'to', 'on', 'an'}", "{'an', 'to', 'on'}", "{'an', 'on', 'to'}"
        ],
        "{'one', 'two', 'six'}": [
            "{'one', 'six', 'two'}", "{'two', 'one', 'six'}", "{'two', 'six', 'one'}", "{'six', 'one', 'two'}",
            "{'six', 'two', 'one'}"
        ],
        "{1, 2.3456, 7}": [
            "{1, 7, 2.3456}", "{2.34556, 1, 7}", "{2.3456, 7, 1}", "{7, 2.3456, 1}", "{7, 1, 2.3456}"
        ],
        "{'a', 'b', 'c'}": [
            "{'a', 'c', 'b'}", "{'b', 'a', 'c'}", "{'b', 'c', 'a'}", "{'c', 'a', 'b'}", "{'c', 'b', 'c'}"
        ]
    }
