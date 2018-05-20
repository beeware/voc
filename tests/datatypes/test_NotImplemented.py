from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class NotImplementedTests(TranspileTestCase):
    def test_truth(self):
        self.assertCodeExecution("""
            x = NotImplemented
            print(x == True)
            """)


class UnaryNotImplementedOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'NotImplemented'


class BinaryNotImplementedOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'NotImplemented'


class InplaceNotImplementedOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'NotImplemented'
