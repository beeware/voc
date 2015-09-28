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
                 Code (168 bytes)
                     Max stack: 7
                     Max locals: 0
                     Bytecode: (132 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GOTO 79>
                          54: <POP>
                          55: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          58: <LDC_W <String 'print'>>
                          61: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          64: <DUP>
                          65: <IFNONNULL 29>
                          68: <POP>
                          69: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          72: <LDC_W <String 'print'>>
                          75: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          78: <DUP>
                          79: <IFNONNULL 15>
                          82: <POP>
                          83: <NEW org/python/exceptions/NameError>
                          86: <DUP>
                          87: <LDC_W <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/types/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_1>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/types/Str>
                         109: <DUP>
                         110: <LDC_W <String 'Got an error'>>
                         113: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         116: <AASTORE>
                         117: <NEW java/util/Hashtable>
                         120: <DUP>
                         121: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         124: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         129: <POP>
                         130: <ACONST_NULL>
                         131: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/BaseException: 0-51 [54]
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 3
                                 55: 5
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
                 Code (168 bytes)
                     Max stack: 7
                     Max locals: 0
                     Bytecode: (132 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GOTO 79>
                          54: <POP>
                          55: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          58: <LDC_W <String 'print'>>
                          61: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          64: <DUP>
                          65: <IFNONNULL 29>
                          68: <POP>
                          69: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          72: <LDC_W <String 'print'>>
                          75: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          78: <DUP>
                          79: <IFNONNULL 15>
                          82: <POP>
                          83: <NEW org/python/exceptions/NameError>
                          86: <DUP>
                          87: <LDC_W <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/types/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_1>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/types/Str>
                         109: <DUP>
                         110: <LDC_W <String 'Got an error'>>
                         113: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         116: <AASTORE>
                         117: <NEW java/util/Hashtable>
                         120: <DUP>
                         121: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         124: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         129: <POP>
                         130: <ACONST_NULL>
                         131: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/AttributeError: 0-51 [54]
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 3
                                 55: 5
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
                 Code (172 bytes)
                     Max stack: 7
                     Max locals: 1
                     Bytecode: (136 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GOTO 83>
                          54: <ASTORE_0>
                          55: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          58: <LDC_W <String 'print'>>
                          61: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          64: <DUP>
                          65: <IFNONNULL 29>
                          68: <POP>
                          69: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          72: <LDC_W <String 'print'>>
                          75: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          78: <DUP>
                          79: <IFNONNULL 15>
                          82: <POP>
                          83: <NEW org/python/exceptions/NameError>
                          86: <DUP>
                          87: <LDC_W <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/types/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_2>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/types/Str>
                         109: <DUP>
                         110: <LDC_W <String 'Got an error'>>
                         113: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         116: <AASTORE>
                         117: <DUP>
                         118: <ICONST_1>
                         119: <ALOAD_0>
                         120: <AASTORE>
                         121: <NEW java/util/Hashtable>
                         124: <DUP>
                         125: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         128: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         133: <POP>
                         134: <ACONST_NULL>
                         135: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/AttributeError: 0-51 [54]
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 3
                                 55: 5
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
                 Code (259 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (211 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GOTO 158>
                          54: <POP>
                          55: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          58: <LDC_W <String 'print'>>
                          61: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          64: <DUP>
                          65: <IFNONNULL 29>
                          68: <POP>
                          69: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          72: <LDC_W <String 'print'>>
                          75: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          78: <DUP>
                          79: <IFNONNULL 15>
                          82: <POP>
                          83: <NEW org/python/exceptions/NameError>
                          86: <DUP>
                          87: <LDC_W <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/types/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_1>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/types/Str>
                         109: <DUP>
                         110: <LDC_W <String 'Got an AttributeError'>>
                         113: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         116: <AASTORE>
                         117: <NEW java/util/Hashtable>
                         120: <DUP>
                         121: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         124: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         129: <POP>
                         130: <GOTO 79>
                         133: <POP>
                         134: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         137: <LDC_W <String 'print'>>
                         140: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         143: <DUP>
                         144: <IFNONNULL 29>
                         147: <POP>
                         148: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         151: <LDC_W <String 'print'>>
                         154: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         157: <DUP>
                         158: <IFNONNULL 15>
                         161: <POP>
                         162: <NEW org/python/exceptions/NameError>
                         165: <DUP>
                         166: <LDC_W <String 'print'>>
                         169: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         172: <ATHROW>
                         173: <CHECKCAST <Class org/python/types/Object>>
                         176: <CHECKCAST <Class org/python/Callable>>
                         179: <ICONST_1>
                         180: <ANEWARRAY org/python/Object>
                         183: <DUP>
                         184: <ICONST_0>
                         185: <NEW org/python/types/Str>
                         188: <DUP>
                         189: <LDC_W <String 'Got a NameError'>>
                         192: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         195: <AASTORE>
                         196: <NEW java/util/Hashtable>
                         199: <DUP>
                         200: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         203: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         208: <POP>
                         209: <ACONST_NULL>
                         210: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-51 [54]
                         org/python/exceptions/NameError: 0-51 [133]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 55: 5
                                 134: 7
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
                 Code (267 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (219 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GOTO 166>
                          54: <ASTORE_0>
                          55: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          58: <LDC_W <String 'print'>>
                          61: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          64: <DUP>
                          65: <IFNONNULL 29>
                          68: <POP>
                          69: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          72: <LDC_W <String 'print'>>
                          75: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          78: <DUP>
                          79: <IFNONNULL 15>
                          82: <POP>
                          83: <NEW org/python/exceptions/NameError>
                          86: <DUP>
                          87: <LDC_W <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/types/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_2>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/types/Str>
                         109: <DUP>
                         110: <LDC_W <String 'Got an AttributeError'>>
                         113: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         116: <AASTORE>
                         117: <DUP>
                         118: <ICONST_1>
                         119: <ALOAD_0>
                         120: <AASTORE>
                         121: <NEW java/util/Hashtable>
                         124: <DUP>
                         125: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         128: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         133: <POP>
                         134: <GOTO 83>
                         137: <ASTORE_0>
                         138: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         141: <LDC_W <String 'print'>>
                         144: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         147: <DUP>
                         148: <IFNONNULL 29>
                         151: <POP>
                         152: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         155: <LDC_W <String 'print'>>
                         158: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         161: <DUP>
                         162: <IFNONNULL 15>
                         165: <POP>
                         166: <NEW org/python/exceptions/NameError>
                         169: <DUP>
                         170: <LDC_W <String 'print'>>
                         173: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         176: <ATHROW>
                         177: <CHECKCAST <Class org/python/types/Object>>
                         180: <CHECKCAST <Class org/python/Callable>>
                         183: <ICONST_2>
                         184: <ANEWARRAY org/python/Object>
                         187: <DUP>
                         188: <ICONST_0>
                         189: <NEW org/python/types/Str>
                         192: <DUP>
                         193: <LDC_W <String 'Got a NameError'>>
                         196: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         199: <AASTORE>
                         200: <DUP>
                         201: <ICONST_1>
                         202: <ALOAD_0>
                         203: <AASTORE>
                         204: <NEW java/util/Hashtable>
                         207: <DUP>
                         208: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         211: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         216: <POP>
                         217: <ACONST_NULL>
                         218: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-51 [54]
                         org/python/exceptions/NameError: 0-51 [137]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 55: 5
                                 138: 7
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
                 Code (259 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (211 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GOTO 158>
                          54: <POP>
                          55: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          58: <LDC_W <String 'print'>>
                          61: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          64: <DUP>
                          65: <IFNONNULL 29>
                          68: <POP>
                          69: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          72: <LDC_W <String 'print'>>
                          75: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          78: <DUP>
                          79: <IFNONNULL 15>
                          82: <POP>
                          83: <NEW org/python/exceptions/NameError>
                          86: <DUP>
                          87: <LDC_W <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/types/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_1>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/types/Str>
                         109: <DUP>
                         110: <LDC_W <String 'Got an AttributeError'>>
                         113: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         116: <AASTORE>
                         117: <NEW java/util/Hashtable>
                         120: <DUP>
                         121: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         124: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         129: <POP>
                         130: <GOTO 79>
                         133: <POP>
                         134: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         137: <LDC_W <String 'print'>>
                         140: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         143: <DUP>
                         144: <IFNONNULL 29>
                         147: <POP>
                         148: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         151: <LDC_W <String 'print'>>
                         154: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         157: <DUP>
                         158: <IFNONNULL 15>
                         161: <POP>
                         162: <NEW org/python/exceptions/NameError>
                         165: <DUP>
                         166: <LDC_W <String 'print'>>
                         169: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         172: <ATHROW>
                         173: <CHECKCAST <Class org/python/types/Object>>
                         176: <CHECKCAST <Class org/python/Callable>>
                         179: <ICONST_1>
                         180: <ANEWARRAY org/python/Object>
                         183: <DUP>
                         184: <ICONST_0>
                         185: <NEW org/python/types/Str>
                         188: <DUP>
                         189: <LDC_W <String 'Got a NameError'>>
                         192: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         195: <AASTORE>
                         196: <NEW java/util/Hashtable>
                         199: <DUP>
                         200: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         203: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         208: <POP>
                         209: <ACONST_NULL>
                         210: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-51 [54]
                         org/python/exceptions/NameError: 0-51 [133]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 55: 5
                                 134: 7
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
                 Code (267 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (219 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GOTO 166>
                          54: <ASTORE_0>
                          55: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          58: <LDC_W <String 'print'>>
                          61: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          64: <DUP>
                          65: <IFNONNULL 29>
                          68: <POP>
                          69: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          72: <LDC_W <String 'print'>>
                          75: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          78: <DUP>
                          79: <IFNONNULL 15>
                          82: <POP>
                          83: <NEW org/python/exceptions/NameError>
                          86: <DUP>
                          87: <LDC_W <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/types/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_2>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/types/Str>
                         109: <DUP>
                         110: <LDC_W <String 'Got an AttributeError'>>
                         113: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         116: <AASTORE>
                         117: <DUP>
                         118: <ICONST_1>
                         119: <ALOAD_0>
                         120: <AASTORE>
                         121: <NEW java/util/Hashtable>
                         124: <DUP>
                         125: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         128: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         133: <POP>
                         134: <GOTO 83>
                         137: <ASTORE_0>
                         138: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         141: <LDC_W <String 'print'>>
                         144: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         147: <DUP>
                         148: <IFNONNULL 29>
                         151: <POP>
                         152: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         155: <LDC_W <String 'print'>>
                         158: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         161: <DUP>
                         162: <IFNONNULL 15>
                         165: <POP>
                         166: <NEW org/python/exceptions/NameError>
                         169: <DUP>
                         170: <LDC_W <String 'print'>>
                         173: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         176: <ATHROW>
                         177: <CHECKCAST <Class org/python/types/Object>>
                         180: <CHECKCAST <Class org/python/Callable>>
                         183: <ICONST_2>
                         184: <ANEWARRAY org/python/Object>
                         187: <DUP>
                         188: <ICONST_0>
                         189: <NEW org/python/types/Str>
                         192: <DUP>
                         193: <LDC_W <String 'Got a NameError'>>
                         196: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         199: <AASTORE>
                         200: <DUP>
                         201: <ICONST_1>
                         202: <ALOAD_0>
                         203: <AASTORE>
                         204: <NEW java/util/Hashtable>
                         207: <DUP>
                         208: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         211: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         216: <POP>
                         217: <ACONST_NULL>
                         218: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-51 [54]
                         org/python/exceptions/NameError: 0-51 [137]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 55: 5
                                 138: 7
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
                 Code (263 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (215 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GOTO 162>
                          54: <POP>
                          55: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          58: <LDC_W <String 'print'>>
                          61: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          64: <DUP>
                          65: <IFNONNULL 29>
                          68: <POP>
                          69: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          72: <LDC_W <String 'print'>>
                          75: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          78: <DUP>
                          79: <IFNONNULL 15>
                          82: <POP>
                          83: <NEW org/python/exceptions/NameError>
                          86: <DUP>
                          87: <LDC_W <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/types/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_1>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/types/Str>
                         109: <DUP>
                         110: <LDC_W <String 'Got an AttributeError'>>
                         113: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         116: <AASTORE>
                         117: <NEW java/util/Hashtable>
                         120: <DUP>
                         121: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         124: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         129: <POP>
                         130: <GOTO 83>
                         133: <ASTORE_0>
                         134: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         137: <LDC_W <String 'print'>>
                         140: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         143: <DUP>
                         144: <IFNONNULL 29>
                         147: <POP>
                         148: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         151: <LDC_W <String 'print'>>
                         154: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         157: <DUP>
                         158: <IFNONNULL 15>
                         161: <POP>
                         162: <NEW org/python/exceptions/NameError>
                         165: <DUP>
                         166: <LDC_W <String 'print'>>
                         169: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         172: <ATHROW>
                         173: <CHECKCAST <Class org/python/types/Object>>
                         176: <CHECKCAST <Class org/python/Callable>>
                         179: <ICONST_2>
                         180: <ANEWARRAY org/python/Object>
                         183: <DUP>
                         184: <ICONST_0>
                         185: <NEW org/python/types/Str>
                         188: <DUP>
                         189: <LDC_W <String 'Got a NameError'>>
                         192: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         195: <AASTORE>
                         196: <DUP>
                         197: <ICONST_1>
                         198: <ALOAD_0>
                         199: <AASTORE>
                         200: <NEW java/util/Hashtable>
                         203: <DUP>
                         204: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         207: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         212: <POP>
                         213: <ACONST_NULL>
                         214: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-51 [54]
                         org/python/exceptions/NameError: 0-51 [133]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 55: 5
                                 134: 7
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
                 Code (263 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (215 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GOTO 162>
                          54: <ASTORE_0>
                          55: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          58: <LDC_W <String 'print'>>
                          61: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          64: <DUP>
                          65: <IFNONNULL 29>
                          68: <POP>
                          69: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          72: <LDC_W <String 'print'>>
                          75: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          78: <DUP>
                          79: <IFNONNULL 15>
                          82: <POP>
                          83: <NEW org/python/exceptions/NameError>
                          86: <DUP>
                          87: <LDC_W <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/types/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_2>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/types/Str>
                         109: <DUP>
                         110: <LDC_W <String 'Got an AttributeError'>>
                         113: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         116: <AASTORE>
                         117: <DUP>
                         118: <ICONST_1>
                         119: <ALOAD_0>
                         120: <AASTORE>
                         121: <NEW java/util/Hashtable>
                         124: <DUP>
                         125: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         128: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         133: <POP>
                         134: <GOTO 79>
                         137: <POP>
                         138: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         141: <LDC_W <String 'print'>>
                         144: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         147: <DUP>
                         148: <IFNONNULL 29>
                         151: <POP>
                         152: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         155: <LDC_W <String 'print'>>
                         158: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         161: <DUP>
                         162: <IFNONNULL 15>
                         165: <POP>
                         166: <NEW org/python/exceptions/NameError>
                         169: <DUP>
                         170: <LDC_W <String 'print'>>
                         173: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         176: <ATHROW>
                         177: <CHECKCAST <Class org/python/types/Object>>
                         180: <CHECKCAST <Class org/python/Callable>>
                         183: <ICONST_1>
                         184: <ANEWARRAY org/python/Object>
                         187: <DUP>
                         188: <ICONST_0>
                         189: <NEW org/python/types/Str>
                         192: <DUP>
                         193: <LDC_W <String 'Got a NameError'>>
                         196: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         199: <AASTORE>
                         200: <NEW java/util/Hashtable>
                         203: <DUP>
                         204: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         207: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         212: <POP>
                         213: <ACONST_NULL>
                         214: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-51 [54]
                         org/python/exceptions/NameError: 0-51 [137]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 55: 5
                                 138: 7
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
                 Code (354 bytes)
                     Max stack: 9
                     Max locals: 1
                     Bytecode: (294 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GOTO 241>
                          54: <ASTORE_0>
                          55: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          58: <LDC_W <String 'print'>>
                          61: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          64: <DUP>
                          65: <IFNONNULL 29>
                          68: <POP>
                          69: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          72: <LDC_W <String 'print'>>
                          75: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          78: <DUP>
                          79: <IFNONNULL 15>
                          82: <POP>
                          83: <NEW org/python/exceptions/NameError>
                          86: <DUP>
                          87: <LDC_W <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/types/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_2>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/types/Str>
                         109: <DUP>
                         110: <LDC_W <String 'Got an AttributeError'>>
                         113: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         116: <AASTORE>
                         117: <DUP>
                         118: <ICONST_1>
                         119: <ALOAD_0>
                         120: <AASTORE>
                         121: <NEW java/util/Hashtable>
                         124: <DUP>
                         125: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         128: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         133: <POP>
                         134: <GOTO 158>
                         137: <POP>
                         138: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         141: <LDC_W <String 'print'>>
                         144: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         147: <DUP>
                         148: <IFNONNULL 29>
                         151: <POP>
                         152: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         155: <LDC_W <String 'print'>>
                         158: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         161: <DUP>
                         162: <IFNONNULL 15>
                         165: <POP>
                         166: <NEW org/python/exceptions/NameError>
                         169: <DUP>
                         170: <LDC_W <String 'print'>>
                         173: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         176: <ATHROW>
                         177: <CHECKCAST <Class org/python/types/Object>>
                         180: <CHECKCAST <Class org/python/Callable>>
                         183: <ICONST_1>
                         184: <ANEWARRAY org/python/Object>
                         187: <DUP>
                         188: <ICONST_0>
                         189: <NEW org/python/types/Str>
                         192: <DUP>
                         193: <LDC_W <String 'Got a NameError'>>
                         196: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         199: <AASTORE>
                         200: <NEW java/util/Hashtable>
                         203: <DUP>
                         204: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         207: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         212: <POP>
                         213: <GOTO 79>
                         216: <POP>
                         217: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         220: <LDC_W <String 'print'>>
                         223: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         226: <DUP>
                         227: <IFNONNULL 29>
                         230: <POP>
                         231: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         234: <LDC_W <String 'print'>>
                         237: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         240: <DUP>
                         241: <IFNONNULL 15>
                         244: <POP>
                         245: <NEW org/python/exceptions/NameError>
                         248: <DUP>
                         249: <LDC_W <String 'print'>>
                         252: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         255: <ATHROW>
                         256: <CHECKCAST <Class org/python/types/Object>>
                         259: <CHECKCAST <Class org/python/Callable>>
                         262: <ICONST_1>
                         263: <ANEWARRAY org/python/Object>
                         266: <DUP>
                         267: <ICONST_0>
                         268: <NEW org/python/types/Str>
                         271: <DUP>
                         272: <LDC_W <String 'Got an anonymous error'>>
                         275: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         278: <AASTORE>
                         279: <NEW java/util/Hashtable>
                         282: <DUP>
                         283: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         286: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         291: <POP>
                         292: <ACONST_NULL>
                         293: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-51 [54]
                         org/python/exceptions/NameError: 0-51 [137]
                         org/python/exceptions/BaseException: 0-51 [216]
                     Attributes: (1)
                         LineNumberTable (18 bytes)
                             Line numbers (4 total):
                                 0: 3
                                 55: 5
                                 138: 7
                                 217: 9
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
                 Code (207 bytes)
                     Max stack: 8
                     Max locals: 2
                     Bytecode: (167 bytes)
                           0: <NEW org/python/types/Int>
                           3: <DUP>
                           4: <ICONST_3>
                           5: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                           8: <ASTORE_0>
                           9: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          12: <LDC_W <String 'print'>>
                          15: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          18: <DUP>
                          19: <IFNONNULL 29>
                          22: <POP>
                          23: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          26: <LDC_W <String 'print'>>
                          29: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          32: <DUP>
                          33: <IFNONNULL 15>
                          36: <POP>
                          37: <NEW org/python/exceptions/NameError>
                          40: <DUP>
                          41: <LDC_W <String 'print'>>
                          44: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          47: <ATHROW>
                          48: <CHECKCAST <Class org/python/types/Object>>
                          51: <CHECKCAST <Class org/python/Callable>>
                          54: <ICONST_1>
                          55: <ANEWARRAY org/python/Object>
                          58: <DUP>
                          59: <ICONST_0>
                          60: <NEW org/python/types/Str>
                          63: <DUP>
                          64: <LDC_W <String 'Do final cleanup'>>
                          67: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                          70: <AASTORE>
                          71: <NEW java/util/Hashtable>
                          74: <DUP>
                          75: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          78: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          83: <POP>
                          84: <GOTO 81>
                          87: <ASTORE_1>
                          88: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          91: <LDC_W <String 'print'>>
                          94: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          97: <DUP>
                          98: <IFNONNULL 29>
                         101: <POP>
                         102: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         105: <LDC_W <String 'print'>>
                         108: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         111: <DUP>
                         112: <IFNONNULL 15>
                         115: <POP>
                         116: <NEW org/python/exceptions/NameError>
                         119: <DUP>
                         120: <LDC_W <String 'print'>>
                         123: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         126: <ATHROW>
                         127: <CHECKCAST <Class org/python/types/Object>>
                         130: <CHECKCAST <Class org/python/Callable>>
                         133: <ICONST_1>
                         134: <ANEWARRAY org/python/Object>
                         137: <DUP>
                         138: <ICONST_0>
                         139: <NEW org/python/types/Str>
                         142: <DUP>
                         143: <LDC_W <String 'Do final cleanup'>>
                         146: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         149: <AASTORE>
                         150: <NEW java/util/Hashtable>
                         153: <DUP>
                         154: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         157: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         162: <POP>
                         163: <ALOAD_1>
                         164: <ATHROW>
                         165: <ACONST_NULL>
                         166: <ARETURN>
                     Exceptions: (1)
                         finally: 0-9 [87]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 9: 5
                                 88: 5
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
                 Code (427 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (363 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC_W <String 'print'>>
                          57: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          60: <DUP>
                          61: <IFNONNULL 29>
                          64: <POP>
                          65: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          68: <LDC_W <String 'print'>>
                          71: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          74: <DUP>
                          75: <IFNONNULL 15>
                          78: <POP>
                          79: <NEW org/python/exceptions/NameError>
                          82: <DUP>
                          83: <LDC_W <String 'print'>>
                          86: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          89: <ATHROW>
                          90: <CHECKCAST <Class org/python/types/Object>>
                          93: <CHECKCAST <Class org/python/Callable>>
                          96: <ICONST_1>
                          97: <ANEWARRAY org/python/Object>
                         100: <DUP>
                         101: <ICONST_0>
                         102: <NEW org/python/types/Str>
                         105: <DUP>
                         106: <LDC_W <String 'Do final cleanup'>>
                         109: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <GOTO 235>
                         129: <POP>
                         130: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         133: <LDC_W <String 'print'>>
                         136: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         139: <DUP>
                         140: <IFNONNULL 29>
                         143: <POP>
                         144: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         147: <LDC_W <String 'print'>>
                         150: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         153: <DUP>
                         154: <IFNONNULL 15>
                         157: <POP>
                         158: <NEW org/python/exceptions/NameError>
                         161: <DUP>
                         162: <LDC_W <String 'print'>>
                         165: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         168: <ATHROW>
                         169: <CHECKCAST <Class org/python/types/Object>>
                         172: <CHECKCAST <Class org/python/Callable>>
                         175: <ICONST_1>
                         176: <ANEWARRAY org/python/Object>
                         179: <DUP>
                         180: <ICONST_0>
                         181: <NEW org/python/types/Str>
                         184: <DUP>
                         185: <LDC_W <String 'Got an error'>>
                         188: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         191: <AASTORE>
                         192: <NEW java/util/Hashtable>
                         195: <DUP>
                         196: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         199: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         204: <POP>
                         205: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         208: <LDC_W <String 'print'>>
                         211: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         214: <DUP>
                         215: <IFNONNULL 29>
                         218: <POP>
                         219: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         222: <LDC_W <String 'print'>>
                         225: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         228: <DUP>
                         229: <IFNONNULL 15>
                         232: <POP>
                         233: <NEW org/python/exceptions/NameError>
                         236: <DUP>
                         237: <LDC_W <String 'print'>>
                         240: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         243: <ATHROW>
                         244: <CHECKCAST <Class org/python/types/Object>>
                         247: <CHECKCAST <Class org/python/Callable>>
                         250: <ICONST_1>
                         251: <ANEWARRAY org/python/Object>
                         254: <DUP>
                         255: <ICONST_0>
                         256: <NEW org/python/types/Str>
                         259: <DUP>
                         260: <LDC_W <String 'Do final cleanup'>>
                         263: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         266: <AASTORE>
                         267: <NEW java/util/Hashtable>
                         270: <DUP>
                         271: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         274: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         279: <POP>
                         280: <GOTO 81>
                         283: <ASTORE_0>
                         284: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         287: <LDC_W <String 'print'>>
                         290: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         293: <DUP>
                         294: <IFNONNULL 29>
                         297: <POP>
                         298: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         301: <LDC_W <String 'print'>>
                         304: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         307: <DUP>
                         308: <IFNONNULL 15>
                         311: <POP>
                         312: <NEW org/python/exceptions/NameError>
                         315: <DUP>
                         316: <LDC_W <String 'print'>>
                         319: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         322: <ATHROW>
                         323: <CHECKCAST <Class org/python/types/Object>>
                         326: <CHECKCAST <Class org/python/Callable>>
                         329: <ICONST_1>
                         330: <ANEWARRAY org/python/Object>
                         333: <DUP>
                         334: <ICONST_0>
                         335: <NEW org/python/types/Str>
                         338: <DUP>
                         339: <LDC_W <String 'Do final cleanup'>>
                         342: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         345: <AASTORE>
                         346: <NEW java/util/Hashtable>
                         349: <DUP>
                         350: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         353: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         358: <POP>
                         359: <ALOAD_0>
                         360: <ATHROW>
                         361: <ACONST_NULL>
                         362: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/BaseException: 0-51 [129]
                         finally: 0-51 [283]
                         finally: 129-205 [283]
                     Attributes: (1)
                         LineNumberTable (22 bytes)
                             Line numbers (5 total):
                                 0: 3
                                 51: 7
                                 130: 5
                                 205: 7
                                 284: 7
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
                 Code (427 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (363 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC_W <String 'print'>>
                          57: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          60: <DUP>
                          61: <IFNONNULL 29>
                          64: <POP>
                          65: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          68: <LDC_W <String 'print'>>
                          71: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          74: <DUP>
                          75: <IFNONNULL 15>
                          78: <POP>
                          79: <NEW org/python/exceptions/NameError>
                          82: <DUP>
                          83: <LDC_W <String 'print'>>
                          86: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          89: <ATHROW>
                          90: <CHECKCAST <Class org/python/types/Object>>
                          93: <CHECKCAST <Class org/python/Callable>>
                          96: <ICONST_1>
                          97: <ANEWARRAY org/python/Object>
                         100: <DUP>
                         101: <ICONST_0>
                         102: <NEW org/python/types/Str>
                         105: <DUP>
                         106: <LDC_W <String 'Do final cleanup'>>
                         109: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <GOTO 235>
                         129: <POP>
                         130: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         133: <LDC_W <String 'print'>>
                         136: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         139: <DUP>
                         140: <IFNONNULL 29>
                         143: <POP>
                         144: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         147: <LDC_W <String 'print'>>
                         150: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         153: <DUP>
                         154: <IFNONNULL 15>
                         157: <POP>
                         158: <NEW org/python/exceptions/NameError>
                         161: <DUP>
                         162: <LDC_W <String 'print'>>
                         165: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         168: <ATHROW>
                         169: <CHECKCAST <Class org/python/types/Object>>
                         172: <CHECKCAST <Class org/python/Callable>>
                         175: <ICONST_1>
                         176: <ANEWARRAY org/python/Object>
                         179: <DUP>
                         180: <ICONST_0>
                         181: <NEW org/python/types/Str>
                         184: <DUP>
                         185: <LDC_W <String 'Got an error'>>
                         188: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         191: <AASTORE>
                         192: <NEW java/util/Hashtable>
                         195: <DUP>
                         196: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         199: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         204: <POP>
                         205: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         208: <LDC_W <String 'print'>>
                         211: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         214: <DUP>
                         215: <IFNONNULL 29>
                         218: <POP>
                         219: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         222: <LDC_W <String 'print'>>
                         225: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         228: <DUP>
                         229: <IFNONNULL 15>
                         232: <POP>
                         233: <NEW org/python/exceptions/NameError>
                         236: <DUP>
                         237: <LDC_W <String 'print'>>
                         240: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         243: <ATHROW>
                         244: <CHECKCAST <Class org/python/types/Object>>
                         247: <CHECKCAST <Class org/python/Callable>>
                         250: <ICONST_1>
                         251: <ANEWARRAY org/python/Object>
                         254: <DUP>
                         255: <ICONST_0>
                         256: <NEW org/python/types/Str>
                         259: <DUP>
                         260: <LDC_W <String 'Do final cleanup'>>
                         263: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         266: <AASTORE>
                         267: <NEW java/util/Hashtable>
                         270: <DUP>
                         271: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         274: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         279: <POP>
                         280: <GOTO 81>
                         283: <ASTORE_0>
                         284: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         287: <LDC_W <String 'print'>>
                         290: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         293: <DUP>
                         294: <IFNONNULL 29>
                         297: <POP>
                         298: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         301: <LDC_W <String 'print'>>
                         304: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         307: <DUP>
                         308: <IFNONNULL 15>
                         311: <POP>
                         312: <NEW org/python/exceptions/NameError>
                         315: <DUP>
                         316: <LDC_W <String 'print'>>
                         319: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         322: <ATHROW>
                         323: <CHECKCAST <Class org/python/types/Object>>
                         326: <CHECKCAST <Class org/python/Callable>>
                         329: <ICONST_1>
                         330: <ANEWARRAY org/python/Object>
                         333: <DUP>
                         334: <ICONST_0>
                         335: <NEW org/python/types/Str>
                         338: <DUP>
                         339: <LDC_W <String 'Do final cleanup'>>
                         342: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         345: <AASTORE>
                         346: <NEW java/util/Hashtable>
                         349: <DUP>
                         350: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         353: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         358: <POP>
                         359: <ALOAD_0>
                         360: <ATHROW>
                         361: <ACONST_NULL>
                         362: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-51 [129]
                         finally: 0-51 [283]
                         finally: 129-205 [283]
                     Attributes: (1)
                         LineNumberTable (22 bytes)
                             Line numbers (5 total):
                                 0: 3
                                 51: 7
                                 130: 5
                                 205: 7
                                 284: 7
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
                 Code (431 bytes)
                     Max stack: 10
                     Max locals: 2
                     Bytecode: (367 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC_W <String 'print'>>
                          57: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          60: <DUP>
                          61: <IFNONNULL 29>
                          64: <POP>
                          65: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          68: <LDC_W <String 'print'>>
                          71: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          74: <DUP>
                          75: <IFNONNULL 15>
                          78: <POP>
                          79: <NEW org/python/exceptions/NameError>
                          82: <DUP>
                          83: <LDC_W <String 'print'>>
                          86: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          89: <ATHROW>
                          90: <CHECKCAST <Class org/python/types/Object>>
                          93: <CHECKCAST <Class org/python/Callable>>
                          96: <ICONST_1>
                          97: <ANEWARRAY org/python/Object>
                         100: <DUP>
                         101: <ICONST_0>
                         102: <NEW org/python/types/Str>
                         105: <DUP>
                         106: <LDC_W <String 'Do final cleanup'>>
                         109: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <GOTO 239>
                         129: <ASTORE_0>
                         130: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         133: <LDC_W <String 'print'>>
                         136: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         139: <DUP>
                         140: <IFNONNULL 29>
                         143: <POP>
                         144: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         147: <LDC_W <String 'print'>>
                         150: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         153: <DUP>
                         154: <IFNONNULL 15>
                         157: <POP>
                         158: <NEW org/python/exceptions/NameError>
                         161: <DUP>
                         162: <LDC_W <String 'print'>>
                         165: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         168: <ATHROW>
                         169: <CHECKCAST <Class org/python/types/Object>>
                         172: <CHECKCAST <Class org/python/Callable>>
                         175: <ICONST_2>
                         176: <ANEWARRAY org/python/Object>
                         179: <DUP>
                         180: <ICONST_0>
                         181: <NEW org/python/types/Str>
                         184: <DUP>
                         185: <LDC_W <String 'Got an AttributeError'>>
                         188: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         191: <AASTORE>
                         192: <DUP>
                         193: <ICONST_1>
                         194: <ALOAD_0>
                         195: <AASTORE>
                         196: <NEW java/util/Hashtable>
                         199: <DUP>
                         200: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         203: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         208: <POP>
                         209: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         212: <LDC_W <String 'print'>>
                         215: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         218: <DUP>
                         219: <IFNONNULL 29>
                         222: <POP>
                         223: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         226: <LDC_W <String 'print'>>
                         229: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         232: <DUP>
                         233: <IFNONNULL 15>
                         236: <POP>
                         237: <NEW org/python/exceptions/NameError>
                         240: <DUP>
                         241: <LDC_W <String 'print'>>
                         244: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         247: <ATHROW>
                         248: <CHECKCAST <Class org/python/types/Object>>
                         251: <CHECKCAST <Class org/python/Callable>>
                         254: <ICONST_1>
                         255: <ANEWARRAY org/python/Object>
                         258: <DUP>
                         259: <ICONST_0>
                         260: <NEW org/python/types/Str>
                         263: <DUP>
                         264: <LDC_W <String 'Do final cleanup'>>
                         267: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         270: <AASTORE>
                         271: <NEW java/util/Hashtable>
                         274: <DUP>
                         275: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         278: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         283: <POP>
                         284: <GOTO 81>
                         287: <ASTORE_1>
                         288: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         291: <LDC_W <String 'print'>>
                         294: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         297: <DUP>
                         298: <IFNONNULL 29>
                         301: <POP>
                         302: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         305: <LDC_W <String 'print'>>
                         308: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         311: <DUP>
                         312: <IFNONNULL 15>
                         315: <POP>
                         316: <NEW org/python/exceptions/NameError>
                         319: <DUP>
                         320: <LDC_W <String 'print'>>
                         323: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         326: <ATHROW>
                         327: <CHECKCAST <Class org/python/types/Object>>
                         330: <CHECKCAST <Class org/python/Callable>>
                         333: <ICONST_1>
                         334: <ANEWARRAY org/python/Object>
                         337: <DUP>
                         338: <ICONST_0>
                         339: <NEW org/python/types/Str>
                         342: <DUP>
                         343: <LDC_W <String 'Do final cleanup'>>
                         346: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         349: <AASTORE>
                         350: <NEW java/util/Hashtable>
                         353: <DUP>
                         354: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         357: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         362: <POP>
                         363: <ALOAD_1>
                         364: <ATHROW>
                         365: <ACONST_NULL>
                         366: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-51 [129]
                         finally: 0-51 [287]
                         finally: 129-209 [287]
                     Attributes: (1)
                         LineNumberTable (22 bytes)
                             Line numbers (5 total):
                                 0: 3
                                 51: 7
                                 130: 5
                                 209: 7
                                 288: 7
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
                 Code (609 bytes)
                     Max stack: 12
                     Max locals: 2
                     Bytecode: (521 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC_W <String 'print'>>
                          57: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          60: <DUP>
                          61: <IFNONNULL 29>
                          64: <POP>
                          65: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          68: <LDC_W <String 'print'>>
                          71: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          74: <DUP>
                          75: <IFNONNULL 15>
                          78: <POP>
                          79: <NEW org/python/exceptions/NameError>
                          82: <DUP>
                          83: <LDC_W <String 'print'>>
                          86: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          89: <ATHROW>
                          90: <CHECKCAST <Class org/python/types/Object>>
                          93: <CHECKCAST <Class org/python/Callable>>
                          96: <ICONST_1>
                          97: <ANEWARRAY org/python/Object>
                         100: <DUP>
                         101: <ICONST_0>
                         102: <NEW org/python/types/Str>
                         105: <DUP>
                         106: <LDC_W <String 'Do final cleanup'>>
                         109: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <GOTO 393>
                         129: <POP>
                         130: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         133: <LDC_W <String 'print'>>
                         136: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         139: <DUP>
                         140: <IFNONNULL 29>
                         143: <POP>
                         144: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         147: <LDC_W <String 'print'>>
                         150: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         153: <DUP>
                         154: <IFNONNULL 15>
                         157: <POP>
                         158: <NEW org/python/exceptions/NameError>
                         161: <DUP>
                         162: <LDC_W <String 'print'>>
                         165: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         168: <ATHROW>
                         169: <CHECKCAST <Class org/python/types/Object>>
                         172: <CHECKCAST <Class org/python/Callable>>
                         175: <ICONST_1>
                         176: <ANEWARRAY org/python/Object>
                         179: <DUP>
                         180: <ICONST_0>
                         181: <NEW org/python/types/Str>
                         184: <DUP>
                         185: <LDC_W <String 'Got an AttributeError'>>
                         188: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         191: <AASTORE>
                         192: <NEW java/util/Hashtable>
                         195: <DUP>
                         196: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         199: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         204: <POP>
                         205: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         208: <LDC_W <String 'print'>>
                         211: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         214: <DUP>
                         215: <IFNONNULL 29>
                         218: <POP>
                         219: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         222: <LDC_W <String 'print'>>
                         225: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         228: <DUP>
                         229: <IFNONNULL 15>
                         232: <POP>
                         233: <NEW org/python/exceptions/NameError>
                         236: <DUP>
                         237: <LDC_W <String 'print'>>
                         240: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         243: <ATHROW>
                         244: <CHECKCAST <Class org/python/types/Object>>
                         247: <CHECKCAST <Class org/python/Callable>>
                         250: <ICONST_1>
                         251: <ANEWARRAY org/python/Object>
                         254: <DUP>
                         255: <ICONST_0>
                         256: <NEW org/python/types/Str>
                         259: <DUP>
                         260: <LDC_W <String 'Do final cleanup'>>
                         263: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         266: <AASTORE>
                         267: <NEW java/util/Hashtable>
                         270: <DUP>
                         271: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         274: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         279: <POP>
                         280: <GOTO 239>
                         283: <ASTORE_0>
                         284: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         287: <LDC_W <String 'print'>>
                         290: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         293: <DUP>
                         294: <IFNONNULL 29>
                         297: <POP>
                         298: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         301: <LDC_W <String 'print'>>
                         304: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         307: <DUP>
                         308: <IFNONNULL 15>
                         311: <POP>
                         312: <NEW org/python/exceptions/NameError>
                         315: <DUP>
                         316: <LDC_W <String 'print'>>
                         319: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         322: <ATHROW>
                         323: <CHECKCAST <Class org/python/types/Object>>
                         326: <CHECKCAST <Class org/python/Callable>>
                         329: <ICONST_2>
                         330: <ANEWARRAY org/python/Object>
                         333: <DUP>
                         334: <ICONST_0>
                         335: <NEW org/python/types/Str>
                         338: <DUP>
                         339: <LDC_W <String 'Got a NameError'>>
                         342: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         345: <AASTORE>
                         346: <DUP>
                         347: <ICONST_1>
                         348: <ALOAD_0>
                         349: <AASTORE>
                         350: <NEW java/util/Hashtable>
                         353: <DUP>
                         354: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         357: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         362: <POP>
                         363: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         366: <LDC_W <String 'print'>>
                         369: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         372: <DUP>
                         373: <IFNONNULL 29>
                         376: <POP>
                         377: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         380: <LDC_W <String 'print'>>
                         383: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         386: <DUP>
                         387: <IFNONNULL 15>
                         390: <POP>
                         391: <NEW org/python/exceptions/NameError>
                         394: <DUP>
                         395: <LDC_W <String 'print'>>
                         398: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         401: <ATHROW>
                         402: <CHECKCAST <Class org/python/types/Object>>
                         405: <CHECKCAST <Class org/python/Callable>>
                         408: <ICONST_1>
                         409: <ANEWARRAY org/python/Object>
                         412: <DUP>
                         413: <ICONST_0>
                         414: <NEW org/python/types/Str>
                         417: <DUP>
                         418: <LDC_W <String 'Do final cleanup'>>
                         421: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         424: <AASTORE>
                         425: <NEW java/util/Hashtable>
                         428: <DUP>
                         429: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         432: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         437: <POP>
                         438: <GOTO 81>
                         441: <ASTORE_1>
                         442: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         445: <LDC_W <String 'print'>>
                         448: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         451: <DUP>
                         452: <IFNONNULL 29>
                         455: <POP>
                         456: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         459: <LDC_W <String 'print'>>
                         462: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         465: <DUP>
                         466: <IFNONNULL 15>
                         469: <POP>
                         470: <NEW org/python/exceptions/NameError>
                         473: <DUP>
                         474: <LDC_W <String 'print'>>
                         477: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         480: <ATHROW>
                         481: <CHECKCAST <Class org/python/types/Object>>
                         484: <CHECKCAST <Class org/python/Callable>>
                         487: <ICONST_1>
                         488: <ANEWARRAY org/python/Object>
                         491: <DUP>
                         492: <ICONST_0>
                         493: <NEW org/python/types/Str>
                         496: <DUP>
                         497: <LDC_W <String 'Do final cleanup'>>
                         500: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         503: <AASTORE>
                         504: <NEW java/util/Hashtable>
                         507: <DUP>
                         508: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         511: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         516: <POP>
                         517: <ALOAD_1>
                         518: <ATHROW>
                         519: <ACONST_NULL>
                         520: <ARETURN>
                     Exceptions: (5)
                         org/python/exceptions/AttributeError: 0-51 [129]
                         org/python/exceptions/NameError: 0-51 [283]
                         finally: 0-51 [441]
                         finally: 129-205 [441]
                         finally: 283-363 [441]
                     Attributes: (1)
                         LineNumberTable (30 bytes)
                             Line numbers (7 total):
                                 0: 3
                                 51: 9
                                 130: 5
                                 205: 9
                                 284: 7
                                 363: 9
                                 442: 9
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
                 Code (247 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (207 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC_W <String 'print'>>
                          57: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          60: <DUP>
                          61: <IFNONNULL 29>
                          64: <POP>
                          65: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          68: <LDC_W <String 'print'>>
                          71: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          74: <DUP>
                          75: <IFNONNULL 15>
                          78: <POP>
                          79: <NEW org/python/exceptions/NameError>
                          82: <DUP>
                          83: <LDC_W <String 'print'>>
                          86: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          89: <ATHROW>
                          90: <CHECKCAST <Class org/python/types/Object>>
                          93: <CHECKCAST <Class org/python/Callable>>
                          96: <ICONST_1>
                          97: <ANEWARRAY org/python/Object>
                         100: <DUP>
                         101: <ICONST_0>
                         102: <NEW org/python/types/Str>
                         105: <DUP>
                         106: <LDC_W <String 'Do else handling'>>
                         109: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <GOTO 79>
                         129: <POP>
                         130: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         133: <LDC_W <String 'print'>>
                         136: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         139: <DUP>
                         140: <IFNONNULL 29>
                         143: <POP>
                         144: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         147: <LDC_W <String 'print'>>
                         150: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         153: <DUP>
                         154: <IFNONNULL 15>
                         157: <POP>
                         158: <NEW org/python/exceptions/NameError>
                         161: <DUP>
                         162: <LDC_W <String 'print'>>
                         165: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         168: <ATHROW>
                         169: <CHECKCAST <Class org/python/types/Object>>
                         172: <CHECKCAST <Class org/python/Callable>>
                         175: <ICONST_1>
                         176: <ANEWARRAY org/python/Object>
                         179: <DUP>
                         180: <ICONST_0>
                         181: <NEW org/python/types/Str>
                         184: <DUP>
                         185: <LDC_W <String 'Got an error'>>
                         188: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         191: <AASTORE>
                         192: <NEW java/util/Hashtable>
                         195: <DUP>
                         196: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         199: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         204: <POP>
                         205: <ACONST_NULL>
                         206: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/BaseException: 0-51 [129]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 51: 7
                                 130: 5
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
                 Code (247 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (207 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC_W <String 'print'>>
                          57: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          60: <DUP>
                          61: <IFNONNULL 29>
                          64: <POP>
                          65: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          68: <LDC_W <String 'print'>>
                          71: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          74: <DUP>
                          75: <IFNONNULL 15>
                          78: <POP>
                          79: <NEW org/python/exceptions/NameError>
                          82: <DUP>
                          83: <LDC_W <String 'print'>>
                          86: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          89: <ATHROW>
                          90: <CHECKCAST <Class org/python/types/Object>>
                          93: <CHECKCAST <Class org/python/Callable>>
                          96: <ICONST_1>
                          97: <ANEWARRAY org/python/Object>
                         100: <DUP>
                         101: <ICONST_0>
                         102: <NEW org/python/types/Str>
                         105: <DUP>
                         106: <LDC_W <String 'Do else handling'>>
                         109: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <GOTO 79>
                         129: <POP>
                         130: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         133: <LDC_W <String 'print'>>
                         136: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         139: <DUP>
                         140: <IFNONNULL 29>
                         143: <POP>
                         144: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         147: <LDC_W <String 'print'>>
                         150: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         153: <DUP>
                         154: <IFNONNULL 15>
                         157: <POP>
                         158: <NEW org/python/exceptions/NameError>
                         161: <DUP>
                         162: <LDC_W <String 'print'>>
                         165: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         168: <ATHROW>
                         169: <CHECKCAST <Class org/python/types/Object>>
                         172: <CHECKCAST <Class org/python/Callable>>
                         175: <ICONST_1>
                         176: <ANEWARRAY org/python/Object>
                         179: <DUP>
                         180: <ICONST_0>
                         181: <NEW org/python/types/Str>
                         184: <DUP>
                         185: <LDC_W <String 'Got an error'>>
                         188: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         191: <AASTORE>
                         192: <NEW java/util/Hashtable>
                         195: <DUP>
                         196: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         199: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         204: <POP>
                         205: <ACONST_NULL>
                         206: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/AttributeError: 0-51 [129]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 51: 7
                                 130: 5
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
                 Code (342 bytes)
                     Max stack: 9
                     Max locals: 1
                     Bytecode: (290 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC_W <String 'print'>>
                          57: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          60: <DUP>
                          61: <IFNONNULL 29>
                          64: <POP>
                          65: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          68: <LDC_W <String 'print'>>
                          71: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          74: <DUP>
                          75: <IFNONNULL 15>
                          78: <POP>
                          79: <NEW org/python/exceptions/NameError>
                          82: <DUP>
                          83: <LDC_W <String 'print'>>
                          86: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          89: <ATHROW>
                          90: <CHECKCAST <Class org/python/types/Object>>
                          93: <CHECKCAST <Class org/python/Callable>>
                          96: <ICONST_1>
                          97: <ANEWARRAY org/python/Object>
                         100: <DUP>
                         101: <ICONST_0>
                         102: <NEW org/python/types/Str>
                         105: <DUP>
                         106: <LDC_W <String 'Do else handling'>>
                         109: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <GOTO 162>
                         129: <POP>
                         130: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         133: <LDC_W <String 'print'>>
                         136: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         139: <DUP>
                         140: <IFNONNULL 29>
                         143: <POP>
                         144: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         147: <LDC_W <String 'print'>>
                         150: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         153: <DUP>
                         154: <IFNONNULL 15>
                         157: <POP>
                         158: <NEW org/python/exceptions/NameError>
                         161: <DUP>
                         162: <LDC_W <String 'print'>>
                         165: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         168: <ATHROW>
                         169: <CHECKCAST <Class org/python/types/Object>>
                         172: <CHECKCAST <Class org/python/Callable>>
                         175: <ICONST_1>
                         176: <ANEWARRAY org/python/Object>
                         179: <DUP>
                         180: <ICONST_0>
                         181: <NEW org/python/types/Str>
                         184: <DUP>
                         185: <LDC_W <String 'Got an AttributeError'>>
                         188: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         191: <AASTORE>
                         192: <NEW java/util/Hashtable>
                         195: <DUP>
                         196: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         199: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         204: <POP>
                         205: <GOTO 83>
                         208: <ASTORE_0>
                         209: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         212: <LDC_W <String 'print'>>
                         215: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         218: <DUP>
                         219: <IFNONNULL 29>
                         222: <POP>
                         223: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         226: <LDC_W <String 'print'>>
                         229: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         232: <DUP>
                         233: <IFNONNULL 15>
                         236: <POP>
                         237: <NEW org/python/exceptions/NameError>
                         240: <DUP>
                         241: <LDC_W <String 'print'>>
                         244: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         247: <ATHROW>
                         248: <CHECKCAST <Class org/python/types/Object>>
                         251: <CHECKCAST <Class org/python/Callable>>
                         254: <ICONST_2>
                         255: <ANEWARRAY org/python/Object>
                         258: <DUP>
                         259: <ICONST_0>
                         260: <NEW org/python/types/Str>
                         263: <DUP>
                         264: <LDC_W <String 'Got a NameError'>>
                         267: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         270: <AASTORE>
                         271: <DUP>
                         272: <ICONST_1>
                         273: <ALOAD_0>
                         274: <AASTORE>
                         275: <NEW java/util/Hashtable>
                         278: <DUP>
                         279: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         282: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         287: <POP>
                         288: <ACONST_NULL>
                         289: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-51 [129]
                         org/python/exceptions/NameError: 0-51 [208]
                     Attributes: (1)
                         LineNumberTable (18 bytes)
                             Line numbers (4 total):
                                 0: 3
                                 51: 9
                                 130: 5
                                 209: 7
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
                 Code (506 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (438 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC_W <String 'print'>>
                          57: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          60: <DUP>
                          61: <IFNONNULL 29>
                          64: <POP>
                          65: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          68: <LDC_W <String 'print'>>
                          71: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          74: <DUP>
                          75: <IFNONNULL 15>
                          78: <POP>
                          79: <NEW org/python/exceptions/NameError>
                          82: <DUP>
                          83: <LDC_W <String 'print'>>
                          86: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          89: <ATHROW>
                          90: <CHECKCAST <Class org/python/types/Object>>
                          93: <CHECKCAST <Class org/python/Callable>>
                          96: <ICONST_1>
                          97: <ANEWARRAY org/python/Object>
                         100: <DUP>
                         101: <ICONST_0>
                         102: <NEW org/python/types/Str>
                         105: <DUP>
                         106: <LDC_W <String 'Do else handling'>>
                         109: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         129: <LDC_W <String 'print'>>
                         132: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         135: <DUP>
                         136: <IFNONNULL 29>
                         139: <POP>
                         140: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         143: <LDC_W <String 'print'>>
                         146: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         149: <DUP>
                         150: <IFNONNULL 15>
                         153: <POP>
                         154: <NEW org/python/exceptions/NameError>
                         157: <DUP>
                         158: <LDC_W <String 'print'>>
                         161: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         164: <ATHROW>
                         165: <CHECKCAST <Class org/python/types/Object>>
                         168: <CHECKCAST <Class org/python/Callable>>
                         171: <ICONST_1>
                         172: <ANEWARRAY org/python/Object>
                         175: <DUP>
                         176: <ICONST_0>
                         177: <NEW org/python/types/Str>
                         180: <DUP>
                         181: <LDC_W <String 'Do final cleanup'>>
                         184: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         187: <AASTORE>
                         188: <NEW java/util/Hashtable>
                         191: <DUP>
                         192: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         195: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         200: <POP>
                         201: <GOTO 235>
                         204: <POP>
                         205: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         208: <LDC_W <String 'print'>>
                         211: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         214: <DUP>
                         215: <IFNONNULL 29>
                         218: <POP>
                         219: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         222: <LDC_W <String 'print'>>
                         225: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         228: <DUP>
                         229: <IFNONNULL 15>
                         232: <POP>
                         233: <NEW org/python/exceptions/NameError>
                         236: <DUP>
                         237: <LDC_W <String 'print'>>
                         240: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         243: <ATHROW>
                         244: <CHECKCAST <Class org/python/types/Object>>
                         247: <CHECKCAST <Class org/python/Callable>>
                         250: <ICONST_1>
                         251: <ANEWARRAY org/python/Object>
                         254: <DUP>
                         255: <ICONST_0>
                         256: <NEW org/python/types/Str>
                         259: <DUP>
                         260: <LDC_W <String 'Got an error'>>
                         263: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         266: <AASTORE>
                         267: <NEW java/util/Hashtable>
                         270: <DUP>
                         271: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         274: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         279: <POP>
                         280: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         283: <LDC_W <String 'print'>>
                         286: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         289: <DUP>
                         290: <IFNONNULL 29>
                         293: <POP>
                         294: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         297: <LDC_W <String 'print'>>
                         300: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         303: <DUP>
                         304: <IFNONNULL 15>
                         307: <POP>
                         308: <NEW org/python/exceptions/NameError>
                         311: <DUP>
                         312: <LDC_W <String 'print'>>
                         315: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         318: <ATHROW>
                         319: <CHECKCAST <Class org/python/types/Object>>
                         322: <CHECKCAST <Class org/python/Callable>>
                         325: <ICONST_1>
                         326: <ANEWARRAY org/python/Object>
                         329: <DUP>
                         330: <ICONST_0>
                         331: <NEW org/python/types/Str>
                         334: <DUP>
                         335: <LDC_W <String 'Do final cleanup'>>
                         338: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         341: <AASTORE>
                         342: <NEW java/util/Hashtable>
                         345: <DUP>
                         346: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         349: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         354: <POP>
                         355: <GOTO 81>
                         358: <ASTORE_0>
                         359: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         362: <LDC_W <String 'print'>>
                         365: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         368: <DUP>
                         369: <IFNONNULL 29>
                         372: <POP>
                         373: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         376: <LDC_W <String 'print'>>
                         379: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         382: <DUP>
                         383: <IFNONNULL 15>
                         386: <POP>
                         387: <NEW org/python/exceptions/NameError>
                         390: <DUP>
                         391: <LDC_W <String 'print'>>
                         394: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         397: <ATHROW>
                         398: <CHECKCAST <Class org/python/types/Object>>
                         401: <CHECKCAST <Class org/python/Callable>>
                         404: <ICONST_1>
                         405: <ANEWARRAY org/python/Object>
                         408: <DUP>
                         409: <ICONST_0>
                         410: <NEW org/python/types/Str>
                         413: <DUP>
                         414: <LDC_W <String 'Do final cleanup'>>
                         417: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         420: <AASTORE>
                         421: <NEW java/util/Hashtable>
                         424: <DUP>
                         425: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         428: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         433: <POP>
                         434: <ALOAD_0>
                         435: <ATHROW>
                         436: <ACONST_NULL>
                         437: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/BaseException: 0-51 [204]
                         finally: 0-51 [358]
                         finally: 204-280 [358]
                     Attributes: (1)
                         LineNumberTable (26 bytes)
                             Line numbers (6 total):
                                 0: 3
                                 51: 7
                                 126: 9
                                 205: 5
                                 280: 9
                                 359: 9
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
                 Code (506 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (438 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC_W <String 'print'>>
                          57: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          60: <DUP>
                          61: <IFNONNULL 29>
                          64: <POP>
                          65: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          68: <LDC_W <String 'print'>>
                          71: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          74: <DUP>
                          75: <IFNONNULL 15>
                          78: <POP>
                          79: <NEW org/python/exceptions/NameError>
                          82: <DUP>
                          83: <LDC_W <String 'print'>>
                          86: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          89: <ATHROW>
                          90: <CHECKCAST <Class org/python/types/Object>>
                          93: <CHECKCAST <Class org/python/Callable>>
                          96: <ICONST_1>
                          97: <ANEWARRAY org/python/Object>
                         100: <DUP>
                         101: <ICONST_0>
                         102: <NEW org/python/types/Str>
                         105: <DUP>
                         106: <LDC_W <String 'Do else handling'>>
                         109: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         129: <LDC_W <String 'print'>>
                         132: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         135: <DUP>
                         136: <IFNONNULL 29>
                         139: <POP>
                         140: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         143: <LDC_W <String 'print'>>
                         146: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         149: <DUP>
                         150: <IFNONNULL 15>
                         153: <POP>
                         154: <NEW org/python/exceptions/NameError>
                         157: <DUP>
                         158: <LDC_W <String 'print'>>
                         161: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         164: <ATHROW>
                         165: <CHECKCAST <Class org/python/types/Object>>
                         168: <CHECKCAST <Class org/python/Callable>>
                         171: <ICONST_1>
                         172: <ANEWARRAY org/python/Object>
                         175: <DUP>
                         176: <ICONST_0>
                         177: <NEW org/python/types/Str>
                         180: <DUP>
                         181: <LDC_W <String 'Do final cleanup'>>
                         184: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         187: <AASTORE>
                         188: <NEW java/util/Hashtable>
                         191: <DUP>
                         192: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         195: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         200: <POP>
                         201: <GOTO 235>
                         204: <POP>
                         205: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         208: <LDC_W <String 'print'>>
                         211: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         214: <DUP>
                         215: <IFNONNULL 29>
                         218: <POP>
                         219: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         222: <LDC_W <String 'print'>>
                         225: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         228: <DUP>
                         229: <IFNONNULL 15>
                         232: <POP>
                         233: <NEW org/python/exceptions/NameError>
                         236: <DUP>
                         237: <LDC_W <String 'print'>>
                         240: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         243: <ATHROW>
                         244: <CHECKCAST <Class org/python/types/Object>>
                         247: <CHECKCAST <Class org/python/Callable>>
                         250: <ICONST_1>
                         251: <ANEWARRAY org/python/Object>
                         254: <DUP>
                         255: <ICONST_0>
                         256: <NEW org/python/types/Str>
                         259: <DUP>
                         260: <LDC_W <String 'Got an error'>>
                         263: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         266: <AASTORE>
                         267: <NEW java/util/Hashtable>
                         270: <DUP>
                         271: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         274: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         279: <POP>
                         280: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         283: <LDC_W <String 'print'>>
                         286: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         289: <DUP>
                         290: <IFNONNULL 29>
                         293: <POP>
                         294: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         297: <LDC_W <String 'print'>>
                         300: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         303: <DUP>
                         304: <IFNONNULL 15>
                         307: <POP>
                         308: <NEW org/python/exceptions/NameError>
                         311: <DUP>
                         312: <LDC_W <String 'print'>>
                         315: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         318: <ATHROW>
                         319: <CHECKCAST <Class org/python/types/Object>>
                         322: <CHECKCAST <Class org/python/Callable>>
                         325: <ICONST_1>
                         326: <ANEWARRAY org/python/Object>
                         329: <DUP>
                         330: <ICONST_0>
                         331: <NEW org/python/types/Str>
                         334: <DUP>
                         335: <LDC_W <String 'Do final cleanup'>>
                         338: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         341: <AASTORE>
                         342: <NEW java/util/Hashtable>
                         345: <DUP>
                         346: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         349: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         354: <POP>
                         355: <GOTO 81>
                         358: <ASTORE_0>
                         359: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         362: <LDC_W <String 'print'>>
                         365: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         368: <DUP>
                         369: <IFNONNULL 29>
                         372: <POP>
                         373: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         376: <LDC_W <String 'print'>>
                         379: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         382: <DUP>
                         383: <IFNONNULL 15>
                         386: <POP>
                         387: <NEW org/python/exceptions/NameError>
                         390: <DUP>
                         391: <LDC_W <String 'print'>>
                         394: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         397: <ATHROW>
                         398: <CHECKCAST <Class org/python/types/Object>>
                         401: <CHECKCAST <Class org/python/Callable>>
                         404: <ICONST_1>
                         405: <ANEWARRAY org/python/Object>
                         408: <DUP>
                         409: <ICONST_0>
                         410: <NEW org/python/types/Str>
                         413: <DUP>
                         414: <LDC_W <String 'Do final cleanup'>>
                         417: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         420: <AASTORE>
                         421: <NEW java/util/Hashtable>
                         424: <DUP>
                         425: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         428: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         433: <POP>
                         434: <ALOAD_0>
                         435: <ATHROW>
                         436: <ACONST_NULL>
                         437: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-51 [204]
                         finally: 0-51 [358]
                         finally: 204-280 [358]
                     Attributes: (1)
                         LineNumberTable (26 bytes)
                             Line numbers (6 total):
                                 0: 3
                                 51: 7
                                 126: 9
                                 205: 5
                                 280: 9
                                 359: 9
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
                 Code (688 bytes)
                     Max stack: 12
                     Max locals: 2
                     Bytecode: (596 bytes)
                           0: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                           3: <LDC_W <String 'obj'>>
                           6: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                           9: <DUP>
                          10: <IFNONNULL 29>
                          13: <POP>
                          14: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          17: <LDC_W <String 'obj'>>
                          20: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          23: <DUP>
                          24: <IFNONNULL 15>
                          27: <POP>
                          28: <NEW org/python/exceptions/NameError>
                          31: <DUP>
                          32: <LDC_W <String 'obj'>>
                          35: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          38: <ATHROW>
                          39: <CHECKCAST <Class org/python/types/Object>>
                          42: <LDC_W <String 'no_such_attribute'>>
                          45: <INVOKEINTERFACE org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          50: <POP>
                          51: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          54: <LDC_W <String 'print'>>
                          57: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          60: <DUP>
                          61: <IFNONNULL 29>
                          64: <POP>
                          65: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          68: <LDC_W <String 'print'>>
                          71: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          74: <DUP>
                          75: <IFNONNULL 15>
                          78: <POP>
                          79: <NEW org/python/exceptions/NameError>
                          82: <DUP>
                          83: <LDC_W <String 'print'>>
                          86: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          89: <ATHROW>
                          90: <CHECKCAST <Class org/python/types/Object>>
                          93: <CHECKCAST <Class org/python/Callable>>
                          96: <ICONST_1>
                          97: <ANEWARRAY org/python/Object>
                         100: <DUP>
                         101: <ICONST_0>
                         102: <NEW org/python/types/Str>
                         105: <DUP>
                         106: <LDC_W <String 'Do else handling'>>
                         109: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         112: <AASTORE>
                         113: <NEW java/util/Hashtable>
                         116: <DUP>
                         117: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         120: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         125: <POP>
                         126: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         129: <LDC_W <String 'print'>>
                         132: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         135: <DUP>
                         136: <IFNONNULL 29>
                         139: <POP>
                         140: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         143: <LDC_W <String 'print'>>
                         146: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         149: <DUP>
                         150: <IFNONNULL 15>
                         153: <POP>
                         154: <NEW org/python/exceptions/NameError>
                         157: <DUP>
                         158: <LDC_W <String 'print'>>
                         161: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         164: <ATHROW>
                         165: <CHECKCAST <Class org/python/types/Object>>
                         168: <CHECKCAST <Class org/python/Callable>>
                         171: <ICONST_1>
                         172: <ANEWARRAY org/python/Object>
                         175: <DUP>
                         176: <ICONST_0>
                         177: <NEW org/python/types/Str>
                         180: <DUP>
                         181: <LDC_W <String 'Do final cleanup'>>
                         184: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         187: <AASTORE>
                         188: <NEW java/util/Hashtable>
                         191: <DUP>
                         192: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         195: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         200: <POP>
                         201: <GOTO 393>
                         204: <POP>
                         205: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         208: <LDC_W <String 'print'>>
                         211: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         214: <DUP>
                         215: <IFNONNULL 29>
                         218: <POP>
                         219: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         222: <LDC_W <String 'print'>>
                         225: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         228: <DUP>
                         229: <IFNONNULL 15>
                         232: <POP>
                         233: <NEW org/python/exceptions/NameError>
                         236: <DUP>
                         237: <LDC_W <String 'print'>>
                         240: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         243: <ATHROW>
                         244: <CHECKCAST <Class org/python/types/Object>>
                         247: <CHECKCAST <Class org/python/Callable>>
                         250: <ICONST_1>
                         251: <ANEWARRAY org/python/Object>
                         254: <DUP>
                         255: <ICONST_0>
                         256: <NEW org/python/types/Str>
                         259: <DUP>
                         260: <LDC_W <String 'Got an AttributeError'>>
                         263: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         266: <AASTORE>
                         267: <NEW java/util/Hashtable>
                         270: <DUP>
                         271: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         274: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         279: <POP>
                         280: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         283: <LDC_W <String 'print'>>
                         286: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         289: <DUP>
                         290: <IFNONNULL 29>
                         293: <POP>
                         294: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         297: <LDC_W <String 'print'>>
                         300: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         303: <DUP>
                         304: <IFNONNULL 15>
                         307: <POP>
                         308: <NEW org/python/exceptions/NameError>
                         311: <DUP>
                         312: <LDC_W <String 'print'>>
                         315: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         318: <ATHROW>
                         319: <CHECKCAST <Class org/python/types/Object>>
                         322: <CHECKCAST <Class org/python/Callable>>
                         325: <ICONST_1>
                         326: <ANEWARRAY org/python/Object>
                         329: <DUP>
                         330: <ICONST_0>
                         331: <NEW org/python/types/Str>
                         334: <DUP>
                         335: <LDC_W <String 'Do final cleanup'>>
                         338: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         341: <AASTORE>
                         342: <NEW java/util/Hashtable>
                         345: <DUP>
                         346: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         349: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         354: <POP>
                         355: <GOTO 239>
                         358: <ASTORE_0>
                         359: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         362: <LDC_W <String 'print'>>
                         365: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         368: <DUP>
                         369: <IFNONNULL 29>
                         372: <POP>
                         373: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         376: <LDC_W <String 'print'>>
                         379: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         382: <DUP>
                         383: <IFNONNULL 15>
                         386: <POP>
                         387: <NEW org/python/exceptions/NameError>
                         390: <DUP>
                         391: <LDC_W <String 'print'>>
                         394: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         397: <ATHROW>
                         398: <CHECKCAST <Class org/python/types/Object>>
                         401: <CHECKCAST <Class org/python/Callable>>
                         404: <ICONST_2>
                         405: <ANEWARRAY org/python/Object>
                         408: <DUP>
                         409: <ICONST_0>
                         410: <NEW org/python/types/Str>
                         413: <DUP>
                         414: <LDC_W <String 'Got a NameError'>>
                         417: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         420: <AASTORE>
                         421: <DUP>
                         422: <ICONST_1>
                         423: <ALOAD_0>
                         424: <AASTORE>
                         425: <NEW java/util/Hashtable>
                         428: <DUP>
                         429: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         432: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         437: <POP>
                         438: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         441: <LDC_W <String 'print'>>
                         444: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         447: <DUP>
                         448: <IFNONNULL 29>
                         451: <POP>
                         452: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         455: <LDC_W <String 'print'>>
                         458: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         461: <DUP>
                         462: <IFNONNULL 15>
                         465: <POP>
                         466: <NEW org/python/exceptions/NameError>
                         469: <DUP>
                         470: <LDC_W <String 'print'>>
                         473: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         476: <ATHROW>
                         477: <CHECKCAST <Class org/python/types/Object>>
                         480: <CHECKCAST <Class org/python/Callable>>
                         483: <ICONST_1>
                         484: <ANEWARRAY org/python/Object>
                         487: <DUP>
                         488: <ICONST_0>
                         489: <NEW org/python/types/Str>
                         492: <DUP>
                         493: <LDC_W <String 'Do final cleanup'>>
                         496: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         499: <AASTORE>
                         500: <NEW java/util/Hashtable>
                         503: <DUP>
                         504: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         507: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         512: <POP>
                         513: <GOTO 81>
                         516: <ASTORE_1>
                         517: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         520: <LDC_W <String 'print'>>
                         523: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         526: <DUP>
                         527: <IFNONNULL 29>
                         530: <POP>
                         531: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         534: <LDC_W <String 'print'>>
                         537: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         540: <DUP>
                         541: <IFNONNULL 15>
                         544: <POP>
                         545: <NEW org/python/exceptions/NameError>
                         548: <DUP>
                         549: <LDC_W <String 'print'>>
                         552: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         555: <ATHROW>
                         556: <CHECKCAST <Class org/python/types/Object>>
                         559: <CHECKCAST <Class org/python/Callable>>
                         562: <ICONST_1>
                         563: <ANEWARRAY org/python/Object>
                         566: <DUP>
                         567: <ICONST_0>
                         568: <NEW org/python/types/Str>
                         571: <DUP>
                         572: <LDC_W <String 'Do final cleanup'>>
                         575: <INVOKESPECIAL org/python/types/Str.<init> (Ljava/lang/String;)V>
                         578: <AASTORE>
                         579: <NEW java/util/Hashtable>
                         582: <DUP>
                         583: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         586: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         591: <POP>
                         592: <ALOAD_1>
                         593: <ATHROW>
                         594: <ACONST_NULL>
                         595: <ARETURN>
                     Exceptions: (5)
                         org/python/exceptions/AttributeError: 0-51 [204]
                         org/python/exceptions/NameError: 0-51 [358]
                         finally: 0-51 [516]
                         finally: 204-280 [516]
                         finally: 358-438 [516]
                     Attributes: (1)
                         LineNumberTable (34 bytes)
                             Line numbers (8 total):
                                 0: 3
                                 51: 9
                                 126: 11
                                 205: 5
                                 280: 11
                                 359: 7
                                 438: 11
                                 517: 11
                """)
