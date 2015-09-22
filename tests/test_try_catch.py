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
    #             except:
    #                 print("Got an error")
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)

    # def test_try_except_named_finally(self):
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

    # def test_try_multiple_except_mixed3_finally(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError, e:
    #                 print("Got an AttributeError")
    #             except NameError:
    #                 print("Got a NameError")
    #             except:
    #                 print("Got an anonymous error")
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
    #             except:
    #                 print("Got an error")
    #             else:
    #                 print("Do else handling")
    #             """,
    #         java="""
    #             """)

    # def test_try_except_unnamed_else(self):
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

    # def test_try_multiple_except_mixed3_else(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError, e:
    #                 print("Got an AttributeError")
    #             except NameError:
    #                 print("Got a NameError")
    #             except:
    #                 print("Got an anonymous error")
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
    #             except:
    #                 print("Got an error")
    #             else:
    #                 print("Do else handling")
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)

    # def test_try_except_else_unnamed_finally(self):
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

    # def test_try_multiple_except_mixed3_else_finally(self):
    #     self.assertBlock(
    #         python="""
    #             try:
    #                 obj.no_such_attribute
    #             except AttributeError, e:
    #                 print("Got an AttributeError")
    #             except NameError:
    #                 print("Got a NameError")
    #             except:
    #                 print("Got an anonymous error")
    #             else:
    #                 print("Do else handling")
    #             finally:
    #                 print("Do final cleanup")
    #             """,
    #         java="""
    #             """)
