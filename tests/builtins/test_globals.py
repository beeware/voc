from unittest import expectedFailure
from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class GlobalsTests(TranspileTestCase):
    @expectedFailure
    def test_simple(self):
        self.assertCodeExecution("""
            print("There are %s globals" % len(globals()))
            x = 1
            y = 'z'
            print("There are %s globals" % len(globals()))

            def method():
                print("In method: there are %s globals" % len(globals()))

                print("globals()['x'] =", globals()['x'])
                print("globals()['y'] =", globals()['y'])
                try:
                    print("globals()['z'] =", globals()['z'])
                except KeyError:
                    print("Variable z not defined")

                globals()[y] = 2

                print("In method: there are %s globals" % len(globals()))

            method()

            print("There are %s globals" % len(globals()))
            print("globals()['x'] =", globals()['x'])
            print("globals()['y'] =", globals()['y'])
            print("globals()['z'] =", globals()['z'])
            print('x', x)
            print('y', y)
            print('z', z)

            print('Done')
        """, run_in_function=False)

    def test_globals_delta(self):
        """This is a version of test_simple that allows for the initial
        global count to be wrong. This test can be removed once test_simple
        passes."""
        self.assertCodeExecution("""
            n_globals = len(globals())
            x = 1
            y = 'z'
            print("Found delta of %s globals" % (len(globals()) - n_globals))

            def method():
                print("In method: Found delta of %s globals" % (len(globals()) - n_globals))

                print("globals()['x'] =", globals()['x'])
                print("globals()['y'] =", globals()['y'])
                try:
                    print("globals()['z'] =", globals()['z'])
                except KeyError:
                    print("Variable z not defined")

                globals()[y] = 2

                print("In method: Found delta of %s globals" % (len(globals()) - n_globals))

            method()

            print("Found delta of %s globals" % (len(globals()) - n_globals))
            print("globals()['x'] =", globals()['x'])
            print("globals()['y'] =", globals()['y'])
            print("globals()['z'] =", globals()['z'])
            print('x', x)
            print('y', y)
            print('z', z)

            print('Done')
        """, run_in_function=False)

class BuiltinGlobalsFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["globals"]

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
