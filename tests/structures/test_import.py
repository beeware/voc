import os

from ..utils import TranspileTestCase


class ImportTests(TranspileTestCase):
    def test_import_stdlib_module(self):
        "You can import a Python module implemented in Java (a native stdlib shim)"
        self.assertCodeExecution(
            """
            import time

            time.time()

            print("Done.")
            """)

    def test_import_module(self):
        "You can import a Python module implemented in Python"
        self.assertCodeExecution(
            """
            import example

            example.some_method()

            print("Done.")
            """,
            extra_code={
                'example':
                    """
                    print("Now we're in the example module")

                    def some_method():
                        print("Now we're calling a module method")
                    """
            })

    def test_import_module_main(self):
        "You can import a Python module with if __name__ == '__main__'"
        self.assertCodeExecution(
            """
            import example

            print('A')

            if __name__ == "__main__":
                print('main')

            print('B')
            """,
            extra_code={
                'example':
                    """
                    print('C')

                    if __name__ == "__main__":
                        print('example main')

                    print('D')
                    """
            })

    def test_multiple_module_import(self):
        "You can import a multiple Python modules implemented in Python"
        self.assertCodeExecution(
            """
            import example, other

            example.some_method()

            other.other_method()

            print("Done.")
            """,
            extra_code={
                'example':
                    """
                    print("Now we're in the example module")

                    def some_method():
                        print("Now we're calling a module method")
                    """,
                'other':
                    """
                    print("Now we're in the other module")

                    def other_method():
                        print("Now we're calling another module method")
                    """
            })

    def test_full_dotted_path(self):
        self.assertCodeExecution(
            """
            import example.submodule

            example.submodule.some_method()

            print("Done.")
            """,
            extra_code={
                'example.__init__':
                    """
                    print("Initializing the example module")
                    """,
                'example.submodule':
                    """
                    print("Now we're in example.submodule")

                    def some_method():
                        print("Now we're calling a submodule method")
                    """
            })

    def test_module_from_dotted_path(self):
        self.assertCodeExecution(
            """
            from example import submodule

            submodule.some_method()

            print("Done.")
            """,
            extra_code={
                'example.__init__':
                    """
                    print("Initializing the example module")
                    """,
                'example.submodule':
                    """
                    print("Now we're in example.submodule")

                    def some_method():
                        print("Now we're calling a submodule method")
                    """
            })

    def test_symbol_from_dotted_path(self):
        self.assertCodeExecution(
            """
            from example.submodule import some_method

            some_method()

            print("Done.")
            """,
            extra_code={
                'example.__init__':
                    """
                    print("Initializing the example module")
                    """,
                'example.submodule':
                    """
                    print("Now we're in example.submodule")

                    def some_method():
                        print("Now we're calling a submodule method")
                    """
            })

    def test_ambiguous_symbol_from_dotted_path(self):
        self.assertCodeExecution(
            """
            from example.thing import Thing

            Thing()

            print("Done.")
            """,
            extra_code={
                'example.__init__':
                    """
                    print("Initializing the example module")
                    """,
                'example.thing':
                    """
                    print("Now we're in example.thing")

                    class Thing:
                        def __init__(self):
                            print("Now we're creating a Thing")

                    """
            })

    def test_full_deep_dotted_path(self):
        self.assertCodeExecution(
            """
            import example.submodule.subsubmodule.another

            example.submodule.subsubmodule.another.another_method()

            print("Done.")
            """,
            extra_code={
                'example.__init__':
                    """
                    print("Initializing the example module")
                    """,
                'example.submodule.__init__':
                    """
                    print("Now we're in example.submodule.__init__")
                    """,
                'example.submodule.other':
                    """
                    print("Now we're in example.submodule.other")

                    def other_method():
                        print("Now we're calling a submodule method")
                    """,
                'example.submodule.subsubmodule.__init__':
                    """
                    print("Now we're in example.submodule.subsubmodule.__init__")
                    """,
                'example.submodule.subsubmodule.another':
                    """
                    print("Now we're in example.submodule.subsubmodule.another")

                    def another_method():
                        print("Now we're calling a subsubmodule method")
                    """
            })

    def test_module_from_deep_dotted_path(self):
        self.assertCodeExecution(
            """
            from example.submodule.subsubmodule import another

            another.another_method()

            print("Done.")
            """,
            extra_code={
                'example.__init__':
                    """
                    print("Initializing the example module")
                    """,
                'example.submodule.__init__':
                    """
                    print("Now we're in example.submodule.__init__")
                    """,
                'example.submodule.other':
                    """
                    print("Now we're in example.submodule.other")

                    def other_method():
                        print("Now we're calling a submodule method")
                    """,
                'example.submodule.subsubmodule.__init__':
                    """
                    print("Now we're in example.submodule.subsubmodule.__init__")
                    """,
                'example.submodule.subsubmodule.another':
                    """
                    print("Now we're in example.submodule.subsubmodule.another")

                    def another_method():
                        print("Now we're calling a subsubmodule method")
                    """
            })

    def test_symbol_from_deep_dotted_path(self):
        self.assertCodeExecution(
            """
            from example.submodule.subsubmodule.another import another_method

            another_method()

            print("Done.")
            """,
            extra_code={
                'example.__init__':
                    """
                    print("Initializing the example module")
                    """,
                'example.submodule.__init__':
                    """
                    print("Now we're in example.submodule.__init__")
                    """,
                'example.submodule.other':
                    """
                    print("Now we're in example.submodule.other")

                    def other_method():
                        print("Now we're calling a submodule method")
                    """,
                'example.submodule.subsubmodule.__init__':
                    """
                    print("Now we're in example.submodule.subsubmodule.__init__")
                    """,
                'example.submodule.subsubmodule.another':
                    """
                    print("Now we're in example.submodule.subsubmodule.another")

                    def another_method():
                        print("Now we're calling a subsubmodule method")
                    """
            })

    def test_symbol_import(self):
        self.assertCodeExecution(
            """
            from example import some_method

            some_method()

            print("Done.")
            """,
            extra_code={
                'example':
                    """
                    print("Now we're in the example module")

                    def some_method():
                        print("Now we're calling a module method")
                    """
            })

    def test_multiple_symbol_import(self):
        self.assertCodeExecution(
            """
            from example import some_method, other_method

            print("Call some method...")
            some_method()

            print("Call another method...")
            other_method()

            try:
                print("But this will fail...")
                third_method()
            except NameError:
                print("Which it does.")

            print("Done.")
            """,
            extra_code={
                'example':
                    """
                    print("Now we're in the example module")

                    def some_method():
                        print("Now we're calling a module method")

                    def other_method():
                        print("Now we're calling another module method")

                    def third_method():
                        print("This shouldn't be called")

                    """
            })

    def test_import_star(self):
        self.assertCodeExecution(
            """
            from example import *

            print("Call some method...")
            some_method()

            print("Call another method...")
            other_method()

            print("Call a third method...")
            third_method()

            print("Done.")
            """,
            extra_code={
                'example':
                    """
                    print("Now we're in the example module")

                    def some_method():
                        print("Now we're calling a module method")

                    def other_method():
                        print("Now we're calling another module method")

                    def third_method():
                        print("Now we're calling a third module method")

                    """
            }, run_in_function=False)

    def test_import_star_with_all(self):
        self.assertCodeExecution(
            """
            from example import *

            print("Call some method...")
            some_method()

            print("Call another method...")
            other_method()

            try:
                print("But this will fail...")
                third_method()
            except NameError:
                print("Which it does.")

            print("Done.")
            """,
            extra_code={
                'example':
                    """
                    __all__ = ['some_method', 'other_method']

                    print("Now we're in the example module")

                    def some_method():
                        print("Now we're calling a module method")

                    def other_method():
                        print("Now we're calling another module method")

                    def third_method():
                        print("This shouldn't be called")

                    """
            }, run_in_function=False)

    def test_import_from_dot(self):
        self.assertCodeExecution(
            """
            from example import submodule2

            submodule2.method()

            print("Done.")
            """,
            extra_code={
                'example.__init__':
                    """
                    """,
                'example.submodule1':
                    """
                    def method():
                        print("Calling method in submodule1")
                    """,
                'example.submodule2':
                    """
                    from . import submodule1

                    def method():
                        print("Calling method in submodule2")
                        submodule1.method()
                    """,
            })

    def test_import_from_local_dot(self):
        self.assertCodeExecution(
            """
            from submodule import method1, method2

            method1()
            method2()

            print("Done.")
            """,
            extra_code={
                'submodule.__init__':
                    """
                    print("in submodule/__init__.py")
                    from .modulea import method2

                    def method1():
                        print("Calling method in submodule.__init__")
                    """,
                'submodule.modulea':
                    """
                    print("in submodule/modulea.py")

                    def method2():
                        print("Calling method in submodule.modulea")
                    """,
            })

    def test_import_from_local_dot_sibling(self):
        self.assertCodeExecution(
            """
            from submodule.moduleb import method3, method2

            method3()
            method2()

            print("Done.")
            """,
            extra_code={
                'submodule.__init__':
                    """
                    print("in submodule/__init__.py")

                    def method1():
                        print("Calling method1 in submodule.__init__")
                    """,
                'submodule.modulea':
                    """
                    print("in submodule/modulea.py")

                    def method2():
                        print("Calling method2 in submodule.modulea")
                    """,
                'submodule.moduleb':
                    """
                    print("in submodule/moduleb.py")
                    from .modulea import method2

                    def method3():
                        print("Calling method3 in submodule.moduleb")
                    """,
            })

    def test_import_from_local_dot_deep(self):
        self.assertCodeExecution(
            """
            from submodule import method1, method2, method3, method4

            method1()
            method2()
            method3()
            method4()

            print("Done.")
            """,
            extra_code={
                'submodule.__init__':
                    """
                    print("in submodule/__init__.py")
                    from .modulea import method2
                    from .subsubmodule import method3, method4

                    def method1():
                        print("Calling method1 in submodule.__init__")
                    """,
                'submodule.modulea':
                    """
                    print("in submodule/modulea.py")

                    def method2():
                        print("Calling method2 in submodule.modulea")
                    """,
                'submodule.subsubmodule.__init__':
                    """
                    print("in submodule/subsubmodule/__init__.py")
                    from .submodulea import method4

                    def method3():
                        print("Calling method3 in submodule.subsubmodule.__init__")
                    """,
                'submodule.subsubmodule.submodulea':
                    """
                    print("in submodule/subsubmodule/submodulea.py")

                    def method4():
                        print("Calling method4 in submodule.subsubmodule.submodula")
                    """,
            })

    def test_import_from_deep_upstream(self):
        self.assertCodeExecution(
            """
            from submodule.subsubmodule.submodulea import method

            method()

            print("Done.")
            """,
            extra_code={
                'submodule.__init__':
                    """
                    print("in submodule/__init__.py")

                    def method1():
                        print("Calling method in submodule.__init__")
                    """,
                'submodule.modulea':
                    """
                    print("in submodule/modulea.py")

                    def method2():
                        print("Calling method in submodule.modulea")
                    """,
                'submodule.moduleb':
                    """
                    print("in submodule/moduleb.py")

                    def method3():
                        print("Calling method in submodule.moduleb")
                    """,
                'submodule.modulec':
                    """
                    print("in submodule/modulec.py")

                    def method4():
                        print("Calling method in submodule.modulec")
                    """,
                'submodule.moduled.__init__':
                    """
                    print("in submodule/moduled/__init__.py")

                    def method5():
                        print("Calling method in submodule.moduled")
                    """,
                'submodule.moduled.submoduled':
                    """
                    print("in submodule/moduled/submoduled.py")

                    def method6():
                        print("Calling method in submodule.moduled.submoduled")
                    """,
                'submodule.subsubmodule.__init__':
                    """
                    print("in submodule/subsubmodule/__init__.py")

                    def method7():
                        print("Calling method in submodule.subsubmodule.__init__")
                    """,
                'submodule.subsubmodule.submodulea':
                    """
                    print("in submodule/subsubmodule/submodulea.py")
                    from .. import moduleb
                    from ..modulec import method4
                    from ..moduled import method5, submoduled

                    def method():
                        print("Calling method4 in submodule.subsubmodule.submodulea")
                        moduleb.method3()
                        method4()
                        method5()
                        submoduled.method6()
                    """,
            })


