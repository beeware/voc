from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class ListTests(TranspileTestCase):
    def test_list_constructor(self):
        self.assertCodeExecution("""
            #No args
            print(list())

            #List arg
            print(list([1,2,3]))
            """)


class BuiltinListFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["list"]

    substitutions = {
        "[1, 2.3456, 'another']": [
            "[1, 'another', 2.3456]",
            "[2.3456, 1, 'another']",
            "[2.3456, 'another', 1]",
            "['another', 1, 2.3456]",
            "['another', 2.3456, 1]",
        ]
    }

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_dict',
        'test_frozenset',
        'test_str',
    ]
