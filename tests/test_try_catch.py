from .utils import TranspileTestCase


class TryExceptTests(TranspileTestCase):

    def test_try_except(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except:
                print("Got an error")
            print('Done.')
            """)

        # Caught exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except:
                print("Got an error")
            print('Done.')
            """)

    def test_try_except_unnamed(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except NameError:
                print("Got an error")
            print('Done.')
            """)

        # Caught exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError:
                print("Got an error")
            print('Done.')
            """)

        # Uncaught exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except NameError:
                print("Got an error")
            print('Done.')
            """, """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)

    def test_try_except_named(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except NameError as e:
                print("Got a NameError")
            print('Done.')
            """)

        # Caught exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError as e:
                print("Got a NameError")
            print('Done.')
            """)

        # Uncaught exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except NameError as e:
                print("Got a NameError")
            print('Done.')
            """, """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)

    def test_try_multiple_except(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError:
                print("Got an AttributeError")
            print('Done.')
            """)

        # Caught first exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError:
                print("Got an AttributeError")
            print('Done.')
            """)

        # Caught second exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except AttributeError:
                print("Got an AttributeError")
            except NameError:
                print("Got a NameError")
            print('Done.')
            """)

        # Uncaught exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError:
                print("Got an AttributeError")
            print('Done.')
            """, """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)

    def test_try_multiple_except_named(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError:
                print("Got an AttributeError")
            print('Done.')
            """)

        # Caught first exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError as e:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            print('Done.')
            """)

        # Caught second exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except AttributeError as e:
                print("Got an AttributeError")
            except NameError as e:
                print("Got a NameError")
            print('Done.')
            """)

        # Uncaught exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except NameError as e:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            print('Done.')
            """, """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)

    def test_try_multiple_match_except_unnamed(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except (NameError, TypeError):
                print("Got a NameError")
            except AttributeError:
                print("Got an AttributeError")
            print('Done.')
            """)

        # Caught first exception, first handler
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except (NameError, TypeError):
                print("Got a NameError")
            except AttributeError:
                print("Got an AttributeError")
            print('Done.')
            """)

        # Caught second exception, first handler
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except (TypeError, NameError):
                print("Got a NameError")
            except AttributeError:
                print("Got an AttributeError")
            print('Done.')
            """)

        # Caught first exception, second handler
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except AttributeError:
                print("Got an AttributeError")
            except (NameError, TypeError):
                print("Got a NameError")
            print('Done.')
            """)

        # Caught second exception, second handler
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except AttributeError:
                print("Got an AttributeError")
            except (TypeError, NameError):
                print("Got a NameError")
            print('Done.')
            """)

        # Uncaught exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except (NameError, TypeError):
                print("Got a TypeError")
            except AttributeError:
                print("Got an AttributeError")
            print('Done.')
            """, """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)

    def test_try_multiple_match_except_named(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except (NameError, TypeError) as e:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            print('Done.')
            """)

        # Caught first exception, first handler
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except (NameError, TypeError) as e:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            print('Done.')
            """)

        # Caught second exception, first handler
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except (TypeError, NameError) as e:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            print('Done.')
            """)

        # Caught first exception, second handler
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except AttributeError as e:
                print("Got an AttributeError")
            except (NameError, TypeError) as e:
                print("Got a NameError")
            print('Done.')
            """)

        # Caught second exception, second handler
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except AttributeError as e:
                print("Got an AttributeError")
            except (TypeError, NameError) as e:
                print("Got a NameError")
            print('Done.')
            """)

        # Uncaught exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except (NameError, TypeError) as e:
                print("Got a TypeError")
            except AttributeError as e:
                print("Got an AttributeError")
            print('Done.')
            """, """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)

    def test_try_multiple_except_mixed1(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            print('Done.')
            """)

        # Caught exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            print('Done.')
            """)

        # Uncaught exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            print('Done.')
            """, """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)

    def test_try_multiple_except_mixed2(self):
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except NameError as e:
                print("Got a NameError")
            except AttributeError:
                print("Got an AttributeError")
            print('Done.')
            """)

        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError as e:
                print("Got a NameError")
            except AttributeError:
                print("Got an AttributeError")
            print('Done.')
            """)

        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except NameError as e:
                print("Got a NameError")
            except AttributeError:
                print("Got an AttributeError")
            print('Done.')
            """, """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)

    def test_try_multiple_except_mixed3(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except NameError as e:
                print("Got a NameError")
            except AttributeError:
                print("Got an AttributeError")
            except:
                print("Got an anonymous error")
            print('Done.')
            """)

        # Caught exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError as e:
                print("Got a NameError")
            except AttributeError:
                print("Got an AttributeError")
            except:
                print("Got an anonymous error")
            print('Done.')
            """)

        # Caught as bucket case
        self.assertCode("""
            try:
                obj = int('asdf')
                print('OK')
            except NameError as e:
                print("Got a NameError")
            except AttributeError:
                print("Got an AttributeError")
            except:
                print("Got an anonymous error")
            print('Done.')
            """)


