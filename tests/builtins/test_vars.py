from .. utils import TranspileTestCase, BuiltinFunctionTestCase

from unittest import expectedFailure


class VarsTests(TranspileTestCase):
    @expectedFailure
    def test_simple(self):
        self.assertCodeExecution("""
            print("There are %s vars" % len(vars()))
            x = 1
            y = 'z'
            print("There are %s vars" % len(vars()))

            def method():
                print("In method: there are %s vars" % len(vars()))

                print("vars()['x'] =", vars()['x'])
                print("vars()['y'] =", vars()['y'])
                try:
                    print("vars()['z'] =", vars()['z'])
                except KeyError:
                    print("Variable z not defined")

                vars()[y] = 2

                print("In method: there are %s vars" % len(vars()))

            method()

            print("There are %s vars" % len(vars()))
            print("vars()['x'] =", vars()['x'])
            print("vars()['y'] =", vars()['y'])
            print("vars()['z'] =", vars()['z'])
            print('x', x)
            print('y', y)
            print('z', z)

            print('Done')
        """, run_in_function=False)


class BuiltinVarsFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["vars"]

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
        'test_set',
        'test_str',
        'test_tuple',
        'test_range',
        'test_slice',
    ]
