from .utils import TranspileTestCase


class TryExceptTests(TranspileTestCase):

    # def test_try_except(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError:
    #                 print("Got an error")
    #             x = 3
    #             """,
    #         java="""
    #             """)

    def test_try_except_named(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except AttributeError as e:
                    print("Got an error", e)
                """,
            java="""
                 Code (135 bytes)
                     Max stack: 7
                     Max locals: 1
                     Bytecode: (99 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 12>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <LDC <String 'no_such_attribute'>>
                          23: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          26: <POP>
                          27: <GOTO 70>
                          30: <ASTORE_0>
                          31: <NEW org/python/Object>
                          34: <DUP>
                          35: <ALOAD_0>
                          36: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                          39: <ASTORE_0>
                          40: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          43: <LDC <String 'print'>>
                          45: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          48: <DUP>
                          49: <IFNONNULL 12>
                          52: <POP>
                          53: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          56: <LDC <String 'print'>>
                          58: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          61: <CHECKCAST <Class org/python/Callable>>
                          64: <ICONST_2>
                          65: <ANEWARRAY org/python/Object>
                          68: <DUP>
                          69: <ICONST_0>
                          70: <NEW org/python/Object>
                          73: <DUP>
                          74: <LDC <String 'Got an error'>>
                          76: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          79: <AASTORE>
                          80: <DUP>
                          81: <ICONST_1>
                          82: <ALOAD_0>
                          83: <AASTORE>
                          84: <NEW java/util/Hashtable>
                          87: <DUP>
                          88: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          91: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          96: <POP>
                          97: <ACONST_NULL>
                          98: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/AttributeError: 0-27 [30]
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 3
                                 40: 5
                """)

    # def test_try_multiple_except(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError:
    #                 print("Got an AttributeError")
    #             except NameError:
    #                 print("Got a NameError")
    #             """,
    #         java="""
    #             """)

    def test_try_multiple_except_named(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except AttributeError as e:
                    print("Got an AttributeError", e)
                except NameError as e:
                    print("Got a NameError", e)
                """,
            java="""
                 Code (217 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (169 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 12>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <LDC <String 'no_such_attribute'>>
                          23: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          26: <POP>
                          27: <GOTO 140>
                          30: <ASTORE_0>
                          31: <NEW org/python/Object>
                          34: <DUP>
                          35: <ALOAD_0>
                          36: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                          39: <ASTORE_0>
                          40: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          43: <LDC <String 'print'>>
                          45: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          48: <DUP>
                          49: <IFNONNULL 12>
                          52: <POP>
                          53: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          56: <LDC <String 'print'>>
                          58: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          61: <CHECKCAST <Class org/python/Callable>>
                          64: <ICONST_2>
                          65: <ANEWARRAY org/python/Object>
                          68: <DUP>
                          69: <ICONST_0>
                          70: <NEW org/python/Object>
                          73: <DUP>
                          74: <LDC <String 'Got an AttributeError'>>
                          76: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          79: <AASTORE>
                          80: <DUP>
                          81: <ICONST_1>
                          82: <ALOAD_0>
                          83: <AASTORE>
                          84: <NEW java/util/Hashtable>
                          87: <DUP>
                          88: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          91: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          96: <POP>
                          97: <GOTO 70>
                         100: <ASTORE_0>
                         101: <NEW org/python/Object>
                         104: <DUP>
                         105: <ALOAD_0>
                         106: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                         109: <ASTORE_0>
                         110: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         113: <LDC <String 'print'>>
                         115: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         118: <DUP>
                         119: <IFNONNULL 12>
                         122: <POP>
                         123: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         126: <LDC <String 'print'>>
                         128: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         131: <CHECKCAST <Class org/python/Callable>>
                         134: <ICONST_2>
                         135: <ANEWARRAY org/python/Object>
                         138: <DUP>
                         139: <ICONST_0>
                         140: <NEW org/python/Object>
                         143: <DUP>
                         144: <LDC <String 'Got a NameError'>>
                         146: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         149: <AASTORE>
                         150: <DUP>
                         151: <ICONST_1>
                         152: <ALOAD_0>
                         153: <AASTORE>
                         154: <NEW java/util/Hashtable>
                         157: <DUP>
                         158: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         161: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         166: <POP>
                         167: <ACONST_NULL>
                         168: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-27 [30]
                         org/python/exceptions/NameError: 0-27 [100]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 40: 5
                                 110: 7
                """)

    # def test_try_multiple_except_mixed1(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError:
    #                 print("Got an AttributeError")
    #             except NameError as e:
    #                 print("Got a NameError", e)
    #             """,
    #         java="""
    #             """)

    # def test_try_multiple_except_mixed2(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError as e:
    #                 print("Got an AttributeError", e)
    #             except NameError:
    #                 print("Got a NameError")
    #             """,
    #         java="""
    #             """)


class TryExceptFinallyTests(TranspileTestCase):
    pass

    # def test_try_finally(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 x = 3
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)

    # def test_try_except_finally(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError:
    #                 print("Got an error")
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)

    # def test_try_multiple_except_finally(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError:
    #                 print("Got an AttributeError")
    #             except NameError:
    #                 print("Got a NameError")
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)

    # def test_try_multiple_named_except_finally(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError as e:
    #                 print("Got an AttributeError", e)
    #             except NameError as e:
    #                 print("Got a NameError", e)
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)

    # def test_try_multiple_except_mixed1_finally(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError:
    #                 print("Got an AttributeError")
    #             except NameError as e:
    #                 print("Got a NameError", e)
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)

    # def test_try_multiple_except_mixed2_finally(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError, e:
    #                 print("Got an AttributeError")
    #             except NameError:
    #                 print("Got a NameError")
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)


