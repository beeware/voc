from .. utils import TranspileTestCase, BuiltinFunctionTestCase

from unittest import expectedFailure

class LocalsTests(TranspileTestCase):
    def test_simple(self):
        self.assertCodeExecution("""
            print("There are %s locals" % len(locals()))
            x = 1
            y = 'z'
            print("There are %s locals" % len(locals()))

            def method():
                print("In method: there are %s locals" % len(locals()))

                try:
                    print("locals()['x'] =", locals()['x'])
                except KeyError:
                    print("Variable x not defined")
                try:
                    print("locals()['y'] =", locals()['y'])
                except KeyError:
                    print("Variable y not defined")
                try:
                    print("locals()['z'] =", locals()['z'])
                except KeyError:
                    print("Variable z not defined")

                x = 1
                y = 'z'
                locals()[y] = 2

                print("locals()['x'] =", locals()['x'])
                print("locals()['y'] =", locals()['y'])
                print("locals()['z'] =", locals()['z'])
                print('x', x)
                print('y', y)
                # print('z', z)

                print("In method: there are %s locals" % len(locals()))

            method()

            print("There are %s locals" % len(locals()))
            print("locals()['x'] =", locals()['x'])
            print("locals()['y'] =", locals()['y'])
            try:
                print("locals()['z'] =", locals()['z'])
            except KeyError:
                print("Variable z not defined")
            print('x', x)
            print('y', y)

            print('Done')
        """, run_in_function=False)

    @expectedFailure
    def test_preloaded_locals(self):
        self.assertCodeExecution("""
            lcls = locals
            x = 1
            y = 'z'

            print("There are %s locals" % len(lcls()))

            def method():
                print("In method: there are %s locals" % len(lcls()))

                x = 1
                y = 'z'

                print("In method: there are %s locals" % len(lcls()))

            method()
        """, run_in_function=False)


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
        'test_obj',
    ]
