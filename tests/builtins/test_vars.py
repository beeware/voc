from unittest import expectedFailure

from .. utils import TranspileTestCase, BuiltinFunctionTestCase


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

    def test_vars_delta(self):
        """This is a version of test_simple that allows for the initial
        global count to be wrong. This test can be removed once test_simple
        passes."""
        self.assertCodeExecution("""
            n_vars = len(vars())
            x = 1
            y = 'z'
            print("Found delta of %s vars" % (len(vars()) - n_vars))

            def method():
                print("In method: Found delta of %s vars" % (len(vars()) - n_vars))

                print("vars()['x'] =", vars()['x'])
                print("vars()['y'] =", vars()['y'])
                try:
                    print("vars()['z'] =", vars()['z'])
                except KeyError:
                    print("Variable z not defined")

                vars()[y] = 2

                print("In method: Found delta of %s vars" % (len(vars()) - n_vars))

            method()

            print("Found delta of %s vars" % (len(vars()) - n_vars))
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