class TryExceptElseTests(TranspileTestCase):
    pass

    # def test_try_else(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 x = 3
    #             else:
    #                 print("Do else handling")
    #             """,
    #         java="""
    #             """)

    # def test_try_except_else(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError:
    #                 print("Got an error")
    #             else:
    #                 print("Do else handling")
    #             """,
    #         java="""
    #             """)

    # def test_try_multiple_except_else(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError:
    #                 print("Got an AttributeError")
    #             except NameError:
    #                 print("Got a NameError")
    #             else:
    #                 print("Do else handling")
    #             """,
    #         java="""
    #             """)

    # def test_try_multiple_named_except_else(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError as e:
    #                 print("Got an AttributeError", e)
    #             except NameError as e:
    #                 print("Got a NameError", e)
    #             else:
    #                 print("Do else handling")
    #             """,
    #         java="""
    #             """)

    # def test_try_multiple_except_mixed1_else(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError:
    #                 print("Got an AttributeError")
    #             except NameError as e:
    #                 print("Got a NameError", e)
    #             else:
    #                 print("Do else handling")
    #             """,
    #         java="""
    #             """)

    # def test_try_multiple_except_mixed2_else(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError, e:
    #                 print("Got an AttributeError")
    #             except NameError:
    #                 print("Got a NameError")
    #             else:
    #                 print("Do else handling")
    #             """,
    #         java="""
    #             """)


class TryExceptElseFinallyTests(TranspileTestCase):
    pass

    # def test_try_else_finally(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 x = 3
    #             else:
    #                 print("Do else handling")
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)

    # def test_try_except_else_finally(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError:
    #                 print("Got an error")
    #             else:
    #                 print("Do else handling")
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)

    # def test_try_multiple_except_else_finally(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError:
    #                 print("Got an AttributeError")
    #             except NameError:
    #                 print("Got a NameError")
    #             else:
    #                 print("Do else handling")
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)

    # def test_try_multiple_named_except_else_finally(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError as e:
    #                 print("Got an AttributeError", e)
    #             except NameError as e:
    #                 print("Got a NameError", e)
    #             else:
    #                 print("Do else handling")
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)

    # def test_try_multiple_except_mixed1_else_finally(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError:
    #                 print("Got an AttributeError")
    #             except NameError as e:
    #                 print("Got a NameError", e)
    #             else:
    #                 print("Do else handling")
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)

    # def test_try_multiple_except_mixed2_else_finally(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError, e:
    #                 print("Got an AttributeError")
    #             except NameError:
    #                 print("Got a NameError")
    #             else:
    #                 print("Do else handling")
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)
