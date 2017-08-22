from .. utils import TranspileTestCase, BuiltinFunctionTestCase, SAMPLE_SUBSTITUTIONS


class ListTests(TranspileTestCase):
    pass


class BuiltinListFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["list"]

    substitutions = dict(SAMPLE_SUBSTITUTIONS)
    substitutions.update({
        "[1, 2.3456, 'another']": [
            "[1, 'another', 2.3456]",
            "[2.3456, 1, 'another']",
            "[2.3456, 'another', 1]",
            "['another', 1, 2.3456]",
            "['another', 2.3456, 1]",
        ],
        "['a', 'c', 'd']": [
            "['a', 'd', 'c']",
            "['c', 'a', 'd']",
            "['c', 'd', 'a']",
            "['d', 'a', 'c']",
            "['d', 'c', 'a']",
        ]
    })
