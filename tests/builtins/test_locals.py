from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class LocalsTests(TranspileTestCase):
    def test_simple(self):
        self.assertCodeExecution("""
            print("There are %s locals" % len(locals()))
            x = 1
            y = 'z'
            print("There are %s locals" % len(locals()))
            print("locals()['x'] =", locals()['x'])
            print("locals()['y'] =", locals()['y'])
            try:
                print("locals()['z'] =", locals()['z'])
            except KeyError:
                print("Variable z not defined")

            locals()[y] = 2

            print("There are %s locals" % len(locals()))
            print("locals()['x'] =", locals()['x'])
            print("locals()['y'] =", locals()['y'])
            print("locals()['z'] =", locals()['z'])
            print('x', x)
            print('y', y)
            print('z', z)

            print('Done')
        """)


class BuiltinLocalsFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["locals"]

    not_implemented = [
        'test_bool',
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_float',
        'test_frozenset',
        'test_int',
        'test_list',
        'test_None',
        'test_NotImplemented',
        'test_range',
        'test_set',
        'test_slice',
        'test_str',
        'test_tuple',
    ]
