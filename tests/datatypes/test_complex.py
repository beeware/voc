from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class ComplexTests(TranspileTestCase):
    def test_conjugate(self):
        self.assertCodeExecution("""
            x = complex(1.5, 1)
            print(x.conjugate())
            """)

    def test_real_imag(self):
        self.assertCodeExecution("""
            x = complex(1, 2.0)
            print(x.real)
            print(x.imag)
            """)

    def test_equality_with_numbers_when_zero_imag(self):
        self.assertCodeExecution("""
            x = 2
            y = complex(2, 0)
            print(x == y)
            print(y.__eq__(x))
            print(x != y)
            print(y.__ne__(x))

            x = 2.0
            y = complex(3, 0)
            print(x == y)
            print(y.__eq__(x))
            print(x != y)
            print(y.__ne__(x))

            x = True
            y = complex(1, 0)
            print(x == y)
            print(y.__eq__(x))
            print(x != y)
            print(y.__ne__(x))
            """)


class UnaryComplexOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'complex'


class BinaryComplexOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'complex'

    substitutions = {
        "(-161.18751321137705+195.77962956590406j)": [
            "(-161.18751321137705+195.77962956590403j)"
        ],
        "(2.6460893340172016e-18+0.04321391826377225j)": [
            "(2.6460019439688186e-18+0.04321391826377225j)"
        ],
        "(-9.8368221286278e-14-535.4916555247646j)": [
            "(-9.836497256617357e-14-535.4916555247646j)"
        ]
    }

    is_flakey = [
        'test_power_complex',
        'test_power_float',
    ]


class InplaceComplexOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'complex'