class TryExceptFinallyTests(TranspileTestCase):
    def test_try_finally(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

        # Uncaugt Exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
                print
            finally:
                print("Do final cleanup")
            print('Done.')
            """, """
            Do final cleanup
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)

    def test_try_except_finally(self):
        # No exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except:
                print("Got an error")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

        # Caught Exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except:
                print("Got an error")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

    def test_try_except_unnamed_finally(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except NameError:
                print("Got an error")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

        # Caught exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError:
                print("Got an error")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

        # Uncaught exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except NameError:
                print("Got an error")
            finally:
                print("Do final cleanup")
            print('Done.')
            """, """
            Do final cleanup
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)

    def test_try_except_named_finally(self):
        # No exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError as e:
                print("Got a NameError")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

        # Caught exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError as e:
                print("Got a NameError")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

        # Uncaught exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except NameError as e:
                print("Got a NameError")
            finally:
                print("Do final cleanup")
            print('Done.')
            """, """
            Do final cleanup
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)

    def test_try_multiple_except_finally(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

        # Caught first exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

        # Caught second exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except AttributeError as e:
                print("Got an AttributeError")
            except NameError:
                print("Got a NameError")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

        # Uncaught exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            finally:
                print("Do final cleanup")
            print('Done.')
            """, """
            Do final cleanup
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)


class TryExceptElseTests(TranspileTestCase):
    def test_try_except_else(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except:
                print("Got an error")
            else:
                print("Do else handling")
            print('Done.')
            """)

        # Caught exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except:
                print("Got an error")
            else:
                print("Do else handling")
            print('Done.')
            """)

    def test_try_except_unnamed_else(self):
        # No exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError:
                print("Got an error")
            else:
                print("Do else handling")
            print('Done.')
            """)

        # Caught exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError:
                print("Got an error")
            else:
                print("Do else handling")
            print('Done.')
            """)

        # Uncaught exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except NameError:
                print("Got an error")
            else:
                print("Do else handling")
            print('Done.')
            """, """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)

    def test_try_multiple_except_else(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            else:
                print("Do else handling")
            print('Done.')
            """)

        # Caught exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            else:
                print("Do else handling")
            print('Done.')
            """)

        # Uncaught exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            else:
                print("Do else handling")
            print('Done.')
            """, """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)


class TryExceptElseFinallyTests(TranspileTestCase):
    def test_try_except_else(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except:
                print("Got an error")
            else:
                print("Do else handling")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

        # Caught exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except:
                print("Got an error")
            else:
                print("Do else handling")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

    def test_try_except_unnamed_else(self):
        # No exception
        self.assertCode("""
            try:
                obj = 3
                print('OK')
            except NameError:
                print("Got an error")
            else:
                print("Do else handling")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

        # Caught exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError:
                print("Got an error")
            else:
                print("Do else handling")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

        # Uncaught exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except NameError:
                print("Got an error")
            else:
                print("Do else handling")
            finally:
                print("Do final cleanup")
            print('Done.')
            """, """
            Do final cleanup
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)

    def test_try_multiple_except_else(self):
        # No exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            else:
                print("Do else handling")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

        # Caught exception
        self.assertCode("""
            try:
                obj.no_such_attribute
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            else:
                print("Do else handling")
            finally:
                print("Do final cleanup")
            print('Done.')
            """)

        # Uncaught exception
        self.assertCodeOutput("""
            try:
                obj = int('asdf')
                print('OK')
            except NameError:
                print("Got a NameError")
            except AttributeError as e:
                print("Got an AttributeError")
            else:
                print("Do else handling")
            finally:
                print("Do final cleanup")
            print('Done.')
            """, """
            Do final cleanup
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:51)
                at org.Python.int_cast(Python.java:615)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:20)
                at org.pybee.test.<clinit>(test.py:2)
            """)
