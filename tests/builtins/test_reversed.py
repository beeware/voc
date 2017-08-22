from .. utils import SAMPLE_DATA, TranspileTestCase, BuiltinFunctionTestCase


def _iterate_test(datatype):

    def test_func(self):
        code = '\n'.join([
            '\nfor x in {value}:\n    print(x)\n'.format(value=value)
            for value in SAMPLE_DATA[datatype]
        ])
        self.assertCodeExecution(code)

    return test_func


class ReversedTests(TranspileTestCase):
    test_iterate_bytearray = _iterate_test('bytearray')
    test_iterate_bytes = _iterate_test('bytes')
    test_iterate_list = _iterate_test('list')
    test_iterate_range = _iterate_test('range')
    test_iterate_str = _iterate_test('str')
    test_iterate_tuple = _iterate_test('tuple')


class BuiltinReversedFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["reversed"]
