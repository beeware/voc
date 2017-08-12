from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase

from unittest import expectedFailure


class IntTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = 37
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = 37
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)

    @expectedFailure
    def test_invalid_literal(self):
        self.assertCodeExecution("""
            int('q', 16)
            """)


class UnaryIntOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'int'


class BinaryIntOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'int'

    not_implemented = [
        'test_modulo_complex',
    ]


class InplaceIntOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'int'

    substitutions = {
        # Float tests rounding
        "(6.134323640217668+11.638718805964096j)": [
            "(6.134323640217669+11.638718805964096j)"
        ],
        "(20.329893907303543+38.57212830945331j)": [
            "(20.329893907303546+38.57212830945331j)"
        ],
        # Complex tests rounding
        "(0.7037573231697811+0.7104404479510611j)": [
            "(0.703757323169781+0.7104404479510611j)"
        ],
        "(-1.758764802874057+2.4303798814529753j)": [
            "(-1.7587648028740568+2.430379881452976j)"
        ],
        "(-0.9523946730227619-0.3048678185671067j)": [
            "(-0.9523946730227619-0.30486781856710676j)"
        ],
        "(4669868.983337471+4714215.686526724j)": [
            "(4669868.98333747+4714215.686526724j)"
        ],
        "(-4.926088756782315e-05-1.5768735125131076e-05j)": [
            "(-4.926088756782315e-05-1.576873512513108e-05j)"
        ],
        "(-35416596.83160829+5518228.872766545j)": [
            "(-35416596.83160829+5518228.872766544j)"
        ],
    }