class NativeImportTests(TranspileTestCase):
    def test_import_java_module_static_method(self):
        "You can invoke a static method from a native Java namespace"
        self.assertJavaExecution(
            """
            from java import lang

            props = lang.System.getProperties()
            print(props.get("file.separator"))

            print("Done.")
            """,
            """
            %s
            Done.
            """ % os.path.sep)

    def test_import_java_class_static_method(self):
        "You can invoke a static method from a native Java class"
        self.assertJavaExecution(
            """
            from java.lang import System

            props = System.getProperties()
            print(props.get("file.separator"))

            print("Done.")
            """,
            """
            %s
            Done.
            """ % os.path.sep)

    def test_import_java_module(self):
        "You can import a native Java namespace as a Python module"
        self.assertJavaExecution(
            """
            from java import lang

            buf = lang.StringBuilder()
            buf.append('Hello, ')
            buf.append('World')
            print(buf.toString())

            print("Done.")
            """,
            """
            Hello, World
            Done.
            """)

    def test_import_java_class(self):
        "You can import a native Java class as a Python module"
        self.assertJavaExecution(
            """
            from java.lang import StringBuilder

            buf = StringBuilder()
            buf.append('Hello, ')
            buf.append('World')
            print(buf.toString())

            print("Done.")
            """,
            """
            Hello, World
            Done.
            """)


class BuiltinsImportTests(TranspileTestCase):
    def test_import_builtins(self):
        self.assertCodeExecution("""
            import builtins
            print(builtins.abs(-42))
            print("Done")
            """)

    def test_import_from_builtins(self):
        self.assertCodeExecution("""
            from builtins import abs
            print(abs(-42))
            print("Done")
            """)

    def test_import_from_builtins_as(self):
        self.assertCodeExecution("""
            from builtins import abs as _abs
            print(_abs(-42))
            print("Done")
            """)
