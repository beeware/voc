from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class BoolTests(TranspileTestCase):

    def test_setattr(self):
        self.assertCodeExecution("""
            x = True
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = True
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)


class UnaryBoolOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bool'


class BinaryBoolOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bool'


class InplaceBoolOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bool'
