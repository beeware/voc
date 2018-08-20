from .. utils import TranspileTestCase, BuiltinFunctionTestCase, SAMPLE_SUBSTITUTIONS


class TupleTests(TranspileTestCase):
    pass


class BuiltinTupleFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["tuple"]

    not_implemented = [
        'test_tuple',
    ]

    substitutions = {
        "('one', 'two', 'six')": [
            "('two', 'one', 'six')", "('six', 'one', 'two')", "('one', 'six', 'two')", "('two', 'six', 'one')", "('six', 'two', 'one')"
        ],
        "('on', 'to', 'an')": [
            "('to', 'on', 'an')", "('an', 'on', 'to')", "('on', 'an', 'to')", "('to', 'an', 'on')", "('an', 'to', 'on')"
        ],
        "(1, 2.3456, 7)": [
            "(2.3456, 1, 7)", "(7, 1, 2.3456)", "(1, 7, 2.3456)", "(2.3456, 7, 1)", "(7, 2.3456, 1)"
        ]
    }

    substitutions.update(SAMPLE_SUBSTITUTIONS)
