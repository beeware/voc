from .utils import TranspileTestCase


class TryExceptTests(TranspileTestCase):

    def test_try_except(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except:
                    print("Got an error")
                """,
            java="""
                 Code (122 bytes)
                     Max stack: 7
                     Max locals: 0
                     Bytecode: (86 bytes)
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
                          27: <GOTO 57>
                          30: <POP>
                          31: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          34: <LDC <String 'print'>>
                          36: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          39: <DUP>
                          40: <IFNONNULL 12>
                          43: <POP>
                          44: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          47: <LDC <String 'print'>>
                          49: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          52: <CHECKCAST <Class org/python/Callable>>
                          55: <ICONST_1>
                          56: <ANEWARRAY org/python/Object>
                          59: <DUP>
                          60: <ICONST_0>
                          61: <NEW org/python/Object>
                          64: <DUP>
                          65: <LDC <String 'Got an error'>>
                          67: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          70: <AASTORE>
                          71: <NEW java/util/Hashtable>
                          74: <DUP>
                          75: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          78: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          83: <POP>
                          84: <ACONST_NULL>
                          85: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/BaseException: 0-27 [30]
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 3
                                 31: 5
                """)

    def test_try_except_unnamed(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except AttributeError:
                    print("Got an error")
                """,
            java="""
                 Code (122 bytes)
                     Max stack: 7
                     Max locals: 0
                     Bytecode: (86 bytes)
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
                          27: <GOTO 57>
                          30: <POP>
                          31: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          34: <LDC <String 'print'>>
                          36: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          39: <DUP>
                          40: <IFNONNULL 12>
                          43: <POP>
                          44: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          47: <LDC <String 'print'>>
                          49: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          52: <CHECKCAST <Class org/python/Callable>>
                          55: <ICONST_1>
                          56: <ANEWARRAY org/python/Object>
                          59: <DUP>
                          60: <ICONST_0>
                          61: <NEW org/python/Object>
                          64: <DUP>
                          65: <LDC <String 'Got an error'>>
                          67: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          70: <AASTORE>
                          71: <NEW java/util/Hashtable>
                          74: <DUP>
                          75: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          78: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          83: <POP>
                          84: <ACONST_NULL>
                          85: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/AttributeError: 0-27 [30]
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 3
                                 31: 5
                """)

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

    def test_try_multiple_except(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except AttributeError:
                    print("Got an AttributeError")
                except NameError:
                    print("Got a NameError")
                """,
            java="""
                 Code (191 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (143 bytes)
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
                          27: <GOTO 114>
                          30: <POP>
                          31: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          34: <LDC <String 'print'>>
                          36: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          39: <DUP>
                          40: <IFNONNULL 12>
                          43: <POP>
                          44: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          47: <LDC <String 'print'>>
                          49: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          52: <CHECKCAST <Class org/python/Callable>>
                          55: <ICONST_1>
                          56: <ANEWARRAY org/python/Object>
                          59: <DUP>
                          60: <ICONST_0>
                          61: <NEW org/python/Object>
                          64: <DUP>
                          65: <LDC <String 'Got an AttributeError'>>
                          67: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          70: <AASTORE>
                          71: <NEW java/util/Hashtable>
                          74: <DUP>
                          75: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          78: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          83: <POP>
                          84: <GOTO 57>
                          87: <POP>
                          88: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          91: <LDC <String 'print'>>
                          93: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          96: <DUP>
                          97: <IFNONNULL 12>
                         100: <POP>
                         101: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         104: <LDC <String 'print'>>
                         106: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         109: <CHECKCAST <Class org/python/Callable>>
                         112: <ICONST_1>
                         113: <ANEWARRAY org/python/Object>
                         116: <DUP>
                         117: <ICONST_0>
                         118: <NEW org/python/Object>
                         121: <DUP>
                         122: <LDC <String 'Got a NameError'>>
                         124: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         127: <AASTORE>
                         128: <NEW java/util/Hashtable>
                         131: <DUP>
                         132: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         135: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         140: <POP>
                         141: <ACONST_NULL>
                         142: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-27 [30]
                         org/python/exceptions/NameError: 0-27 [87]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 31: 5
                                 88: 7
                """)

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

    def test_try_multiple_match_except_unnamed(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except (AttributeError, TypeError):
                    print("Got an AttributeError")
                except NameError:
                    print("Got a NameError")
                """,
            java="""
                 Code (191 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (143 bytes)
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
                          27: <GOTO 114>
                          30: <POP>
                          31: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          34: <LDC <String 'print'>>
                          36: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          39: <DUP>
                          40: <IFNONNULL 12>
                          43: <POP>
                          44: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          47: <LDC <String 'print'>>
                          49: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          52: <CHECKCAST <Class org/python/Callable>>
                          55: <ICONST_1>
                          56: <ANEWARRAY org/python/Object>
                          59: <DUP>
                          60: <ICONST_0>
                          61: <NEW org/python/Object>
                          64: <DUP>
                          65: <LDC <String 'Got an AttributeError'>>
                          67: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          70: <AASTORE>
                          71: <NEW java/util/Hashtable>
                          74: <DUP>
                          75: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          78: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          83: <POP>
                          84: <GOTO 57>
                          87: <POP>
                          88: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          91: <LDC <String 'print'>>
                          93: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          96: <DUP>
                          97: <IFNONNULL 12>
                         100: <POP>
                         101: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         104: <LDC <String 'print'>>
                         106: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         109: <CHECKCAST <Class org/python/Callable>>
                         112: <ICONST_1>
                         113: <ANEWARRAY org/python/Object>
                         116: <DUP>
                         117: <ICONST_0>
                         118: <NEW org/python/Object>
                         121: <DUP>
                         122: <LDC <String 'Got a NameError'>>
                         124: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         127: <AASTORE>
                         128: <NEW java/util/Hashtable>
                         131: <DUP>
                         132: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         135: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         140: <POP>
                         141: <ACONST_NULL>
                         142: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-27 [30]
                         org/python/exceptions/NameError: 0-27 [87]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 31: 5
                                 88: 7
                """)

    def test_try_multiple_match_except_named(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except (AttributeError, TypeError) as e:
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

    def test_try_multiple_except_mixed1(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except AttributeError:
                    print("Got an AttributeError")
                except NameError as e:
                    print("Got a NameError", e)
                """,
            java="""
                 Code (204 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (156 bytes)
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
                          27: <GOTO 127>
                          30: <POP>
                          31: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          34: <LDC <String 'print'>>
                          36: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          39: <DUP>
                          40: <IFNONNULL 12>
                          43: <POP>
                          44: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          47: <LDC <String 'print'>>
                          49: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          52: <CHECKCAST <Class org/python/Callable>>
                          55: <ICONST_1>
                          56: <ANEWARRAY org/python/Object>
                          59: <DUP>
                          60: <ICONST_0>
                          61: <NEW org/python/Object>
                          64: <DUP>
                          65: <LDC <String 'Got an AttributeError'>>
                          67: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          70: <AASTORE>
                          71: <NEW java/util/Hashtable>
                          74: <DUP>
                          75: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          78: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          83: <POP>
                          84: <GOTO 70>
                          87: <ASTORE_0>
                          88: <NEW org/python/Object>
                          91: <DUP>
                          92: <ALOAD_0>
                          93: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                          96: <ASTORE_0>
                          97: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         100: <LDC <String 'print'>>
                         102: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         105: <DUP>
                         106: <IFNONNULL 12>
                         109: <POP>
                         110: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         113: <LDC <String 'print'>>
                         115: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         118: <CHECKCAST <Class org/python/Callable>>
                         121: <ICONST_2>
                         122: <ANEWARRAY org/python/Object>
                         125: <DUP>
                         126: <ICONST_0>
                         127: <NEW org/python/Object>
                         130: <DUP>
                         131: <LDC <String 'Got a NameError'>>
                         133: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         136: <AASTORE>
                         137: <DUP>
                         138: <ICONST_1>
                         139: <ALOAD_0>
                         140: <AASTORE>
                         141: <NEW java/util/Hashtable>
                         144: <DUP>
                         145: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         148: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         153: <POP>
                         154: <ACONST_NULL>
                         155: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-27 [30]
                         org/python/exceptions/NameError: 0-27 [87]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 31: 5
                                 97: 7
                """)

    def test_try_multiple_except_mixed2(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except AttributeError as e:
                    print("Got an AttributeError", e)
                except NameError:
                    print("Got a NameError")
                """,
            java="""
                 Code (204 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (156 bytes)
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
                          27: <GOTO 127>
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
                          97: <GOTO 57>
                         100: <POP>
                         101: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         104: <LDC <String 'print'>>
                         106: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         109: <DUP>
                         110: <IFNONNULL 12>
                         113: <POP>
                         114: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         117: <LDC <String 'print'>>
                         119: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         122: <CHECKCAST <Class org/python/Callable>>
                         125: <ICONST_1>
                         126: <ANEWARRAY org/python/Object>
                         129: <DUP>
                         130: <ICONST_0>
                         131: <NEW org/python/Object>
                         134: <DUP>
                         135: <LDC <String 'Got a NameError'>>
                         137: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         140: <AASTORE>
                         141: <NEW java/util/Hashtable>
                         144: <DUP>
                         145: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         148: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         153: <POP>
                         154: <ACONST_NULL>
                         155: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-27 [30]
                         org/python/exceptions/NameError: 0-27 [100]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 40: 5
                                 101: 7
                """)

    def test_try_multiple_except_mixed3(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except AttributeError as e:
                    print("Got an AttributeError", e)
                except NameError:
                    print("Got a NameError")
                except:
                    print("Got an anonymous error")
                """,
            java="""
                 Code (273 bytes)
                     Max stack: 9
                     Max locals: 1
                     Bytecode: (213 bytes)
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
                          27: <GOTO 184>
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
                          97: <GOTO 114>
                         100: <POP>
                         101: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         104: <LDC <String 'print'>>
                         106: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         109: <DUP>
                         110: <IFNONNULL 12>
                         113: <POP>
                         114: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         117: <LDC <String 'print'>>
                         119: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         122: <CHECKCAST <Class org/python/Callable>>
                         125: <ICONST_1>
                         126: <ANEWARRAY org/python/Object>
                         129: <DUP>
                         130: <ICONST_0>
                         131: <NEW org/python/Object>
                         134: <DUP>
                         135: <LDC <String 'Got a NameError'>>
                         137: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         140: <AASTORE>
                         141: <NEW java/util/Hashtable>
                         144: <DUP>
                         145: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         148: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         153: <POP>
                         154: <GOTO 57>
                         157: <POP>
                         158: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         161: <LDC <String 'print'>>
                         163: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         166: <DUP>
                         167: <IFNONNULL 12>
                         170: <POP>
                         171: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         174: <LDC <String 'print'>>
                         176: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         179: <CHECKCAST <Class org/python/Callable>>
                         182: <ICONST_1>
                         183: <ANEWARRAY org/python/Object>
                         186: <DUP>
                         187: <ICONST_0>
                         188: <NEW org/python/Object>
                         191: <DUP>
                         192: <LDC <String 'Got an anonymous error'>>
                         194: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         197: <AASTORE>
                         198: <NEW java/util/Hashtable>
                         201: <DUP>
                         202: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         205: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         210: <POP>
                         211: <ACONST_NULL>
                         212: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-27 [30]
                         org/python/exceptions/NameError: 0-27 [100]
                         org/python/exceptions/BaseException: 0-27 [157]
                     Attributes: (1)
                         LineNumberTable (18 bytes)
                             Line numbers (4 total):
                                 0: 3
                                 40: 5
                                 101: 7
                                 158: 9
                """)


class TryExceptFinallyTests(TranspileTestCase):
    def test_try_finally(self):
        self.assertBlock(
            python="""
                try:
                    x = 3
                finally:
                    print("Do final cleanup")
                """,
            java="""
                 Code (163 bytes)
                     Max stack: 8
                     Max locals: 2
                     Bytecode: (123 bytes)
                           0: <NEW org/python/Object>
                           3: <DUP>
                           4: <ICONST_3>
                           5: <INVOKESPECIAL org/python/Object.<init> (I)V>
                           8: <ASTORE_0>
                           9: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          12: <LDC <String 'print'>>
                          14: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          17: <DUP>
                          18: <IFNONNULL 12>
                          21: <POP>
                          22: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          25: <LDC <String 'print'>>
                          27: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          30: <CHECKCAST <Class org/python/Callable>>
                          33: <ICONST_1>
                          34: <ANEWARRAY org/python/Object>
                          37: <DUP>
                          38: <ICONST_0>
                          39: <NEW org/python/Object>
                          42: <DUP>
                          43: <LDC <String 'Do final cleanup'>>
                          45: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          48: <AASTORE>
                          49: <NEW java/util/Hashtable>
                          52: <DUP>
                          53: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          56: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          61: <POP>
                          62: <GOTO 59>
                          65: <ASTORE_1>
                          66: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          69: <LDC <String 'print'>>
                          71: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          74: <DUP>
                          75: <IFNONNULL 12>
                          78: <POP>
                          79: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          82: <LDC <String 'print'>>
                          84: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          87: <CHECKCAST <Class org/python/Callable>>
                          90: <ICONST_1>
                          91: <ANEWARRAY org/python/Object>
                          94: <DUP>
                          95: <ICONST_0>
                          96: <NEW org/python/Object>
                          99: <DUP>
                         100: <LDC <String 'Do final cleanup'>>
                         102: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         105: <AASTORE>
                         106: <NEW java/util/Hashtable>
                         109: <DUP>
                         110: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         113: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         118: <POP>
                         119: <ALOAD_1>
                         120: <ATHROW>
                         121: <ACONST_NULL>
                         122: <ARETURN>
                     Exceptions: (1)
                         finally: 0-9 [65]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 9: 5
                                 66: 5
                """)

    def test_try_except_finally(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except:
                    print("Got an error")
                finally:
                    print("Do final cleanup")
                """,
            java="""
                 Code (315 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (251 bytes)
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
                          27: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          30: <LDC <String 'print'>>
                          32: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          35: <DUP>
                          36: <IFNONNULL 12>
                          39: <POP>
                          40: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          43: <LDC <String 'print'>>
                          45: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          48: <CHECKCAST <Class org/python/Callable>>
                          51: <ICONST_1>
                          52: <ANEWARRAY org/python/Object>
                          55: <DUP>
                          56: <ICONST_0>
                          57: <NEW org/python/Object>
                          60: <DUP>
                          61: <LDC <String 'Do final cleanup'>>
                          63: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          66: <AASTORE>
                          67: <NEW java/util/Hashtable>
                          70: <DUP>
                          71: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          74: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          79: <POP>
                          80: <GOTO 169>
                          83: <POP>
                          84: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          87: <LDC <String 'print'>>
                          89: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          92: <DUP>
                          93: <IFNONNULL 12>
                          96: <POP>
                          97: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         100: <LDC <String 'print'>>
                         102: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         105: <CHECKCAST <Class org/python/Callable>>
                         108: <ICONST_1>
                         109: <ANEWARRAY org/python/Object>
                         112: <DUP>
                         113: <ICONST_0>
                         114: <NEW org/python/Object>
                         117: <DUP>
                         118: <LDC <String 'Got an error'>>
                         120: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         123: <AASTORE>
                         124: <NEW java/util/Hashtable>
                         127: <DUP>
                         128: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         131: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         136: <POP>
                         137: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         140: <LDC <String 'print'>>
                         142: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         145: <DUP>
                         146: <IFNONNULL 12>
                         149: <POP>
                         150: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         153: <LDC <String 'print'>>
                         155: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         158: <CHECKCAST <Class org/python/Callable>>
                         161: <ICONST_1>
                         162: <ANEWARRAY org/python/Object>
                         165: <DUP>
                         166: <ICONST_0>
                         167: <NEW org/python/Object>
                         170: <DUP>
                         171: <LDC <String 'Do final cleanup'>>
                         173: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         176: <AASTORE>
                         177: <NEW java/util/Hashtable>
                         180: <DUP>
                         181: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         184: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         189: <POP>
                         190: <GOTO 59>
                         193: <ASTORE_0>
                         194: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         197: <LDC <String 'print'>>
                         199: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         202: <DUP>
                         203: <IFNONNULL 12>
                         206: <POP>
                         207: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         210: <LDC <String 'print'>>
                         212: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         215: <CHECKCAST <Class org/python/Callable>>
                         218: <ICONST_1>
                         219: <ANEWARRAY org/python/Object>
                         222: <DUP>
                         223: <ICONST_0>
                         224: <NEW org/python/Object>
                         227: <DUP>
                         228: <LDC <String 'Do final cleanup'>>
                         230: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         233: <AASTORE>
                         234: <NEW java/util/Hashtable>
                         237: <DUP>
                         238: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         241: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         246: <POP>
                         247: <ALOAD_0>
                         248: <ATHROW>
                         249: <ACONST_NULL>
                         250: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/BaseException: 0-27 [83]
                         finally: 0-27 [193]
                         finally: 83-137 [193]
                     Attributes: (1)
                         LineNumberTable (22 bytes)
                             Line numbers (5 total):
                                 0: 3
                                 27: 7
                                 84: 5
                                 137: 7
                                 194: 7
                """)

    def test_try_except_unnamed_finally(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except AttributeError:
                    print("Got an error")
                finally:
                    print("Do final cleanup")
                """,
            java="""
                 Code (315 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (251 bytes)
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
                          27: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          30: <LDC <String 'print'>>
                          32: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          35: <DUP>
                          36: <IFNONNULL 12>
                          39: <POP>
                          40: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          43: <LDC <String 'print'>>
                          45: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          48: <CHECKCAST <Class org/python/Callable>>
                          51: <ICONST_1>
                          52: <ANEWARRAY org/python/Object>
                          55: <DUP>
                          56: <ICONST_0>
                          57: <NEW org/python/Object>
                          60: <DUP>
                          61: <LDC <String 'Do final cleanup'>>
                          63: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          66: <AASTORE>
                          67: <NEW java/util/Hashtable>
                          70: <DUP>
                          71: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          74: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          79: <POP>
                          80: <GOTO 169>
                          83: <POP>
                          84: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          87: <LDC <String 'print'>>
                          89: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          92: <DUP>
                          93: <IFNONNULL 12>
                          96: <POP>
                          97: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         100: <LDC <String 'print'>>
                         102: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         105: <CHECKCAST <Class org/python/Callable>>
                         108: <ICONST_1>
                         109: <ANEWARRAY org/python/Object>
                         112: <DUP>
                         113: <ICONST_0>
                         114: <NEW org/python/Object>
                         117: <DUP>
                         118: <LDC <String 'Got an error'>>
                         120: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         123: <AASTORE>
                         124: <NEW java/util/Hashtable>
                         127: <DUP>
                         128: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         131: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         136: <POP>
                         137: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         140: <LDC <String 'print'>>
                         142: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         145: <DUP>
                         146: <IFNONNULL 12>
                         149: <POP>
                         150: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         153: <LDC <String 'print'>>
                         155: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         158: <CHECKCAST <Class org/python/Callable>>
                         161: <ICONST_1>
                         162: <ANEWARRAY org/python/Object>
                         165: <DUP>
                         166: <ICONST_0>
                         167: <NEW org/python/Object>
                         170: <DUP>
                         171: <LDC <String 'Do final cleanup'>>
                         173: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         176: <AASTORE>
                         177: <NEW java/util/Hashtable>
                         180: <DUP>
                         181: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         184: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         189: <POP>
                         190: <GOTO 59>
                         193: <ASTORE_0>
                         194: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         197: <LDC <String 'print'>>
                         199: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         202: <DUP>
                         203: <IFNONNULL 12>
                         206: <POP>
                         207: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         210: <LDC <String 'print'>>
                         212: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         215: <CHECKCAST <Class org/python/Callable>>
                         218: <ICONST_1>
                         219: <ANEWARRAY org/python/Object>
                         222: <DUP>
                         223: <ICONST_0>
                         224: <NEW org/python/Object>
                         227: <DUP>
                         228: <LDC <String 'Do final cleanup'>>
                         230: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         233: <AASTORE>
                         234: <NEW java/util/Hashtable>
                         237: <DUP>
                         238: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         241: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         246: <POP>
                         247: <ALOAD_0>
                         248: <ATHROW>
                         249: <ACONST_NULL>
                         250: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-27 [83]
                         finally: 0-27 [193]
                         finally: 83-137 [193]
                     Attributes: (1)
                         LineNumberTable (22 bytes)
                             Line numbers (5 total):
                                 0: 3
                                 27: 7
                                 84: 5
                                 137: 7
                                 194: 7
                """)

    def test_try_except_named_finally(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except AttributeError as e:
                    print("Got an AttributeError", e)
                finally:
                    print("Do final cleanup")
                """,
            java="""
                 Code (328 bytes)
                     Max stack: 10
                     Max locals: 2
                     Bytecode: (264 bytes)
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
                          27: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          30: <LDC <String 'print'>>
                          32: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          35: <DUP>
                          36: <IFNONNULL 12>
                          39: <POP>
                          40: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          43: <LDC <String 'print'>>
                          45: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          48: <CHECKCAST <Class org/python/Callable>>
                          51: <ICONST_1>
                          52: <ANEWARRAY org/python/Object>
                          55: <DUP>
                          56: <ICONST_0>
                          57: <NEW org/python/Object>
                          60: <DUP>
                          61: <LDC <String 'Do final cleanup'>>
                          63: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          66: <AASTORE>
                          67: <NEW java/util/Hashtable>
                          70: <DUP>
                          71: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          74: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          79: <POP>
                          80: <GOTO 182>
                          83: <ASTORE_0>
                          84: <NEW org/python/Object>
                          87: <DUP>
                          88: <ALOAD_0>
                          89: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                          92: <ASTORE_0>
                          93: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          96: <LDC <String 'print'>>
                          98: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         101: <DUP>
                         102: <IFNONNULL 12>
                         105: <POP>
                         106: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         109: <LDC <String 'print'>>
                         111: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         114: <CHECKCAST <Class org/python/Callable>>
                         117: <ICONST_2>
                         118: <ANEWARRAY org/python/Object>
                         121: <DUP>
                         122: <ICONST_0>
                         123: <NEW org/python/Object>
                         126: <DUP>
                         127: <LDC <String 'Got an AttributeError'>>
                         129: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         132: <AASTORE>
                         133: <DUP>
                         134: <ICONST_1>
                         135: <ALOAD_0>
                         136: <AASTORE>
                         137: <NEW java/util/Hashtable>
                         140: <DUP>
                         141: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         144: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         149: <POP>
                         150: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         153: <LDC <String 'print'>>
                         155: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         158: <DUP>
                         159: <IFNONNULL 12>
                         162: <POP>
                         163: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         166: <LDC <String 'print'>>
                         168: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         171: <CHECKCAST <Class org/python/Callable>>
                         174: <ICONST_1>
                         175: <ANEWARRAY org/python/Object>
                         178: <DUP>
                         179: <ICONST_0>
                         180: <NEW org/python/Object>
                         183: <DUP>
                         184: <LDC <String 'Do final cleanup'>>
                         186: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         189: <AASTORE>
                         190: <NEW java/util/Hashtable>
                         193: <DUP>
                         194: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         197: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         202: <POP>
                         203: <GOTO 59>
                         206: <ASTORE_1>
                         207: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         210: <LDC <String 'print'>>
                         212: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         215: <DUP>
                         216: <IFNONNULL 12>
                         219: <POP>
                         220: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         223: <LDC <String 'print'>>
                         225: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         228: <CHECKCAST <Class org/python/Callable>>
                         231: <ICONST_1>
                         232: <ANEWARRAY org/python/Object>
                         235: <DUP>
                         236: <ICONST_0>
                         237: <NEW org/python/Object>
                         240: <DUP>
                         241: <LDC <String 'Do final cleanup'>>
                         243: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         246: <AASTORE>
                         247: <NEW java/util/Hashtable>
                         250: <DUP>
                         251: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         254: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         259: <POP>
                         260: <ALOAD_1>
                         261: <ATHROW>
                         262: <ACONST_NULL>
                         263: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-27 [83]
                         finally: 0-27 [206]
                         finally: 83-150 [206]
                     Attributes: (1)
                         LineNumberTable (22 bytes)
                             Line numbers (5 total):
                                 0: 3
                                 27: 7
                                 93: 5
                                 150: 7
                                 207: 7
                """)

    def test_try_multiple_except_finally(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except AttributeError:
                    print("Got an AttributeError")
                except NameError as e:
                    print("Got a NameError", e)
                finally:
                    print("Do final cleanup")
                """,
            java="""
                 Code (462 bytes)
                     Max stack: 12
                     Max locals: 2
                     Bytecode: (374 bytes)
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
                          27: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          30: <LDC <String 'print'>>
                          32: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          35: <DUP>
                          36: <IFNONNULL 12>
                          39: <POP>
                          40: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          43: <LDC <String 'print'>>
                          45: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          48: <CHECKCAST <Class org/python/Callable>>
                          51: <ICONST_1>
                          52: <ANEWARRAY org/python/Object>
                          55: <DUP>
                          56: <ICONST_0>
                          57: <NEW org/python/Object>
                          60: <DUP>
                          61: <LDC <String 'Do final cleanup'>>
                          63: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          66: <AASTORE>
                          67: <NEW java/util/Hashtable>
                          70: <DUP>
                          71: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          74: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          79: <POP>
                          80: <GOTO 292>
                          83: <POP>
                          84: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          87: <LDC <String 'print'>>
                          89: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          92: <DUP>
                          93: <IFNONNULL 12>
                          96: <POP>
                          97: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         100: <LDC <String 'print'>>
                         102: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         105: <CHECKCAST <Class org/python/Callable>>
                         108: <ICONST_1>
                         109: <ANEWARRAY org/python/Object>
                         112: <DUP>
                         113: <ICONST_0>
                         114: <NEW org/python/Object>
                         117: <DUP>
                         118: <LDC <String 'Got an AttributeError'>>
                         120: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         123: <AASTORE>
                         124: <NEW java/util/Hashtable>
                         127: <DUP>
                         128: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         131: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         136: <POP>
                         137: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         140: <LDC <String 'print'>>
                         142: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         145: <DUP>
                         146: <IFNONNULL 12>
                         149: <POP>
                         150: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         153: <LDC <String 'print'>>
                         155: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         158: <CHECKCAST <Class org/python/Callable>>
                         161: <ICONST_1>
                         162: <ANEWARRAY org/python/Object>
                         165: <DUP>
                         166: <ICONST_0>
                         167: <NEW org/python/Object>
                         170: <DUP>
                         171: <LDC <String 'Do final cleanup'>>
                         173: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         176: <AASTORE>
                         177: <NEW java/util/Hashtable>
                         180: <DUP>
                         181: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         184: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         189: <POP>
                         190: <GOTO 182>
                         193: <ASTORE_0>
                         194: <NEW org/python/Object>
                         197: <DUP>
                         198: <ALOAD_0>
                         199: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                         202: <ASTORE_0>
                         203: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         206: <LDC <String 'print'>>
                         208: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         211: <DUP>
                         212: <IFNONNULL 12>
                         215: <POP>
                         216: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         219: <LDC <String 'print'>>
                         221: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         224: <CHECKCAST <Class org/python/Callable>>
                         227: <ICONST_2>
                         228: <ANEWARRAY org/python/Object>
                         231: <DUP>
                         232: <ICONST_0>
                         233: <NEW org/python/Object>
                         236: <DUP>
                         237: <LDC <String 'Got a NameError'>>
                         239: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         242: <AASTORE>
                         243: <DUP>
                         244: <ICONST_1>
                         245: <ALOAD_0>
                         246: <AASTORE>
                         247: <NEW java/util/Hashtable>
                         250: <DUP>
                         251: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         254: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         259: <POP>
                         260: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         263: <LDC <String 'print'>>
                         265: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         268: <DUP>
                         269: <IFNONNULL 12>
                         272: <POP>
                         273: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         276: <LDC <String 'print'>>
                         278: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         281: <CHECKCAST <Class org/python/Callable>>
                         284: <ICONST_1>
                         285: <ANEWARRAY org/python/Object>
                         288: <DUP>
                         289: <ICONST_0>
                         290: <NEW org/python/Object>
                         293: <DUP>
                         294: <LDC <String 'Do final cleanup'>>
                         296: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         299: <AASTORE>
                         300: <NEW java/util/Hashtable>
                         303: <DUP>
                         304: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         307: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         312: <POP>
                         313: <GOTO 59>
                         316: <ASTORE_1>
                         317: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         320: <LDC <String 'print'>>
                         322: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         325: <DUP>
                         326: <IFNONNULL 12>
                         329: <POP>
                         330: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         333: <LDC <String 'print'>>
                         335: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         338: <CHECKCAST <Class org/python/Callable>>
                         341: <ICONST_1>
                         342: <ANEWARRAY org/python/Object>
                         345: <DUP>
                         346: <ICONST_0>
                         347: <NEW org/python/Object>
                         350: <DUP>
                         351: <LDC <String 'Do final cleanup'>>
                         353: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         356: <AASTORE>
                         357: <NEW java/util/Hashtable>
                         360: <DUP>
                         361: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         364: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         369: <POP>
                         370: <ALOAD_1>
                         371: <ATHROW>
                         372: <ACONST_NULL>
                         373: <ARETURN>
                     Exceptions: (5)
                         org/python/exceptions/AttributeError: 0-27 [83]
                         org/python/exceptions/NameError: 0-27 [193]
                         finally: 0-27 [316]
                         finally: 83-137 [316]
                         finally: 193-260 [316]
                     Attributes: (1)
                         LineNumberTable (30 bytes)
                             Line numbers (7 total):
                                 0: 3
                                 27: 9
                                 84: 5
                                 137: 9
                                 203: 7
                                 260: 9
                                 317: 9
                """)


class TryExceptElseTests(TranspileTestCase):
    def test_try_except_else(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except:
                    print("Got an error")
                else:
                    print("Do else handling")
                """,
            java="""
                 Code (179 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (139 bytes)
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
                          27: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          30: <LDC <String 'print'>>
                          32: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          35: <DUP>
                          36: <IFNONNULL 12>
                          39: <POP>
                          40: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          43: <LDC <String 'print'>>
                          45: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          48: <CHECKCAST <Class org/python/Callable>>
                          51: <ICONST_1>
                          52: <ANEWARRAY org/python/Object>
                          55: <DUP>
                          56: <ICONST_0>
                          57: <NEW org/python/Object>
                          60: <DUP>
                          61: <LDC <String 'Do else handling'>>
                          63: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          66: <AASTORE>
                          67: <NEW java/util/Hashtable>
                          70: <DUP>
                          71: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          74: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          79: <POP>
                          80: <GOTO 57>
                          83: <POP>
                          84: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          87: <LDC <String 'print'>>
                          89: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          92: <DUP>
                          93: <IFNONNULL 12>
                          96: <POP>
                          97: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         100: <LDC <String 'print'>>
                         102: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         105: <CHECKCAST <Class org/python/Callable>>
                         108: <ICONST_1>
                         109: <ANEWARRAY org/python/Object>
                         112: <DUP>
                         113: <ICONST_0>
                         114: <NEW org/python/Object>
                         117: <DUP>
                         118: <LDC <String 'Got an error'>>
                         120: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         123: <AASTORE>
                         124: <NEW java/util/Hashtable>
                         127: <DUP>
                         128: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         131: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         136: <POP>
                         137: <ACONST_NULL>
                         138: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/BaseException: 0-27 [83]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 27: 7
                                 84: 5
                """)

    def test_try_except_unnamed_else(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except AttributeError:
                    print("Got an error")
                else:
                    print("Do else handling")
                """,
            java="""
                 Code (179 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (139 bytes)
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
                          27: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          30: <LDC <String 'print'>>
                          32: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          35: <DUP>
                          36: <IFNONNULL 12>
                          39: <POP>
                          40: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          43: <LDC <String 'print'>>
                          45: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          48: <CHECKCAST <Class org/python/Callable>>
                          51: <ICONST_1>
                          52: <ANEWARRAY org/python/Object>
                          55: <DUP>
                          56: <ICONST_0>
                          57: <NEW org/python/Object>
                          60: <DUP>
                          61: <LDC <String 'Do else handling'>>
                          63: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          66: <AASTORE>
                          67: <NEW java/util/Hashtable>
                          70: <DUP>
                          71: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          74: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          79: <POP>
                          80: <GOTO 57>
                          83: <POP>
                          84: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          87: <LDC <String 'print'>>
                          89: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          92: <DUP>
                          93: <IFNONNULL 12>
                          96: <POP>
                          97: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         100: <LDC <String 'print'>>
                         102: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         105: <CHECKCAST <Class org/python/Callable>>
                         108: <ICONST_1>
                         109: <ANEWARRAY org/python/Object>
                         112: <DUP>
                         113: <ICONST_0>
                         114: <NEW org/python/Object>
                         117: <DUP>
                         118: <LDC <String 'Got an error'>>
                         120: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         123: <AASTORE>
                         124: <NEW java/util/Hashtable>
                         127: <DUP>
                         128: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         131: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         136: <POP>
                         137: <ACONST_NULL>
                         138: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/AttributeError: 0-27 [83]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 27: 7
                                 84: 5
                """)

    def test_try_multiple_except_else(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except AttributeError:
                    print("Got an AttributeError")
                except NameError as e:
                    print("Got a NameError", e)
                else:
                    print("Do else handling")
                """,
            java="""
                 Code (261 bytes)
                     Max stack: 9
                     Max locals: 1
                     Bytecode: (209 bytes)
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
                          27: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          30: <LDC <String 'print'>>
                          32: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          35: <DUP>
                          36: <IFNONNULL 12>
                          39: <POP>
                          40: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          43: <LDC <String 'print'>>
                          45: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          48: <CHECKCAST <Class org/python/Callable>>
                          51: <ICONST_1>
                          52: <ANEWARRAY org/python/Object>
                          55: <DUP>
                          56: <ICONST_0>
                          57: <NEW org/python/Object>
                          60: <DUP>
                          61: <LDC <String 'Do else handling'>>
                          63: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          66: <AASTORE>
                          67: <NEW java/util/Hashtable>
                          70: <DUP>
                          71: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          74: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          79: <POP>
                          80: <GOTO 127>
                          83: <POP>
                          84: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          87: <LDC <String 'print'>>
                          89: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          92: <DUP>
                          93: <IFNONNULL 12>
                          96: <POP>
                          97: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         100: <LDC <String 'print'>>
                         102: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         105: <CHECKCAST <Class org/python/Callable>>
                         108: <ICONST_1>
                         109: <ANEWARRAY org/python/Object>
                         112: <DUP>
                         113: <ICONST_0>
                         114: <NEW org/python/Object>
                         117: <DUP>
                         118: <LDC <String 'Got an AttributeError'>>
                         120: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         123: <AASTORE>
                         124: <NEW java/util/Hashtable>
                         127: <DUP>
                         128: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         131: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         136: <POP>
                         137: <GOTO 70>
                         140: <ASTORE_0>
                         141: <NEW org/python/Object>
                         144: <DUP>
                         145: <ALOAD_0>
                         146: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                         149: <ASTORE_0>
                         150: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         153: <LDC <String 'print'>>
                         155: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         158: <DUP>
                         159: <IFNONNULL 12>
                         162: <POP>
                         163: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         166: <LDC <String 'print'>>
                         168: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         171: <CHECKCAST <Class org/python/Callable>>
                         174: <ICONST_2>
                         175: <ANEWARRAY org/python/Object>
                         178: <DUP>
                         179: <ICONST_0>
                         180: <NEW org/python/Object>
                         183: <DUP>
                         184: <LDC <String 'Got a NameError'>>
                         186: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         189: <AASTORE>
                         190: <DUP>
                         191: <ICONST_1>
                         192: <ALOAD_0>
                         193: <AASTORE>
                         194: <NEW java/util/Hashtable>
                         197: <DUP>
                         198: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         201: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         206: <POP>
                         207: <ACONST_NULL>
                         208: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-27 [83]
                         org/python/exceptions/NameError: 0-27 [140]
                     Attributes: (1)
                         LineNumberTable (18 bytes)
                             Line numbers (4 total):
                                 0: 3
                                 27: 9
                                 84: 5
                                 150: 7
                """)


class TryExceptElseFinallyTests(TranspileTestCase):
    def test_try_except_else(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except:
                    print("Got an error")
                else:
                    print("Do else handling")
                finally:
                    print("Do final cleanup")
                """,
            java="""
                 Code (372 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (304 bytes)
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
                          27: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          30: <LDC <String 'print'>>
                          32: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          35: <DUP>
                          36: <IFNONNULL 12>
                          39: <POP>
                          40: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          43: <LDC <String 'print'>>
                          45: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          48: <CHECKCAST <Class org/python/Callable>>
                          51: <ICONST_1>
                          52: <ANEWARRAY org/python/Object>
                          55: <DUP>
                          56: <ICONST_0>
                          57: <NEW org/python/Object>
                          60: <DUP>
                          61: <LDC <String 'Do else handling'>>
                          63: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          66: <AASTORE>
                          67: <NEW java/util/Hashtable>
                          70: <DUP>
                          71: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          74: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          79: <POP>
                          80: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          83: <LDC <String 'print'>>
                          85: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          88: <DUP>
                          89: <IFNONNULL 12>
                          92: <POP>
                          93: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          96: <LDC <String 'print'>>
                          98: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         101: <CHECKCAST <Class org/python/Callable>>
                         104: <ICONST_1>
                         105: <ANEWARRAY org/python/Object>
                         108: <DUP>
                         109: <ICONST_0>
                         110: <NEW org/python/Object>
                         113: <DUP>
                         114: <LDC <String 'Do final cleanup'>>
                         116: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         119: <AASTORE>
                         120: <NEW java/util/Hashtable>
                         123: <DUP>
                         124: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         127: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         132: <POP>
                         133: <GOTO 169>
                         136: <POP>
                         137: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         140: <LDC <String 'print'>>
                         142: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         145: <DUP>
                         146: <IFNONNULL 12>
                         149: <POP>
                         150: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         153: <LDC <String 'print'>>
                         155: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         158: <CHECKCAST <Class org/python/Callable>>
                         161: <ICONST_1>
                         162: <ANEWARRAY org/python/Object>
                         165: <DUP>
                         166: <ICONST_0>
                         167: <NEW org/python/Object>
                         170: <DUP>
                         171: <LDC <String 'Got an error'>>
                         173: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         176: <AASTORE>
                         177: <NEW java/util/Hashtable>
                         180: <DUP>
                         181: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         184: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         189: <POP>
                         190: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         193: <LDC <String 'print'>>
                         195: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         198: <DUP>
                         199: <IFNONNULL 12>
                         202: <POP>
                         203: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         206: <LDC <String 'print'>>
                         208: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         211: <CHECKCAST <Class org/python/Callable>>
                         214: <ICONST_1>
                         215: <ANEWARRAY org/python/Object>
                         218: <DUP>
                         219: <ICONST_0>
                         220: <NEW org/python/Object>
                         223: <DUP>
                         224: <LDC <String 'Do final cleanup'>>
                         226: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         229: <AASTORE>
                         230: <NEW java/util/Hashtable>
                         233: <DUP>
                         234: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         237: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         242: <POP>
                         243: <GOTO 59>
                         246: <ASTORE_0>
                         247: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         250: <LDC <String 'print'>>
                         252: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         255: <DUP>
                         256: <IFNONNULL 12>
                         259: <POP>
                         260: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         263: <LDC <String 'print'>>
                         265: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         268: <CHECKCAST <Class org/python/Callable>>
                         271: <ICONST_1>
                         272: <ANEWARRAY org/python/Object>
                         275: <DUP>
                         276: <ICONST_0>
                         277: <NEW org/python/Object>
                         280: <DUP>
                         281: <LDC <String 'Do final cleanup'>>
                         283: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         286: <AASTORE>
                         287: <NEW java/util/Hashtable>
                         290: <DUP>
                         291: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         294: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         299: <POP>
                         300: <ALOAD_0>
                         301: <ATHROW>
                         302: <ACONST_NULL>
                         303: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/BaseException: 0-27 [136]
                         finally: 0-27 [246]
                         finally: 136-190 [246]
                     Attributes: (1)
                         LineNumberTable (26 bytes)
                             Line numbers (6 total):
                                 0: 3
                                 27: 7
                                 80: 9
                                 137: 5
                                 190: 9
                                 247: 9
                """)

    def test_try_except_unnamed_else(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except AttributeError:
                    print("Got an error")
                else:
                    print("Do else handling")
                finally:
                    print("Do final cleanup")
                """,
            java="""
                 Code (372 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (304 bytes)
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
                          27: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          30: <LDC <String 'print'>>
                          32: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          35: <DUP>
                          36: <IFNONNULL 12>
                          39: <POP>
                          40: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          43: <LDC <String 'print'>>
                          45: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          48: <CHECKCAST <Class org/python/Callable>>
                          51: <ICONST_1>
                          52: <ANEWARRAY org/python/Object>
                          55: <DUP>
                          56: <ICONST_0>
                          57: <NEW org/python/Object>
                          60: <DUP>
                          61: <LDC <String 'Do else handling'>>
                          63: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          66: <AASTORE>
                          67: <NEW java/util/Hashtable>
                          70: <DUP>
                          71: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          74: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          79: <POP>
                          80: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          83: <LDC <String 'print'>>
                          85: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          88: <DUP>
                          89: <IFNONNULL 12>
                          92: <POP>
                          93: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          96: <LDC <String 'print'>>
                          98: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         101: <CHECKCAST <Class org/python/Callable>>
                         104: <ICONST_1>
                         105: <ANEWARRAY org/python/Object>
                         108: <DUP>
                         109: <ICONST_0>
                         110: <NEW org/python/Object>
                         113: <DUP>
                         114: <LDC <String 'Do final cleanup'>>
                         116: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         119: <AASTORE>
                         120: <NEW java/util/Hashtable>
                         123: <DUP>
                         124: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         127: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         132: <POP>
                         133: <GOTO 169>
                         136: <POP>
                         137: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         140: <LDC <String 'print'>>
                         142: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         145: <DUP>
                         146: <IFNONNULL 12>
                         149: <POP>
                         150: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         153: <LDC <String 'print'>>
                         155: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         158: <CHECKCAST <Class org/python/Callable>>
                         161: <ICONST_1>
                         162: <ANEWARRAY org/python/Object>
                         165: <DUP>
                         166: <ICONST_0>
                         167: <NEW org/python/Object>
                         170: <DUP>
                         171: <LDC <String 'Got an error'>>
                         173: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         176: <AASTORE>
                         177: <NEW java/util/Hashtable>
                         180: <DUP>
                         181: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         184: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         189: <POP>
                         190: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         193: <LDC <String 'print'>>
                         195: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         198: <DUP>
                         199: <IFNONNULL 12>
                         202: <POP>
                         203: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         206: <LDC <String 'print'>>
                         208: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         211: <CHECKCAST <Class org/python/Callable>>
                         214: <ICONST_1>
                         215: <ANEWARRAY org/python/Object>
                         218: <DUP>
                         219: <ICONST_0>
                         220: <NEW org/python/Object>
                         223: <DUP>
                         224: <LDC <String 'Do final cleanup'>>
                         226: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         229: <AASTORE>
                         230: <NEW java/util/Hashtable>
                         233: <DUP>
                         234: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         237: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         242: <POP>
                         243: <GOTO 59>
                         246: <ASTORE_0>
                         247: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         250: <LDC <String 'print'>>
                         252: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         255: <DUP>
                         256: <IFNONNULL 12>
                         259: <POP>
                         260: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         263: <LDC <String 'print'>>
                         265: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         268: <CHECKCAST <Class org/python/Callable>>
                         271: <ICONST_1>
                         272: <ANEWARRAY org/python/Object>
                         275: <DUP>
                         276: <ICONST_0>
                         277: <NEW org/python/Object>
                         280: <DUP>
                         281: <LDC <String 'Do final cleanup'>>
                         283: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         286: <AASTORE>
                         287: <NEW java/util/Hashtable>
                         290: <DUP>
                         291: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         294: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         299: <POP>
                         300: <ALOAD_0>
                         301: <ATHROW>
                         302: <ACONST_NULL>
                         303: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-27 [136]
                         finally: 0-27 [246]
                         finally: 136-190 [246]
                     Attributes: (1)
                         LineNumberTable (26 bytes)
                             Line numbers (6 total):
                                 0: 3
                                 27: 7
                                 80: 9
                                 137: 5
                                 190: 9
                                 247: 9
                """)

    def test_try_multiple_except_else(self):
        self.assertBlock(
            python="""
                try:
                    obj.no_such_attribute
                except AttributeError:
                    print("Got an AttributeError")
                except NameError as e:
                    print("Got a NameError", e)
                else:
                    print("Do else handling")
                finally:
                    print("Do final cleanup")
                """,
            java="""
                 Code (519 bytes)
                     Max stack: 12
                     Max locals: 2
                     Bytecode: (427 bytes)
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
                          27: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          30: <LDC <String 'print'>>
                          32: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          35: <DUP>
                          36: <IFNONNULL 12>
                          39: <POP>
                          40: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          43: <LDC <String 'print'>>
                          45: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          48: <CHECKCAST <Class org/python/Callable>>
                          51: <ICONST_1>
                          52: <ANEWARRAY org/python/Object>
                          55: <DUP>
                          56: <ICONST_0>
                          57: <NEW org/python/Object>
                          60: <DUP>
                          61: <LDC <String 'Do else handling'>>
                          63: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                          66: <AASTORE>
                          67: <NEW java/util/Hashtable>
                          70: <DUP>
                          71: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          74: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          79: <POP>
                          80: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          83: <LDC <String 'print'>>
                          85: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          88: <DUP>
                          89: <IFNONNULL 12>
                          92: <POP>
                          93: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          96: <LDC <String 'print'>>
                          98: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         101: <CHECKCAST <Class org/python/Callable>>
                         104: <ICONST_1>
                         105: <ANEWARRAY org/python/Object>
                         108: <DUP>
                         109: <ICONST_0>
                         110: <NEW org/python/Object>
                         113: <DUP>
                         114: <LDC <String 'Do final cleanup'>>
                         116: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         119: <AASTORE>
                         120: <NEW java/util/Hashtable>
                         123: <DUP>
                         124: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         127: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         132: <POP>
                         133: <GOTO 292>
                         136: <POP>
                         137: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         140: <LDC <String 'print'>>
                         142: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         145: <DUP>
                         146: <IFNONNULL 12>
                         149: <POP>
                         150: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         153: <LDC <String 'print'>>
                         155: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         158: <CHECKCAST <Class org/python/Callable>>
                         161: <ICONST_1>
                         162: <ANEWARRAY org/python/Object>
                         165: <DUP>
                         166: <ICONST_0>
                         167: <NEW org/python/Object>
                         170: <DUP>
                         171: <LDC <String 'Got an AttributeError'>>
                         173: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         176: <AASTORE>
                         177: <NEW java/util/Hashtable>
                         180: <DUP>
                         181: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         184: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         189: <POP>
                         190: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         193: <LDC <String 'print'>>
                         195: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         198: <DUP>
                         199: <IFNONNULL 12>
                         202: <POP>
                         203: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         206: <LDC <String 'print'>>
                         208: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         211: <CHECKCAST <Class org/python/Callable>>
                         214: <ICONST_1>
                         215: <ANEWARRAY org/python/Object>
                         218: <DUP>
                         219: <ICONST_0>
                         220: <NEW org/python/Object>
                         223: <DUP>
                         224: <LDC <String 'Do final cleanup'>>
                         226: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         229: <AASTORE>
                         230: <NEW java/util/Hashtable>
                         233: <DUP>
                         234: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         237: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         242: <POP>
                         243: <GOTO 182>
                         246: <ASTORE_0>
                         247: <NEW org/python/Object>
                         250: <DUP>
                         251: <ALOAD_0>
                         252: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                         255: <ASTORE_0>
                         256: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         259: <LDC <String 'print'>>
                         261: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         264: <DUP>
                         265: <IFNONNULL 12>
                         268: <POP>
                         269: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         272: <LDC <String 'print'>>
                         274: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         277: <CHECKCAST <Class org/python/Callable>>
                         280: <ICONST_2>
                         281: <ANEWARRAY org/python/Object>
                         284: <DUP>
                         285: <ICONST_0>
                         286: <NEW org/python/Object>
                         289: <DUP>
                         290: <LDC <String 'Got a NameError'>>
                         292: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         295: <AASTORE>
                         296: <DUP>
                         297: <ICONST_1>
                         298: <ALOAD_0>
                         299: <AASTORE>
                         300: <NEW java/util/Hashtable>
                         303: <DUP>
                         304: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         307: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         312: <POP>
                         313: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         316: <LDC <String 'print'>>
                         318: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         321: <DUP>
                         322: <IFNONNULL 12>
                         325: <POP>
                         326: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         329: <LDC <String 'print'>>
                         331: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         334: <CHECKCAST <Class org/python/Callable>>
                         337: <ICONST_1>
                         338: <ANEWARRAY org/python/Object>
                         341: <DUP>
                         342: <ICONST_0>
                         343: <NEW org/python/Object>
                         346: <DUP>
                         347: <LDC <String 'Do final cleanup'>>
                         349: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         352: <AASTORE>
                         353: <NEW java/util/Hashtable>
                         356: <DUP>
                         357: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         360: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         365: <POP>
                         366: <GOTO 59>
                         369: <ASTORE_1>
                         370: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         373: <LDC <String 'print'>>
                         375: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         378: <DUP>
                         379: <IFNONNULL 12>
                         382: <POP>
                         383: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         386: <LDC <String 'print'>>
                         388: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         391: <CHECKCAST <Class org/python/Callable>>
                         394: <ICONST_1>
                         395: <ANEWARRAY org/python/Object>
                         398: <DUP>
                         399: <ICONST_0>
                         400: <NEW org/python/Object>
                         403: <DUP>
                         404: <LDC <String 'Do final cleanup'>>
                         406: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         409: <AASTORE>
                         410: <NEW java/util/Hashtable>
                         413: <DUP>
                         414: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         417: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         422: <POP>
                         423: <ALOAD_1>
                         424: <ATHROW>
                         425: <ACONST_NULL>
                         426: <ARETURN>
                     Exceptions: (5)
                         org/python/exceptions/AttributeError: 0-27 [136]
                         org/python/exceptions/NameError: 0-27 [246]
                         finally: 0-27 [369]
                         finally: 136-190 [369]
                         finally: 246-313 [369]
                     Attributes: (1)
                         LineNumberTable (34 bytes)
                             Line numbers (8 total):
                                 0: 3
                                 27: 9
                                 80: 11
                                 137: 5
                                 190: 11
                                 256: 7
                                 313: 11
                                 370: 11
                """)
