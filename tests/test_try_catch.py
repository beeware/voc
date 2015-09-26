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
                 Code (160 bytes)
                     Max stack: 7
                     Max locals: 0
                     Bytecode: (124 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GOTO 75>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC <String 'print'>>
                          56: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          59: <DUP>
                          60: <IFNONNULL 27>
                          63: <POP>
                          64: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          67: <LDC <String 'print'>>
                          69: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          72: <DUP>
                          73: <IFNONNULL 14>
                          76: <POP>
                          77: <NEW org/python/exceptions/NameError>
                          80: <DUP>
                          81: <LDC <String 'print'>>
                          83: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          86: <ATHROW>
                          87: <CHECKCAST <Class org/python/types/Object>>
                          90: <CHECKCAST <Class org/python/Callable>>
                          93: <ICONST_1>
                          94: <ANEWARRAY org/python/Object>
                          97: <DUP>
                          98: <ICONST_0>
                          99: <NEW org/python/types/Str>
                         102: <DUP>
                         103: <LDC <String 'Got an error'>>
                         105: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         108: <AASTORE>
                         109: <NEW java/util/Hashtable>
                         112: <DUP>
                         113: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         116: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         121: <POP>
                         122: <ACONST_NULL>
                         123: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/BaseException: 0-47 [50]
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 3
                                 51: 5
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
                 Code (160 bytes)
                     Max stack: 7
                     Max locals: 0
                     Bytecode: (124 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GOTO 75>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC <String 'print'>>
                          56: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          59: <DUP>
                          60: <IFNONNULL 27>
                          63: <POP>
                          64: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          67: <LDC <String 'print'>>
                          69: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          72: <DUP>
                          73: <IFNONNULL 14>
                          76: <POP>
                          77: <NEW org/python/exceptions/NameError>
                          80: <DUP>
                          81: <LDC <String 'print'>>
                          83: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          86: <ATHROW>
                          87: <CHECKCAST <Class org/python/types/Object>>
                          90: <CHECKCAST <Class org/python/Callable>>
                          93: <ICONST_1>
                          94: <ANEWARRAY org/python/Object>
                          97: <DUP>
                          98: <ICONST_0>
                          99: <NEW org/python/types/Str>
                         102: <DUP>
                         103: <LDC <String 'Got an error'>>
                         105: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         108: <AASTORE>
                         109: <NEW java/util/Hashtable>
                         112: <DUP>
                         113: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         116: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         121: <POP>
                         122: <ACONST_NULL>
                         123: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/AttributeError: 0-47 [50]
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 3
                                 51: 5
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
                 Code (164 bytes)
                     Max stack: 7
                     Max locals: 1
                     Bytecode: (128 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GOTO 79>
                          50: <ASTORE_0>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC <String 'print'>>
                          56: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          59: <DUP>
                          60: <IFNONNULL 27>
                          63: <POP>
                          64: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          67: <LDC <String 'print'>>
                          69: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          72: <DUP>
                          73: <IFNONNULL 14>
                          76: <POP>
                          77: <NEW org/python/exceptions/NameError>
                          80: <DUP>
                          81: <LDC <String 'print'>>
                          83: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          86: <ATHROW>
                          87: <CHECKCAST <Class org/python/types/Object>>
                          90: <CHECKCAST <Class org/python/Callable>>
                          93: <ICONST_2>
                          94: <ANEWARRAY org/python/Object>
                          97: <DUP>
                          98: <ICONST_0>
                          99: <NEW org/python/types/Str>
                         102: <DUP>
                         103: <LDC <String 'Got an error'>>
                         105: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         108: <AASTORE>
                         109: <DUP>
                         110: <ICONST_1>
                         111: <ALOAD_0>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <ACONST_NULL>
                         127: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/AttributeError: 0-47 [50]
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 3
                                 51: 5
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
                 Code (247 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (199 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GOTO 150>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC <String 'print'>>
                          56: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          59: <DUP>
                          60: <IFNONNULL 27>
                          63: <POP>
                          64: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          67: <LDC <String 'print'>>
                          69: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          72: <DUP>
                          73: <IFNONNULL 14>
                          76: <POP>
                          77: <NEW org/python/exceptions/NameError>
                          80: <DUP>
                          81: <LDC <String 'print'>>
                          83: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          86: <ATHROW>
                          87: <CHECKCAST <Class org/python/types/Object>>
                          90: <CHECKCAST <Class org/python/Callable>>
                          93: <ICONST_1>
                          94: <ANEWARRAY org/python/Object>
                          97: <DUP>
                          98: <ICONST_0>
                          99: <NEW org/python/types/Str>
                         102: <DUP>
                         103: <LDC <String 'Got an AttributeError'>>
                         105: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         108: <AASTORE>
                         109: <NEW java/util/Hashtable>
                         112: <DUP>
                         113: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         116: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         121: <POP>
                         122: <GOTO 75>
                         125: <POP>
                         126: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         129: <LDC <String 'print'>>
                         131: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         134: <DUP>
                         135: <IFNONNULL 27>
                         138: <POP>
                         139: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         142: <LDC <String 'print'>>
                         144: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         147: <DUP>
                         148: <IFNONNULL 14>
                         151: <POP>
                         152: <NEW org/python/exceptions/NameError>
                         155: <DUP>
                         156: <LDC <String 'print'>>
                         158: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         161: <ATHROW>
                         162: <CHECKCAST <Class org/python/types/Object>>
                         165: <CHECKCAST <Class org/python/Callable>>
                         168: <ICONST_1>
                         169: <ANEWARRAY org/python/Object>
                         172: <DUP>
                         173: <ICONST_0>
                         174: <NEW org/python/types/Str>
                         177: <DUP>
                         178: <LDC <String 'Got a NameError'>>
                         180: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         183: <AASTORE>
                         184: <NEW java/util/Hashtable>
                         187: <DUP>
                         188: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         191: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         196: <POP>
                         197: <ACONST_NULL>
                         198: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-47 [50]
                         org/python/exceptions/NameError: 0-47 [125]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 51: 5
                                 126: 7
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
                 Code (255 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (207 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GOTO 158>
                          50: <ASTORE_0>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC <String 'print'>>
                          56: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          59: <DUP>
                          60: <IFNONNULL 27>
                          63: <POP>
                          64: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          67: <LDC <String 'print'>>
                          69: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          72: <DUP>
                          73: <IFNONNULL 14>
                          76: <POP>
                          77: <NEW org/python/exceptions/NameError>
                          80: <DUP>
                          81: <LDC <String 'print'>>
                          83: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          86: <ATHROW>
                          87: <CHECKCAST <Class org/python/types/Object>>
                          90: <CHECKCAST <Class org/python/Callable>>
                          93: <ICONST_2>
                          94: <ANEWARRAY org/python/Object>
                          97: <DUP>
                          98: <ICONST_0>
                          99: <NEW org/python/types/Str>
                         102: <DUP>
                         103: <LDC <String 'Got an AttributeError'>>
                         105: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         108: <AASTORE>
                         109: <DUP>
                         110: <ICONST_1>
                         111: <ALOAD_0>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <GOTO 79>
                         129: <ASTORE_0>
                         130: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         133: <LDC <String 'print'>>
                         135: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         138: <DUP>
                         139: <IFNONNULL 27>
                         142: <POP>
                         143: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         146: <LDC <String 'print'>>
                         148: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         151: <DUP>
                         152: <IFNONNULL 14>
                         155: <POP>
                         156: <NEW org/python/exceptions/NameError>
                         159: <DUP>
                         160: <LDC <String 'print'>>
                         162: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         165: <ATHROW>
                         166: <CHECKCAST <Class org/python/types/Object>>
                         169: <CHECKCAST <Class org/python/Callable>>
                         172: <ICONST_2>
                         173: <ANEWARRAY org/python/Object>
                         176: <DUP>
                         177: <ICONST_0>
                         178: <NEW org/python/types/Str>
                         181: <DUP>
                         182: <LDC <String 'Got a NameError'>>
                         184: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         187: <AASTORE>
                         188: <DUP>
                         189: <ICONST_1>
                         190: <ALOAD_0>
                         191: <AASTORE>
                         192: <NEW java/util/Hashtable>
                         195: <DUP>
                         196: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         199: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         204: <POP>
                         205: <ACONST_NULL>
                         206: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-47 [50]
                         org/python/exceptions/NameError: 0-47 [129]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 51: 5
                                 130: 7
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
                 Code (247 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (199 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GOTO 150>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC <String 'print'>>
                          56: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          59: <DUP>
                          60: <IFNONNULL 27>
                          63: <POP>
                          64: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          67: <LDC <String 'print'>>
                          69: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          72: <DUP>
                          73: <IFNONNULL 14>
                          76: <POP>
                          77: <NEW org/python/exceptions/NameError>
                          80: <DUP>
                          81: <LDC <String 'print'>>
                          83: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          86: <ATHROW>
                          87: <CHECKCAST <Class org/python/types/Object>>
                          90: <CHECKCAST <Class org/python/Callable>>
                          93: <ICONST_1>
                          94: <ANEWARRAY org/python/Object>
                          97: <DUP>
                          98: <ICONST_0>
                          99: <NEW org/python/types/Str>
                         102: <DUP>
                         103: <LDC <String 'Got an AttributeError'>>
                         105: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         108: <AASTORE>
                         109: <NEW java/util/Hashtable>
                         112: <DUP>
                         113: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         116: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         121: <POP>
                         122: <GOTO 75>
                         125: <POP>
                         126: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         129: <LDC <String 'print'>>
                         131: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         134: <DUP>
                         135: <IFNONNULL 27>
                         138: <POP>
                         139: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         142: <LDC <String 'print'>>
                         144: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         147: <DUP>
                         148: <IFNONNULL 14>
                         151: <POP>
                         152: <NEW org/python/exceptions/NameError>
                         155: <DUP>
                         156: <LDC <String 'print'>>
                         158: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         161: <ATHROW>
                         162: <CHECKCAST <Class org/python/types/Object>>
                         165: <CHECKCAST <Class org/python/Callable>>
                         168: <ICONST_1>
                         169: <ANEWARRAY org/python/Object>
                         172: <DUP>
                         173: <ICONST_0>
                         174: <NEW org/python/types/Str>
                         177: <DUP>
                         178: <LDC <String 'Got a NameError'>>
                         180: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         183: <AASTORE>
                         184: <NEW java/util/Hashtable>
                         187: <DUP>
                         188: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         191: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         196: <POP>
                         197: <ACONST_NULL>
                         198: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-47 [50]
                         org/python/exceptions/NameError: 0-47 [125]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 51: 5
                                 126: 7
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
                 Code (255 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (207 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GOTO 158>
                          50: <ASTORE_0>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC <String 'print'>>
                          56: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          59: <DUP>
                          60: <IFNONNULL 27>
                          63: <POP>
                          64: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          67: <LDC <String 'print'>>
                          69: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          72: <DUP>
                          73: <IFNONNULL 14>
                          76: <POP>
                          77: <NEW org/python/exceptions/NameError>
                          80: <DUP>
                          81: <LDC <String 'print'>>
                          83: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          86: <ATHROW>
                          87: <CHECKCAST <Class org/python/types/Object>>
                          90: <CHECKCAST <Class org/python/Callable>>
                          93: <ICONST_2>
                          94: <ANEWARRAY org/python/Object>
                          97: <DUP>
                          98: <ICONST_0>
                          99: <NEW org/python/types/Str>
                         102: <DUP>
                         103: <LDC <String 'Got an AttributeError'>>
                         105: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         108: <AASTORE>
                         109: <DUP>
                         110: <ICONST_1>
                         111: <ALOAD_0>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <GOTO 79>
                         129: <ASTORE_0>
                         130: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         133: <LDC <String 'print'>>
                         135: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         138: <DUP>
                         139: <IFNONNULL 27>
                         142: <POP>
                         143: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         146: <LDC <String 'print'>>
                         148: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         151: <DUP>
                         152: <IFNONNULL 14>
                         155: <POP>
                         156: <NEW org/python/exceptions/NameError>
                         159: <DUP>
                         160: <LDC <String 'print'>>
                         162: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         165: <ATHROW>
                         166: <CHECKCAST <Class org/python/types/Object>>
                         169: <CHECKCAST <Class org/python/Callable>>
                         172: <ICONST_2>
                         173: <ANEWARRAY org/python/Object>
                         176: <DUP>
                         177: <ICONST_0>
                         178: <NEW org/python/types/Str>
                         181: <DUP>
                         182: <LDC <String 'Got a NameError'>>
                         184: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         187: <AASTORE>
                         188: <DUP>
                         189: <ICONST_1>
                         190: <ALOAD_0>
                         191: <AASTORE>
                         192: <NEW java/util/Hashtable>
                         195: <DUP>
                         196: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         199: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         204: <POP>
                         205: <ACONST_NULL>
                         206: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-47 [50]
                         org/python/exceptions/NameError: 0-47 [129]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 51: 5
                                 130: 7
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
                 Code (251 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (203 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GOTO 154>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC <String 'print'>>
                          56: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          59: <DUP>
                          60: <IFNONNULL 27>
                          63: <POP>
                          64: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          67: <LDC <String 'print'>>
                          69: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          72: <DUP>
                          73: <IFNONNULL 14>
                          76: <POP>
                          77: <NEW org/python/exceptions/NameError>
                          80: <DUP>
                          81: <LDC <String 'print'>>
                          83: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          86: <ATHROW>
                          87: <CHECKCAST <Class org/python/types/Object>>
                          90: <CHECKCAST <Class org/python/Callable>>
                          93: <ICONST_1>
                          94: <ANEWARRAY org/python/Object>
                          97: <DUP>
                          98: <ICONST_0>
                          99: <NEW org/python/types/Str>
                         102: <DUP>
                         103: <LDC <String 'Got an AttributeError'>>
                         105: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         108: <AASTORE>
                         109: <NEW java/util/Hashtable>
                         112: <DUP>
                         113: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         116: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         121: <POP>
                         122: <GOTO 79>
                         125: <ASTORE_0>
                         126: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         129: <LDC <String 'print'>>
                         131: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         134: <DUP>
                         135: <IFNONNULL 27>
                         138: <POP>
                         139: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         142: <LDC <String 'print'>>
                         144: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         147: <DUP>
                         148: <IFNONNULL 14>
                         151: <POP>
                         152: <NEW org/python/exceptions/NameError>
                         155: <DUP>
                         156: <LDC <String 'print'>>
                         158: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         161: <ATHROW>
                         162: <CHECKCAST <Class org/python/types/Object>>
                         165: <CHECKCAST <Class org/python/Callable>>
                         168: <ICONST_2>
                         169: <ANEWARRAY org/python/Object>
                         172: <DUP>
                         173: <ICONST_0>
                         174: <NEW org/python/types/Str>
                         177: <DUP>
                         178: <LDC <String 'Got a NameError'>>
                         180: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         183: <AASTORE>
                         184: <DUP>
                         185: <ICONST_1>
                         186: <ALOAD_0>
                         187: <AASTORE>
                         188: <NEW java/util/Hashtable>
                         191: <DUP>
                         192: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         195: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         200: <POP>
                         201: <ACONST_NULL>
                         202: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-47 [50]
                         org/python/exceptions/NameError: 0-47 [125]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 51: 5
                                 126: 7
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
                 Code (251 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (203 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GOTO 154>
                          50: <ASTORE_0>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC <String 'print'>>
                          56: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          59: <DUP>
                          60: <IFNONNULL 27>
                          63: <POP>
                          64: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          67: <LDC <String 'print'>>
                          69: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          72: <DUP>
                          73: <IFNONNULL 14>
                          76: <POP>
                          77: <NEW org/python/exceptions/NameError>
                          80: <DUP>
                          81: <LDC <String 'print'>>
                          83: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          86: <ATHROW>
                          87: <CHECKCAST <Class org/python/types/Object>>
                          90: <CHECKCAST <Class org/python/Callable>>
                          93: <ICONST_2>
                          94: <ANEWARRAY org/python/Object>
                          97: <DUP>
                          98: <ICONST_0>
                          99: <NEW org/python/types/Str>
                         102: <DUP>
                         103: <LDC <String 'Got an AttributeError'>>
                         105: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         108: <AASTORE>
                         109: <DUP>
                         110: <ICONST_1>
                         111: <ALOAD_0>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <GOTO 75>
                         129: <POP>
                         130: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         133: <LDC <String 'print'>>
                         135: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         138: <DUP>
                         139: <IFNONNULL 27>
                         142: <POP>
                         143: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         146: <LDC <String 'print'>>
                         148: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         151: <DUP>
                         152: <IFNONNULL 14>
                         155: <POP>
                         156: <NEW org/python/exceptions/NameError>
                         159: <DUP>
                         160: <LDC <String 'print'>>
                         162: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         165: <ATHROW>
                         166: <CHECKCAST <Class org/python/types/Object>>
                         169: <CHECKCAST <Class org/python/Callable>>
                         172: <ICONST_1>
                         173: <ANEWARRAY org/python/Object>
                         176: <DUP>
                         177: <ICONST_0>
                         178: <NEW org/python/types/Str>
                         181: <DUP>
                         182: <LDC <String 'Got a NameError'>>
                         184: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         187: <AASTORE>
                         188: <NEW java/util/Hashtable>
                         191: <DUP>
                         192: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         195: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         200: <POP>
                         201: <ACONST_NULL>
                         202: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-47 [50]
                         org/python/exceptions/NameError: 0-47 [129]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 51: 5
                                 130: 7
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
                 Code (338 bytes)
                     Max stack: 9
                     Max locals: 1
                     Bytecode: (278 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GOTO 229>
                          50: <ASTORE_0>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC <String 'print'>>
                          56: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          59: <DUP>
                          60: <IFNONNULL 27>
                          63: <POP>
                          64: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          67: <LDC <String 'print'>>
                          69: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          72: <DUP>
                          73: <IFNONNULL 14>
                          76: <POP>
                          77: <NEW org/python/exceptions/NameError>
                          80: <DUP>
                          81: <LDC <String 'print'>>
                          83: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          86: <ATHROW>
                          87: <CHECKCAST <Class org/python/types/Object>>
                          90: <CHECKCAST <Class org/python/Callable>>
                          93: <ICONST_2>
                          94: <ANEWARRAY org/python/Object>
                          97: <DUP>
                          98: <ICONST_0>
                          99: <NEW org/python/types/Str>
                         102: <DUP>
                         103: <LDC <String 'Got an AttributeError'>>
                         105: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         108: <AASTORE>
                         109: <DUP>
                         110: <ICONST_1>
                         111: <ALOAD_0>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <GOTO 150>
                         129: <POP>
                         130: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         133: <LDC <String 'print'>>
                         135: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         138: <DUP>
                         139: <IFNONNULL 27>
                         142: <POP>
                         143: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         146: <LDC <String 'print'>>
                         148: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         151: <DUP>
                         152: <IFNONNULL 14>
                         155: <POP>
                         156: <NEW org/python/exceptions/NameError>
                         159: <DUP>
                         160: <LDC <String 'print'>>
                         162: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         165: <ATHROW>
                         166: <CHECKCAST <Class org/python/types/Object>>
                         169: <CHECKCAST <Class org/python/Callable>>
                         172: <ICONST_1>
                         173: <ANEWARRAY org/python/Object>
                         176: <DUP>
                         177: <ICONST_0>
                         178: <NEW org/python/types/Str>
                         181: <DUP>
                         182: <LDC <String 'Got a NameError'>>
                         184: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         187: <AASTORE>
                         188: <NEW java/util/Hashtable>
                         191: <DUP>
                         192: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         195: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         200: <POP>
                         201: <GOTO 75>
                         204: <POP>
                         205: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         208: <LDC <String 'print'>>
                         210: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         213: <DUP>
                         214: <IFNONNULL 27>
                         217: <POP>
                         218: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         221: <LDC <String 'print'>>
                         223: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         226: <DUP>
                         227: <IFNONNULL 14>
                         230: <POP>
                         231: <NEW org/python/exceptions/NameError>
                         234: <DUP>
                         235: <LDC <String 'print'>>
                         237: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         240: <ATHROW>
                         241: <CHECKCAST <Class org/python/types/Object>>
                         244: <CHECKCAST <Class org/python/Callable>>
                         247: <ICONST_1>
                         248: <ANEWARRAY org/python/Object>
                         251: <DUP>
                         252: <ICONST_0>
                         253: <NEW org/python/types/Str>
                         256: <DUP>
                         257: <LDC <String 'Got an anonymous error'>>
                         259: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         262: <AASTORE>
                         263: <NEW java/util/Hashtable>
                         266: <DUP>
                         267: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         270: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         275: <POP>
                         276: <ACONST_NULL>
                         277: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-47 [50]
                         org/python/exceptions/NameError: 0-47 [129]
                         org/python/exceptions/BaseException: 0-47 [204]
                     Attributes: (1)
                         LineNumberTable (18 bytes)
                             Line numbers (4 total):
                                 0: 3
                                 51: 5
                                 130: 7
                                 205: 9
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
                 Code (199 bytes)
                     Max stack: 8
                     Max locals: 2
                     Bytecode: (159 bytes)
                           0: <NEW org/python/types/Int>
                           3: <DUP>
                           4: <ICONST_3>
                           5: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                           8: <ASTORE_0>
                           9: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          12: <LDC <String 'print'>>
                          14: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          17: <DUP>
                          18: <IFNONNULL 27>
                          21: <POP>
                          22: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          25: <LDC <String 'print'>>
                          27: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          30: <DUP>
                          31: <IFNONNULL 14>
                          34: <POP>
                          35: <NEW org/python/exceptions/NameError>
                          38: <DUP>
                          39: <LDC <String 'print'>>
                          41: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          44: <ATHROW>
                          45: <CHECKCAST <Class org/python/types/Object>>
                          48: <CHECKCAST <Class org/python/Callable>>
                          51: <ICONST_1>
                          52: <ANEWARRAY org/python/Object>
                          55: <DUP>
                          56: <ICONST_0>
                          57: <NEW org/python/types/Str>
                          60: <DUP>
                          61: <LDC <String 'Do final cleanup'>>
                          63: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                          66: <AASTORE>
                          67: <NEW java/util/Hashtable>
                          70: <DUP>
                          71: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          74: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          79: <POP>
                          80: <GOTO 77>
                          83: <ASTORE_1>
                          84: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          87: <LDC <String 'print'>>
                          89: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          92: <DUP>
                          93: <IFNONNULL 27>
                          96: <POP>
                          97: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         100: <LDC <String 'print'>>
                         102: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         105: <DUP>
                         106: <IFNONNULL 14>
                         109: <POP>
                         110: <NEW org/python/exceptions/NameError>
                         113: <DUP>
                         114: <LDC <String 'print'>>
                         116: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         119: <ATHROW>
                         120: <CHECKCAST <Class org/python/types/Object>>
                         123: <CHECKCAST <Class org/python/Callable>>
                         126: <ICONST_1>
                         127: <ANEWARRAY org/python/Object>
                         130: <DUP>
                         131: <ICONST_0>
                         132: <NEW org/python/types/Str>
                         135: <DUP>
                         136: <LDC <String 'Do final cleanup'>>
                         138: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         141: <AASTORE>
                         142: <NEW java/util/Hashtable>
                         145: <DUP>
                         146: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         149: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         154: <POP>
                         155: <ALOAD_1>
                         156: <ATHROW>
                         157: <ACONST_NULL>
                         158: <ARETURN>
                     Exceptions: (1)
                         finally: 0-9 [83]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 9: 5
                                 84: 5
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
                 Code (407 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (343 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          50: <LDC <String 'print'>>
                          52: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          55: <DUP>
                          56: <IFNONNULL 27>
                          59: <POP>
                          60: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          63: <LDC <String 'print'>>
                          65: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          68: <DUP>
                          69: <IFNONNULL 14>
                          72: <POP>
                          73: <NEW org/python/exceptions/NameError>
                          76: <DUP>
                          77: <LDC <String 'print'>>
                          79: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          82: <ATHROW>
                          83: <CHECKCAST <Class org/python/types/Object>>
                          86: <CHECKCAST <Class org/python/Callable>>
                          89: <ICONST_1>
                          90: <ANEWARRAY org/python/Object>
                          93: <DUP>
                          94: <ICONST_0>
                          95: <NEW org/python/types/Str>
                          98: <DUP>
                          99: <LDC <String 'Do final cleanup'>>
                         101: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         104: <AASTORE>
                         105: <NEW java/util/Hashtable>
                         108: <DUP>
                         109: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         112: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         117: <POP>
                         118: <GOTO 223>
                         121: <POP>
                         122: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         125: <LDC <String 'print'>>
                         127: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         130: <DUP>
                         131: <IFNONNULL 27>
                         134: <POP>
                         135: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         138: <LDC <String 'print'>>
                         140: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         143: <DUP>
                         144: <IFNONNULL 14>
                         147: <POP>
                         148: <NEW org/python/exceptions/NameError>
                         151: <DUP>
                         152: <LDC <String 'print'>>
                         154: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         157: <ATHROW>
                         158: <CHECKCAST <Class org/python/types/Object>>
                         161: <CHECKCAST <Class org/python/Callable>>
                         164: <ICONST_1>
                         165: <ANEWARRAY org/python/Object>
                         168: <DUP>
                         169: <ICONST_0>
                         170: <NEW org/python/types/Str>
                         173: <DUP>
                         174: <LDC <String 'Got an error'>>
                         176: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         179: <AASTORE>
                         180: <NEW java/util/Hashtable>
                         183: <DUP>
                         184: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         187: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         192: <POP>
                         193: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         196: <LDC <String 'print'>>
                         198: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         201: <DUP>
                         202: <IFNONNULL 27>
                         205: <POP>
                         206: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         209: <LDC <String 'print'>>
                         211: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         214: <DUP>
                         215: <IFNONNULL 14>
                         218: <POP>
                         219: <NEW org/python/exceptions/NameError>
                         222: <DUP>
                         223: <LDC <String 'print'>>
                         225: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         228: <ATHROW>
                         229: <CHECKCAST <Class org/python/types/Object>>
                         232: <CHECKCAST <Class org/python/Callable>>
                         235: <ICONST_1>
                         236: <ANEWARRAY org/python/Object>
                         239: <DUP>
                         240: <ICONST_0>
                         241: <NEW org/python/types/Str>
                         244: <DUP>
                         245: <LDC <String 'Do final cleanup'>>
                         247: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         250: <AASTORE>
                         251: <NEW java/util/Hashtable>
                         254: <DUP>
                         255: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         258: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         263: <POP>
                         264: <GOTO 77>
                         267: <ASTORE_0>
                         268: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         271: <LDC <String 'print'>>
                         273: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         276: <DUP>
                         277: <IFNONNULL 27>
                         280: <POP>
                         281: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         284: <LDC <String 'print'>>
                         286: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         289: <DUP>
                         290: <IFNONNULL 14>
                         293: <POP>
                         294: <NEW org/python/exceptions/NameError>
                         297: <DUP>
                         298: <LDC <String 'print'>>
                         300: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         303: <ATHROW>
                         304: <CHECKCAST <Class org/python/types/Object>>
                         307: <CHECKCAST <Class org/python/Callable>>
                         310: <ICONST_1>
                         311: <ANEWARRAY org/python/Object>
                         314: <DUP>
                         315: <ICONST_0>
                         316: <NEW org/python/types/Str>
                         319: <DUP>
                         320: <LDC <String 'Do final cleanup'>>
                         322: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         325: <AASTORE>
                         326: <NEW java/util/Hashtable>
                         329: <DUP>
                         330: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         333: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         338: <POP>
                         339: <ALOAD_0>
                         340: <ATHROW>
                         341: <ACONST_NULL>
                         342: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/BaseException: 0-47 [121]
                         finally: 0-47 [267]
                         finally: 121-193 [267]
                     Attributes: (1)
                         LineNumberTable (22 bytes)
                             Line numbers (5 total):
                                 0: 3
                                 47: 7
                                 122: 5
                                 193: 7
                                 268: 7
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
                 Code (407 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (343 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          50: <LDC <String 'print'>>
                          52: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          55: <DUP>
                          56: <IFNONNULL 27>
                          59: <POP>
                          60: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          63: <LDC <String 'print'>>
                          65: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          68: <DUP>
                          69: <IFNONNULL 14>
                          72: <POP>
                          73: <NEW org/python/exceptions/NameError>
                          76: <DUP>
                          77: <LDC <String 'print'>>
                          79: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          82: <ATHROW>
                          83: <CHECKCAST <Class org/python/types/Object>>
                          86: <CHECKCAST <Class org/python/Callable>>
                          89: <ICONST_1>
                          90: <ANEWARRAY org/python/Object>
                          93: <DUP>
                          94: <ICONST_0>
                          95: <NEW org/python/types/Str>
                          98: <DUP>
                          99: <LDC <String 'Do final cleanup'>>
                         101: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         104: <AASTORE>
                         105: <NEW java/util/Hashtable>
                         108: <DUP>
                         109: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         112: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         117: <POP>
                         118: <GOTO 223>
                         121: <POP>
                         122: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         125: <LDC <String 'print'>>
                         127: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         130: <DUP>
                         131: <IFNONNULL 27>
                         134: <POP>
                         135: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         138: <LDC <String 'print'>>
                         140: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         143: <DUP>
                         144: <IFNONNULL 14>
                         147: <POP>
                         148: <NEW org/python/exceptions/NameError>
                         151: <DUP>
                         152: <LDC <String 'print'>>
                         154: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         157: <ATHROW>
                         158: <CHECKCAST <Class org/python/types/Object>>
                         161: <CHECKCAST <Class org/python/Callable>>
                         164: <ICONST_1>
                         165: <ANEWARRAY org/python/Object>
                         168: <DUP>
                         169: <ICONST_0>
                         170: <NEW org/python/types/Str>
                         173: <DUP>
                         174: <LDC <String 'Got an error'>>
                         176: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         179: <AASTORE>
                         180: <NEW java/util/Hashtable>
                         183: <DUP>
                         184: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         187: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         192: <POP>
                         193: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         196: <LDC <String 'print'>>
                         198: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         201: <DUP>
                         202: <IFNONNULL 27>
                         205: <POP>
                         206: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         209: <LDC <String 'print'>>
                         211: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         214: <DUP>
                         215: <IFNONNULL 14>
                         218: <POP>
                         219: <NEW org/python/exceptions/NameError>
                         222: <DUP>
                         223: <LDC <String 'print'>>
                         225: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         228: <ATHROW>
                         229: <CHECKCAST <Class org/python/types/Object>>
                         232: <CHECKCAST <Class org/python/Callable>>
                         235: <ICONST_1>
                         236: <ANEWARRAY org/python/Object>
                         239: <DUP>
                         240: <ICONST_0>
                         241: <NEW org/python/types/Str>
                         244: <DUP>
                         245: <LDC <String 'Do final cleanup'>>
                         247: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         250: <AASTORE>
                         251: <NEW java/util/Hashtable>
                         254: <DUP>
                         255: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         258: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         263: <POP>
                         264: <GOTO 77>
                         267: <ASTORE_0>
                         268: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         271: <LDC <String 'print'>>
                         273: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         276: <DUP>
                         277: <IFNONNULL 27>
                         280: <POP>
                         281: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         284: <LDC <String 'print'>>
                         286: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         289: <DUP>
                         290: <IFNONNULL 14>
                         293: <POP>
                         294: <NEW org/python/exceptions/NameError>
                         297: <DUP>
                         298: <LDC <String 'print'>>
                         300: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         303: <ATHROW>
                         304: <CHECKCAST <Class org/python/types/Object>>
                         307: <CHECKCAST <Class org/python/Callable>>
                         310: <ICONST_1>
                         311: <ANEWARRAY org/python/Object>
                         314: <DUP>
                         315: <ICONST_0>
                         316: <NEW org/python/types/Str>
                         319: <DUP>
                         320: <LDC <String 'Do final cleanup'>>
                         322: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         325: <AASTORE>
                         326: <NEW java/util/Hashtable>
                         329: <DUP>
                         330: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         333: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         338: <POP>
                         339: <ALOAD_0>
                         340: <ATHROW>
                         341: <ACONST_NULL>
                         342: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-47 [121]
                         finally: 0-47 [267]
                         finally: 121-193 [267]
                     Attributes: (1)
                         LineNumberTable (22 bytes)
                             Line numbers (5 total):
                                 0: 3
                                 47: 7
                                 122: 5
                                 193: 7
                                 268: 7
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
                 Code (411 bytes)
                     Max stack: 10
                     Max locals: 2
                     Bytecode: (347 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          50: <LDC <String 'print'>>
                          52: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          55: <DUP>
                          56: <IFNONNULL 27>
                          59: <POP>
                          60: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          63: <LDC <String 'print'>>
                          65: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          68: <DUP>
                          69: <IFNONNULL 14>
                          72: <POP>
                          73: <NEW org/python/exceptions/NameError>
                          76: <DUP>
                          77: <LDC <String 'print'>>
                          79: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          82: <ATHROW>
                          83: <CHECKCAST <Class org/python/types/Object>>
                          86: <CHECKCAST <Class org/python/Callable>>
                          89: <ICONST_1>
                          90: <ANEWARRAY org/python/Object>
                          93: <DUP>
                          94: <ICONST_0>
                          95: <NEW org/python/types/Str>
                          98: <DUP>
                          99: <LDC <String 'Do final cleanup'>>
                         101: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         104: <AASTORE>
                         105: <NEW java/util/Hashtable>
                         108: <DUP>
                         109: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         112: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         117: <POP>
                         118: <GOTO 227>
                         121: <ASTORE_0>
                         122: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         125: <LDC <String 'print'>>
                         127: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         130: <DUP>
                         131: <IFNONNULL 27>
                         134: <POP>
                         135: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         138: <LDC <String 'print'>>
                         140: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         143: <DUP>
                         144: <IFNONNULL 14>
                         147: <POP>
                         148: <NEW org/python/exceptions/NameError>
                         151: <DUP>
                         152: <LDC <String 'print'>>
                         154: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         157: <ATHROW>
                         158: <CHECKCAST <Class org/python/types/Object>>
                         161: <CHECKCAST <Class org/python/Callable>>
                         164: <ICONST_2>
                         165: <ANEWARRAY org/python/Object>
                         168: <DUP>
                         169: <ICONST_0>
                         170: <NEW org/python/types/Str>
                         173: <DUP>
                         174: <LDC <String 'Got an AttributeError'>>
                         176: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         179: <AASTORE>
                         180: <DUP>
                         181: <ICONST_1>
                         182: <ALOAD_0>
                         183: <AASTORE>
                         184: <NEW java/util/Hashtable>
                         187: <DUP>
                         188: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         191: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         196: <POP>
                         197: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         200: <LDC <String 'print'>>
                         202: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         205: <DUP>
                         206: <IFNONNULL 27>
                         209: <POP>
                         210: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         213: <LDC <String 'print'>>
                         215: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         218: <DUP>
                         219: <IFNONNULL 14>
                         222: <POP>
                         223: <NEW org/python/exceptions/NameError>
                         226: <DUP>
                         227: <LDC <String 'print'>>
                         229: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         232: <ATHROW>
                         233: <CHECKCAST <Class org/python/types/Object>>
                         236: <CHECKCAST <Class org/python/Callable>>
                         239: <ICONST_1>
                         240: <ANEWARRAY org/python/Object>
                         243: <DUP>
                         244: <ICONST_0>
                         245: <NEW org/python/types/Str>
                         248: <DUP>
                         249: <LDC <String 'Do final cleanup'>>
                         251: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         254: <AASTORE>
                         255: <NEW java/util/Hashtable>
                         258: <DUP>
                         259: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         262: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         267: <POP>
                         268: <GOTO 77>
                         271: <ASTORE_1>
                         272: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         275: <LDC <String 'print'>>
                         277: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         280: <DUP>
                         281: <IFNONNULL 27>
                         284: <POP>
                         285: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         288: <LDC <String 'print'>>
                         290: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         293: <DUP>
                         294: <IFNONNULL 14>
                         297: <POP>
                         298: <NEW org/python/exceptions/NameError>
                         301: <DUP>
                         302: <LDC <String 'print'>>
                         304: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         307: <ATHROW>
                         308: <CHECKCAST <Class org/python/types/Object>>
                         311: <CHECKCAST <Class org/python/Callable>>
                         314: <ICONST_1>
                         315: <ANEWARRAY org/python/Object>
                         318: <DUP>
                         319: <ICONST_0>
                         320: <NEW org/python/types/Str>
                         323: <DUP>
                         324: <LDC <String 'Do final cleanup'>>
                         326: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         329: <AASTORE>
                         330: <NEW java/util/Hashtable>
                         333: <DUP>
                         334: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         337: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         342: <POP>
                         343: <ALOAD_1>
                         344: <ATHROW>
                         345: <ACONST_NULL>
                         346: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-47 [121]
                         finally: 0-47 [271]
                         finally: 121-197 [271]
                     Attributes: (1)
                         LineNumberTable (22 bytes)
                             Line numbers (5 total):
                                 0: 3
                                 47: 7
                                 122: 5
                                 197: 7
                                 272: 7
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
                 Code (581 bytes)
                     Max stack: 12
                     Max locals: 2
                     Bytecode: (493 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          50: <LDC <String 'print'>>
                          52: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          55: <DUP>
                          56: <IFNONNULL 27>
                          59: <POP>
                          60: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          63: <LDC <String 'print'>>
                          65: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          68: <DUP>
                          69: <IFNONNULL 14>
                          72: <POP>
                          73: <NEW org/python/exceptions/NameError>
                          76: <DUP>
                          77: <LDC <String 'print'>>
                          79: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          82: <ATHROW>
                          83: <CHECKCAST <Class org/python/types/Object>>
                          86: <CHECKCAST <Class org/python/Callable>>
                          89: <ICONST_1>
                          90: <ANEWARRAY org/python/Object>
                          93: <DUP>
                          94: <ICONST_0>
                          95: <NEW org/python/types/Str>
                          98: <DUP>
                          99: <LDC <String 'Do final cleanup'>>
                         101: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         104: <AASTORE>
                         105: <NEW java/util/Hashtable>
                         108: <DUP>
                         109: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         112: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         117: <POP>
                         118: <GOTO 373>
                         121: <POP>
                         122: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         125: <LDC <String 'print'>>
                         127: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         130: <DUP>
                         131: <IFNONNULL 27>
                         134: <POP>
                         135: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         138: <LDC <String 'print'>>
                         140: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         143: <DUP>
                         144: <IFNONNULL 14>
                         147: <POP>
                         148: <NEW org/python/exceptions/NameError>
                         151: <DUP>
                         152: <LDC <String 'print'>>
                         154: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         157: <ATHROW>
                         158: <CHECKCAST <Class org/python/types/Object>>
                         161: <CHECKCAST <Class org/python/Callable>>
                         164: <ICONST_1>
                         165: <ANEWARRAY org/python/Object>
                         168: <DUP>
                         169: <ICONST_0>
                         170: <NEW org/python/types/Str>
                         173: <DUP>
                         174: <LDC <String 'Got an AttributeError'>>
                         176: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         179: <AASTORE>
                         180: <NEW java/util/Hashtable>
                         183: <DUP>
                         184: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         187: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         192: <POP>
                         193: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         196: <LDC <String 'print'>>
                         198: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         201: <DUP>
                         202: <IFNONNULL 27>
                         205: <POP>
                         206: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         209: <LDC <String 'print'>>
                         211: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         214: <DUP>
                         215: <IFNONNULL 14>
                         218: <POP>
                         219: <NEW org/python/exceptions/NameError>
                         222: <DUP>
                         223: <LDC <String 'print'>>
                         225: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         228: <ATHROW>
                         229: <CHECKCAST <Class org/python/types/Object>>
                         232: <CHECKCAST <Class org/python/Callable>>
                         235: <ICONST_1>
                         236: <ANEWARRAY org/python/Object>
                         239: <DUP>
                         240: <ICONST_0>
                         241: <NEW org/python/types/Str>
                         244: <DUP>
                         245: <LDC <String 'Do final cleanup'>>
                         247: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         250: <AASTORE>
                         251: <NEW java/util/Hashtable>
                         254: <DUP>
                         255: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         258: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         263: <POP>
                         264: <GOTO 227>
                         267: <ASTORE_0>
                         268: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         271: <LDC <String 'print'>>
                         273: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         276: <DUP>
                         277: <IFNONNULL 27>
                         280: <POP>
                         281: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         284: <LDC <String 'print'>>
                         286: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         289: <DUP>
                         290: <IFNONNULL 14>
                         293: <POP>
                         294: <NEW org/python/exceptions/NameError>
                         297: <DUP>
                         298: <LDC <String 'print'>>
                         300: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         303: <ATHROW>
                         304: <CHECKCAST <Class org/python/types/Object>>
                         307: <CHECKCAST <Class org/python/Callable>>
                         310: <ICONST_2>
                         311: <ANEWARRAY org/python/Object>
                         314: <DUP>
                         315: <ICONST_0>
                         316: <NEW org/python/types/Str>
                         319: <DUP>
                         320: <LDC <String 'Got a NameError'>>
                         322: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         325: <AASTORE>
                         326: <DUP>
                         327: <ICONST_1>
                         328: <ALOAD_0>
                         329: <AASTORE>
                         330: <NEW java/util/Hashtable>
                         333: <DUP>
                         334: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         337: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         342: <POP>
                         343: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         346: <LDC <String 'print'>>
                         348: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         351: <DUP>
                         352: <IFNONNULL 27>
                         355: <POP>
                         356: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         359: <LDC <String 'print'>>
                         361: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         364: <DUP>
                         365: <IFNONNULL 14>
                         368: <POP>
                         369: <NEW org/python/exceptions/NameError>
                         372: <DUP>
                         373: <LDC <String 'print'>>
                         375: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         378: <ATHROW>
                         379: <CHECKCAST <Class org/python/types/Object>>
                         382: <CHECKCAST <Class org/python/Callable>>
                         385: <ICONST_1>
                         386: <ANEWARRAY org/python/Object>
                         389: <DUP>
                         390: <ICONST_0>
                         391: <NEW org/python/types/Str>
                         394: <DUP>
                         395: <LDC <String 'Do final cleanup'>>
                         397: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         400: <AASTORE>
                         401: <NEW java/util/Hashtable>
                         404: <DUP>
                         405: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         408: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         413: <POP>
                         414: <GOTO 77>
                         417: <ASTORE_1>
                         418: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         421: <LDC <String 'print'>>
                         423: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         426: <DUP>
                         427: <IFNONNULL 27>
                         430: <POP>
                         431: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         434: <LDC <String 'print'>>
                         436: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         439: <DUP>
                         440: <IFNONNULL 14>
                         443: <POP>
                         444: <NEW org/python/exceptions/NameError>
                         447: <DUP>
                         448: <LDC <String 'print'>>
                         450: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         453: <ATHROW>
                         454: <CHECKCAST <Class org/python/types/Object>>
                         457: <CHECKCAST <Class org/python/Callable>>
                         460: <ICONST_1>
                         461: <ANEWARRAY org/python/Object>
                         464: <DUP>
                         465: <ICONST_0>
                         466: <NEW org/python/types/Str>
                         469: <DUP>
                         470: <LDC <String 'Do final cleanup'>>
                         472: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         475: <AASTORE>
                         476: <NEW java/util/Hashtable>
                         479: <DUP>
                         480: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         483: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         488: <POP>
                         489: <ALOAD_1>
                         490: <ATHROW>
                         491: <ACONST_NULL>
                         492: <ARETURN>
                     Exceptions: (5)
                         org/python/exceptions/AttributeError: 0-47 [121]
                         org/python/exceptions/NameError: 0-47 [267]
                         finally: 0-47 [417]
                         finally: 121-193 [417]
                         finally: 267-343 [417]
                     Attributes: (1)
                         LineNumberTable (30 bytes)
                             Line numbers (7 total):
                                 0: 3
                                 47: 9
                                 122: 5
                                 193: 9
                                 268: 7
                                 343: 9
                                 418: 9
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
                 Code (235 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (195 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          50: <LDC <String 'print'>>
                          52: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          55: <DUP>
                          56: <IFNONNULL 27>
                          59: <POP>
                          60: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          63: <LDC <String 'print'>>
                          65: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          68: <DUP>
                          69: <IFNONNULL 14>
                          72: <POP>
                          73: <NEW org/python/exceptions/NameError>
                          76: <DUP>
                          77: <LDC <String 'print'>>
                          79: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          82: <ATHROW>
                          83: <CHECKCAST <Class org/python/types/Object>>
                          86: <CHECKCAST <Class org/python/Callable>>
                          89: <ICONST_1>
                          90: <ANEWARRAY org/python/Object>
                          93: <DUP>
                          94: <ICONST_0>
                          95: <NEW org/python/types/Str>
                          98: <DUP>
                          99: <LDC <String 'Do else handling'>>
                         101: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         104: <AASTORE>
                         105: <NEW java/util/Hashtable>
                         108: <DUP>
                         109: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         112: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         117: <POP>
                         118: <GOTO 75>
                         121: <POP>
                         122: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         125: <LDC <String 'print'>>
                         127: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         130: <DUP>
                         131: <IFNONNULL 27>
                         134: <POP>
                         135: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         138: <LDC <String 'print'>>
                         140: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         143: <DUP>
                         144: <IFNONNULL 14>
                         147: <POP>
                         148: <NEW org/python/exceptions/NameError>
                         151: <DUP>
                         152: <LDC <String 'print'>>
                         154: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         157: <ATHROW>
                         158: <CHECKCAST <Class org/python/types/Object>>
                         161: <CHECKCAST <Class org/python/Callable>>
                         164: <ICONST_1>
                         165: <ANEWARRAY org/python/Object>
                         168: <DUP>
                         169: <ICONST_0>
                         170: <NEW org/python/types/Str>
                         173: <DUP>
                         174: <LDC <String 'Got an error'>>
                         176: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         179: <AASTORE>
                         180: <NEW java/util/Hashtable>
                         183: <DUP>
                         184: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         187: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         192: <POP>
                         193: <ACONST_NULL>
                         194: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/BaseException: 0-47 [121]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 47: 7
                                 122: 5
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
                 Code (235 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (195 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          50: <LDC <String 'print'>>
                          52: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          55: <DUP>
                          56: <IFNONNULL 27>
                          59: <POP>
                          60: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          63: <LDC <String 'print'>>
                          65: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          68: <DUP>
                          69: <IFNONNULL 14>
                          72: <POP>
                          73: <NEW org/python/exceptions/NameError>
                          76: <DUP>
                          77: <LDC <String 'print'>>
                          79: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          82: <ATHROW>
                          83: <CHECKCAST <Class org/python/types/Object>>
                          86: <CHECKCAST <Class org/python/Callable>>
                          89: <ICONST_1>
                          90: <ANEWARRAY org/python/Object>
                          93: <DUP>
                          94: <ICONST_0>
                          95: <NEW org/python/types/Str>
                          98: <DUP>
                          99: <LDC <String 'Do else handling'>>
                         101: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         104: <AASTORE>
                         105: <NEW java/util/Hashtable>
                         108: <DUP>
                         109: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         112: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         117: <POP>
                         118: <GOTO 75>
                         121: <POP>
                         122: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         125: <LDC <String 'print'>>
                         127: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         130: <DUP>
                         131: <IFNONNULL 27>
                         134: <POP>
                         135: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         138: <LDC <String 'print'>>
                         140: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         143: <DUP>
                         144: <IFNONNULL 14>
                         147: <POP>
                         148: <NEW org/python/exceptions/NameError>
                         151: <DUP>
                         152: <LDC <String 'print'>>
                         154: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         157: <ATHROW>
                         158: <CHECKCAST <Class org/python/types/Object>>
                         161: <CHECKCAST <Class org/python/Callable>>
                         164: <ICONST_1>
                         165: <ANEWARRAY org/python/Object>
                         168: <DUP>
                         169: <ICONST_0>
                         170: <NEW org/python/types/Str>
                         173: <DUP>
                         174: <LDC <String 'Got an error'>>
                         176: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         179: <AASTORE>
                         180: <NEW java/util/Hashtable>
                         183: <DUP>
                         184: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         187: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         192: <POP>
                         193: <ACONST_NULL>
                         194: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/AttributeError: 0-47 [121]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 47: 7
                                 122: 5
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
                 Code (326 bytes)
                     Max stack: 9
                     Max locals: 1
                     Bytecode: (274 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          50: <LDC <String 'print'>>
                          52: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          55: <DUP>
                          56: <IFNONNULL 27>
                          59: <POP>
                          60: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          63: <LDC <String 'print'>>
                          65: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          68: <DUP>
                          69: <IFNONNULL 14>
                          72: <POP>
                          73: <NEW org/python/exceptions/NameError>
                          76: <DUP>
                          77: <LDC <String 'print'>>
                          79: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          82: <ATHROW>
                          83: <CHECKCAST <Class org/python/types/Object>>
                          86: <CHECKCAST <Class org/python/Callable>>
                          89: <ICONST_1>
                          90: <ANEWARRAY org/python/Object>
                          93: <DUP>
                          94: <ICONST_0>
                          95: <NEW org/python/types/Str>
                          98: <DUP>
                          99: <LDC <String 'Do else handling'>>
                         101: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         104: <AASTORE>
                         105: <NEW java/util/Hashtable>
                         108: <DUP>
                         109: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         112: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         117: <POP>
                         118: <GOTO 154>
                         121: <POP>
                         122: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         125: <LDC <String 'print'>>
                         127: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         130: <DUP>
                         131: <IFNONNULL 27>
                         134: <POP>
                         135: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         138: <LDC <String 'print'>>
                         140: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         143: <DUP>
                         144: <IFNONNULL 14>
                         147: <POP>
                         148: <NEW org/python/exceptions/NameError>
                         151: <DUP>
                         152: <LDC <String 'print'>>
                         154: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         157: <ATHROW>
                         158: <CHECKCAST <Class org/python/types/Object>>
                         161: <CHECKCAST <Class org/python/Callable>>
                         164: <ICONST_1>
                         165: <ANEWARRAY org/python/Object>
                         168: <DUP>
                         169: <ICONST_0>
                         170: <NEW org/python/types/Str>
                         173: <DUP>
                         174: <LDC <String 'Got an AttributeError'>>
                         176: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         179: <AASTORE>
                         180: <NEW java/util/Hashtable>
                         183: <DUP>
                         184: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         187: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         192: <POP>
                         193: <GOTO 79>
                         196: <ASTORE_0>
                         197: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         200: <LDC <String 'print'>>
                         202: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         205: <DUP>
                         206: <IFNONNULL 27>
                         209: <POP>
                         210: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         213: <LDC <String 'print'>>
                         215: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         218: <DUP>
                         219: <IFNONNULL 14>
                         222: <POP>
                         223: <NEW org/python/exceptions/NameError>
                         226: <DUP>
                         227: <LDC <String 'print'>>
                         229: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         232: <ATHROW>
                         233: <CHECKCAST <Class org/python/types/Object>>
                         236: <CHECKCAST <Class org/python/Callable>>
                         239: <ICONST_2>
                         240: <ANEWARRAY org/python/Object>
                         243: <DUP>
                         244: <ICONST_0>
                         245: <NEW org/python/types/Str>
                         248: <DUP>
                         249: <LDC <String 'Got a NameError'>>
                         251: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         254: <AASTORE>
                         255: <DUP>
                         256: <ICONST_1>
                         257: <ALOAD_0>
                         258: <AASTORE>
                         259: <NEW java/util/Hashtable>
                         262: <DUP>
                         263: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         266: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         271: <POP>
                         272: <ACONST_NULL>
                         273: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-47 [121]
                         org/python/exceptions/NameError: 0-47 [196]
                     Attributes: (1)
                         LineNumberTable (18 bytes)
                             Line numbers (4 total):
                                 0: 3
                                 47: 9
                                 122: 5
                                 197: 7
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
                 Code (482 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (414 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          50: <LDC <String 'print'>>
                          52: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          55: <DUP>
                          56: <IFNONNULL 27>
                          59: <POP>
                          60: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          63: <LDC <String 'print'>>
                          65: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          68: <DUP>
                          69: <IFNONNULL 14>
                          72: <POP>
                          73: <NEW org/python/exceptions/NameError>
                          76: <DUP>
                          77: <LDC <String 'print'>>
                          79: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          82: <ATHROW>
                          83: <CHECKCAST <Class org/python/types/Object>>
                          86: <CHECKCAST <Class org/python/Callable>>
                          89: <ICONST_1>
                          90: <ANEWARRAY org/python/Object>
                          93: <DUP>
                          94: <ICONST_0>
                          95: <NEW org/python/types/Str>
                          98: <DUP>
                          99: <LDC <String 'Do else handling'>>
                         101: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         104: <AASTORE>
                         105: <NEW java/util/Hashtable>
                         108: <DUP>
                         109: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         112: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         117: <POP>
                         118: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         121: <LDC <String 'print'>>
                         123: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         126: <DUP>
                         127: <IFNONNULL 27>
                         130: <POP>
                         131: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         134: <LDC <String 'print'>>
                         136: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         139: <DUP>
                         140: <IFNONNULL 14>
                         143: <POP>
                         144: <NEW org/python/exceptions/NameError>
                         147: <DUP>
                         148: <LDC <String 'print'>>
                         150: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         153: <ATHROW>
                         154: <CHECKCAST <Class org/python/types/Object>>
                         157: <CHECKCAST <Class org/python/Callable>>
                         160: <ICONST_1>
                         161: <ANEWARRAY org/python/Object>
                         164: <DUP>
                         165: <ICONST_0>
                         166: <NEW org/python/types/Str>
                         169: <DUP>
                         170: <LDC <String 'Do final cleanup'>>
                         172: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         175: <AASTORE>
                         176: <NEW java/util/Hashtable>
                         179: <DUP>
                         180: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         183: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         188: <POP>
                         189: <GOTO 223>
                         192: <POP>
                         193: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         196: <LDC <String 'print'>>
                         198: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         201: <DUP>
                         202: <IFNONNULL 27>
                         205: <POP>
                         206: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         209: <LDC <String 'print'>>
                         211: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         214: <DUP>
                         215: <IFNONNULL 14>
                         218: <POP>
                         219: <NEW org/python/exceptions/NameError>
                         222: <DUP>
                         223: <LDC <String 'print'>>
                         225: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         228: <ATHROW>
                         229: <CHECKCAST <Class org/python/types/Object>>
                         232: <CHECKCAST <Class org/python/Callable>>
                         235: <ICONST_1>
                         236: <ANEWARRAY org/python/Object>
                         239: <DUP>
                         240: <ICONST_0>
                         241: <NEW org/python/types/Str>
                         244: <DUP>
                         245: <LDC <String 'Got an error'>>
                         247: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         250: <AASTORE>
                         251: <NEW java/util/Hashtable>
                         254: <DUP>
                         255: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         258: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         263: <POP>
                         264: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         267: <LDC <String 'print'>>
                         269: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         272: <DUP>
                         273: <IFNONNULL 27>
                         276: <POP>
                         277: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         280: <LDC <String 'print'>>
                         282: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         285: <DUP>
                         286: <IFNONNULL 14>
                         289: <POP>
                         290: <NEW org/python/exceptions/NameError>
                         293: <DUP>
                         294: <LDC <String 'print'>>
                         296: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         299: <ATHROW>
                         300: <CHECKCAST <Class org/python/types/Object>>
                         303: <CHECKCAST <Class org/python/Callable>>
                         306: <ICONST_1>
                         307: <ANEWARRAY org/python/Object>
                         310: <DUP>
                         311: <ICONST_0>
                         312: <NEW org/python/types/Str>
                         315: <DUP>
                         316: <LDC <String 'Do final cleanup'>>
                         318: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         321: <AASTORE>
                         322: <NEW java/util/Hashtable>
                         325: <DUP>
                         326: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         329: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         334: <POP>
                         335: <GOTO 77>
                         338: <ASTORE_0>
                         339: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         342: <LDC <String 'print'>>
                         344: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         347: <DUP>
                         348: <IFNONNULL 27>
                         351: <POP>
                         352: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         355: <LDC <String 'print'>>
                         357: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         360: <DUP>
                         361: <IFNONNULL 14>
                         364: <POP>
                         365: <NEW org/python/exceptions/NameError>
                         368: <DUP>
                         369: <LDC <String 'print'>>
                         371: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         374: <ATHROW>
                         375: <CHECKCAST <Class org/python/types/Object>>
                         378: <CHECKCAST <Class org/python/Callable>>
                         381: <ICONST_1>
                         382: <ANEWARRAY org/python/Object>
                         385: <DUP>
                         386: <ICONST_0>
                         387: <NEW org/python/types/Str>
                         390: <DUP>
                         391: <LDC <String 'Do final cleanup'>>
                         393: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         396: <AASTORE>
                         397: <NEW java/util/Hashtable>
                         400: <DUP>
                         401: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         404: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         409: <POP>
                         410: <ALOAD_0>
                         411: <ATHROW>
                         412: <ACONST_NULL>
                         413: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/BaseException: 0-47 [192]
                         finally: 0-47 [338]
                         finally: 192-264 [338]
                     Attributes: (1)
                         LineNumberTable (26 bytes)
                             Line numbers (6 total):
                                 0: 3
                                 47: 7
                                 118: 9
                                 193: 5
                                 264: 9
                                 339: 9
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
                 Code (482 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (414 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          50: <LDC <String 'print'>>
                          52: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          55: <DUP>
                          56: <IFNONNULL 27>
                          59: <POP>
                          60: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          63: <LDC <String 'print'>>
                          65: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          68: <DUP>
                          69: <IFNONNULL 14>
                          72: <POP>
                          73: <NEW org/python/exceptions/NameError>
                          76: <DUP>
                          77: <LDC <String 'print'>>
                          79: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          82: <ATHROW>
                          83: <CHECKCAST <Class org/python/types/Object>>
                          86: <CHECKCAST <Class org/python/Callable>>
                          89: <ICONST_1>
                          90: <ANEWARRAY org/python/Object>
                          93: <DUP>
                          94: <ICONST_0>
                          95: <NEW org/python/types/Str>
                          98: <DUP>
                          99: <LDC <String 'Do else handling'>>
                         101: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         104: <AASTORE>
                         105: <NEW java/util/Hashtable>
                         108: <DUP>
                         109: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         112: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         117: <POP>
                         118: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         121: <LDC <String 'print'>>
                         123: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         126: <DUP>
                         127: <IFNONNULL 27>
                         130: <POP>
                         131: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         134: <LDC <String 'print'>>
                         136: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         139: <DUP>
                         140: <IFNONNULL 14>
                         143: <POP>
                         144: <NEW org/python/exceptions/NameError>
                         147: <DUP>
                         148: <LDC <String 'print'>>
                         150: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         153: <ATHROW>
                         154: <CHECKCAST <Class org/python/types/Object>>
                         157: <CHECKCAST <Class org/python/Callable>>
                         160: <ICONST_1>
                         161: <ANEWARRAY org/python/Object>
                         164: <DUP>
                         165: <ICONST_0>
                         166: <NEW org/python/types/Str>
                         169: <DUP>
                         170: <LDC <String 'Do final cleanup'>>
                         172: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         175: <AASTORE>
                         176: <NEW java/util/Hashtable>
                         179: <DUP>
                         180: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         183: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         188: <POP>
                         189: <GOTO 223>
                         192: <POP>
                         193: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         196: <LDC <String 'print'>>
                         198: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         201: <DUP>
                         202: <IFNONNULL 27>
                         205: <POP>
                         206: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         209: <LDC <String 'print'>>
                         211: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         214: <DUP>
                         215: <IFNONNULL 14>
                         218: <POP>
                         219: <NEW org/python/exceptions/NameError>
                         222: <DUP>
                         223: <LDC <String 'print'>>
                         225: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         228: <ATHROW>
                         229: <CHECKCAST <Class org/python/types/Object>>
                         232: <CHECKCAST <Class org/python/Callable>>
                         235: <ICONST_1>
                         236: <ANEWARRAY org/python/Object>
                         239: <DUP>
                         240: <ICONST_0>
                         241: <NEW org/python/types/Str>
                         244: <DUP>
                         245: <LDC <String 'Got an error'>>
                         247: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         250: <AASTORE>
                         251: <NEW java/util/Hashtable>
                         254: <DUP>
                         255: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         258: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         263: <POP>
                         264: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         267: <LDC <String 'print'>>
                         269: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         272: <DUP>
                         273: <IFNONNULL 27>
                         276: <POP>
                         277: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         280: <LDC <String 'print'>>
                         282: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         285: <DUP>
                         286: <IFNONNULL 14>
                         289: <POP>
                         290: <NEW org/python/exceptions/NameError>
                         293: <DUP>
                         294: <LDC <String 'print'>>
                         296: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         299: <ATHROW>
                         300: <CHECKCAST <Class org/python/types/Object>>
                         303: <CHECKCAST <Class org/python/Callable>>
                         306: <ICONST_1>
                         307: <ANEWARRAY org/python/Object>
                         310: <DUP>
                         311: <ICONST_0>
                         312: <NEW org/python/types/Str>
                         315: <DUP>
                         316: <LDC <String 'Do final cleanup'>>
                         318: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         321: <AASTORE>
                         322: <NEW java/util/Hashtable>
                         325: <DUP>
                         326: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         329: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         334: <POP>
                         335: <GOTO 77>
                         338: <ASTORE_0>
                         339: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         342: <LDC <String 'print'>>
                         344: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         347: <DUP>
                         348: <IFNONNULL 27>
                         351: <POP>
                         352: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         355: <LDC <String 'print'>>
                         357: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         360: <DUP>
                         361: <IFNONNULL 14>
                         364: <POP>
                         365: <NEW org/python/exceptions/NameError>
                         368: <DUP>
                         369: <LDC <String 'print'>>
                         371: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         374: <ATHROW>
                         375: <CHECKCAST <Class org/python/types/Object>>
                         378: <CHECKCAST <Class org/python/Callable>>
                         381: <ICONST_1>
                         382: <ANEWARRAY org/python/Object>
                         385: <DUP>
                         386: <ICONST_0>
                         387: <NEW org/python/types/Str>
                         390: <DUP>
                         391: <LDC <String 'Do final cleanup'>>
                         393: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         396: <AASTORE>
                         397: <NEW java/util/Hashtable>
                         400: <DUP>
                         401: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         404: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         409: <POP>
                         410: <ALOAD_0>
                         411: <ATHROW>
                         412: <ACONST_NULL>
                         413: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-47 [192]
                         finally: 0-47 [338]
                         finally: 192-264 [338]
                     Attributes: (1)
                         LineNumberTable (26 bytes)
                             Line numbers (6 total):
                                 0: 3
                                 47: 7
                                 118: 9
                                 193: 5
                                 264: 9
                                 339: 9
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
                 Code (656 bytes)
                     Max stack: 12
                     Max locals: 2
                     Bytecode: (564 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC <String 'obj'>>
                           5: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           8: <DUP>
                           9: <IFNONNULL 27>
                          12: <POP>
                          13: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          16: <LDC <String 'obj'>>
                          18: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          21: <DUP>
                          22: <IFNONNULL 14>
                          25: <POP>
                          26: <NEW org/python/exceptions/NameError>
                          29: <DUP>
                          30: <LDC <String 'obj'>>
                          32: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          35: <ATHROW>
                          36: <CHECKCAST <Class org/python/types/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          46: <POP>
                          47: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          50: <LDC <String 'print'>>
                          52: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          55: <DUP>
                          56: <IFNONNULL 27>
                          59: <POP>
                          60: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          63: <LDC <String 'print'>>
                          65: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          68: <DUP>
                          69: <IFNONNULL 14>
                          72: <POP>
                          73: <NEW org/python/exceptions/NameError>
                          76: <DUP>
                          77: <LDC <String 'print'>>
                          79: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          82: <ATHROW>
                          83: <CHECKCAST <Class org/python/types/Object>>
                          86: <CHECKCAST <Class org/python/Callable>>
                          89: <ICONST_1>
                          90: <ANEWARRAY org/python/Object>
                          93: <DUP>
                          94: <ICONST_0>
                          95: <NEW org/python/types/Str>
                          98: <DUP>
                          99: <LDC <String 'Do else handling'>>
                         101: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         104: <AASTORE>
                         105: <NEW java/util/Hashtable>
                         108: <DUP>
                         109: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         112: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         117: <POP>
                         118: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         121: <LDC <String 'print'>>
                         123: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         126: <DUP>
                         127: <IFNONNULL 27>
                         130: <POP>
                         131: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         134: <LDC <String 'print'>>
                         136: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         139: <DUP>
                         140: <IFNONNULL 14>
                         143: <POP>
                         144: <NEW org/python/exceptions/NameError>
                         147: <DUP>
                         148: <LDC <String 'print'>>
                         150: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         153: <ATHROW>
                         154: <CHECKCAST <Class org/python/types/Object>>
                         157: <CHECKCAST <Class org/python/Callable>>
                         160: <ICONST_1>
                         161: <ANEWARRAY org/python/Object>
                         164: <DUP>
                         165: <ICONST_0>
                         166: <NEW org/python/types/Str>
                         169: <DUP>
                         170: <LDC <String 'Do final cleanup'>>
                         172: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         175: <AASTORE>
                         176: <NEW java/util/Hashtable>
                         179: <DUP>
                         180: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         183: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         188: <POP>
                         189: <GOTO 373>
                         192: <POP>
                         193: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         196: <LDC <String 'print'>>
                         198: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         201: <DUP>
                         202: <IFNONNULL 27>
                         205: <POP>
                         206: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         209: <LDC <String 'print'>>
                         211: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         214: <DUP>
                         215: <IFNONNULL 14>
                         218: <POP>
                         219: <NEW org/python/exceptions/NameError>
                         222: <DUP>
                         223: <LDC <String 'print'>>
                         225: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         228: <ATHROW>
                         229: <CHECKCAST <Class org/python/types/Object>>
                         232: <CHECKCAST <Class org/python/Callable>>
                         235: <ICONST_1>
                         236: <ANEWARRAY org/python/Object>
                         239: <DUP>
                         240: <ICONST_0>
                         241: <NEW org/python/types/Str>
                         244: <DUP>
                         245: <LDC <String 'Got an AttributeError'>>
                         247: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         250: <AASTORE>
                         251: <NEW java/util/Hashtable>
                         254: <DUP>
                         255: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         258: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         263: <POP>
                         264: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         267: <LDC <String 'print'>>
                         269: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         272: <DUP>
                         273: <IFNONNULL 27>
                         276: <POP>
                         277: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         280: <LDC <String 'print'>>
                         282: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         285: <DUP>
                         286: <IFNONNULL 14>
                         289: <POP>
                         290: <NEW org/python/exceptions/NameError>
                         293: <DUP>
                         294: <LDC <String 'print'>>
                         296: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         299: <ATHROW>
                         300: <CHECKCAST <Class org/python/types/Object>>
                         303: <CHECKCAST <Class org/python/Callable>>
                         306: <ICONST_1>
                         307: <ANEWARRAY org/python/Object>
                         310: <DUP>
                         311: <ICONST_0>
                         312: <NEW org/python/types/Str>
                         315: <DUP>
                         316: <LDC <String 'Do final cleanup'>>
                         318: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         321: <AASTORE>
                         322: <NEW java/util/Hashtable>
                         325: <DUP>
                         326: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         329: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         334: <POP>
                         335: <GOTO 227>
                         338: <ASTORE_0>
                         339: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         342: <LDC <String 'print'>>
                         344: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         347: <DUP>
                         348: <IFNONNULL 27>
                         351: <POP>
                         352: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         355: <LDC <String 'print'>>
                         357: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         360: <DUP>
                         361: <IFNONNULL 14>
                         364: <POP>
                         365: <NEW org/python/exceptions/NameError>
                         368: <DUP>
                         369: <LDC <String 'print'>>
                         371: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         374: <ATHROW>
                         375: <CHECKCAST <Class org/python/types/Object>>
                         378: <CHECKCAST <Class org/python/Callable>>
                         381: <ICONST_2>
                         382: <ANEWARRAY org/python/Object>
                         385: <DUP>
                         386: <ICONST_0>
                         387: <NEW org/python/types/Str>
                         390: <DUP>
                         391: <LDC <String 'Got a NameError'>>
                         393: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         396: <AASTORE>
                         397: <DUP>
                         398: <ICONST_1>
                         399: <ALOAD_0>
                         400: <AASTORE>
                         401: <NEW java/util/Hashtable>
                         404: <DUP>
                         405: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         408: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         413: <POP>
                         414: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         417: <LDC <String 'print'>>
                         419: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         422: <DUP>
                         423: <IFNONNULL 27>
                         426: <POP>
                         427: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         430: <LDC <String 'print'>>
                         432: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         435: <DUP>
                         436: <IFNONNULL 14>
                         439: <POP>
                         440: <NEW org/python/exceptions/NameError>
                         443: <DUP>
                         444: <LDC <String 'print'>>
                         446: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         449: <ATHROW>
                         450: <CHECKCAST <Class org/python/types/Object>>
                         453: <CHECKCAST <Class org/python/Callable>>
                         456: <ICONST_1>
                         457: <ANEWARRAY org/python/Object>
                         460: <DUP>
                         461: <ICONST_0>
                         462: <NEW org/python/types/Str>
                         465: <DUP>
                         466: <LDC <String 'Do final cleanup'>>
                         468: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         471: <AASTORE>
                         472: <NEW java/util/Hashtable>
                         475: <DUP>
                         476: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         479: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         484: <POP>
                         485: <GOTO 77>
                         488: <ASTORE_1>
                         489: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         492: <LDC <String 'print'>>
                         494: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         497: <DUP>
                         498: <IFNONNULL 27>
                         501: <POP>
                         502: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         505: <LDC <String 'print'>>
                         507: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         510: <DUP>
                         511: <IFNONNULL 14>
                         514: <POP>
                         515: <NEW org/python/exceptions/NameError>
                         518: <DUP>
                         519: <LDC <String 'print'>>
                         521: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         524: <ATHROW>
                         525: <CHECKCAST <Class org/python/types/Object>>
                         528: <CHECKCAST <Class org/python/Callable>>
                         531: <ICONST_1>
                         532: <ANEWARRAY org/python/Object>
                         535: <DUP>
                         536: <ICONST_0>
                         537: <NEW org/python/types/Str>
                         540: <DUP>
                         541: <LDC <String 'Do final cleanup'>>
                         543: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         546: <AASTORE>
                         547: <NEW java/util/Hashtable>
                         550: <DUP>
                         551: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         554: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         559: <POP>
                         560: <ALOAD_1>
                         561: <ATHROW>
                         562: <ACONST_NULL>
                         563: <ARETURN>
                     Exceptions: (5)
                         org/python/exceptions/AttributeError: 0-47 [192]
                         org/python/exceptions/NameError: 0-47 [338]
                         finally: 0-47 [488]
                         finally: 192-264 [488]
                         finally: 338-414 [488]
                     Attributes: (1)
                         LineNumberTable (34 bytes)
                             Line numbers (8 total):
                                 0: 3
                                 47: 9
                                 118: 11
                                 193: 5
                                 264: 11
                                 339: 7
                                 414: 11
                                 489: 11
                """)
