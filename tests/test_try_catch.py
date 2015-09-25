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
                 Code (158 bytes)
                     Max stack: 7
                     Max locals: 0
                     Bytecode: (122 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GOTO 75>
                          48: <POP>
                          49: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          52: <LDC <String 'print'>>
                          54: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          57: <DUP>
                          58: <IFNONNULL 27>
                          61: <POP>
                          62: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          65: <LDC <String 'print'>>
                          67: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          70: <DUP>
                          71: <IFNONNULL 14>
                          74: <POP>
                          75: <NEW org/python/exceptions/NameError>
                          78: <DUP>
                          79: <LDC <String 'print'>>
                          81: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          84: <ATHROW>
                          85: <CHECKCAST <Class org/python/Object>>
                          88: <CHECKCAST <Class org/python/Callable>>
                          91: <ICONST_1>
                          92: <ANEWARRAY org/python/Object>
                          95: <DUP>
                          96: <ICONST_0>
                          97: <NEW org/python/Object>
                         100: <DUP>
                         101: <LDC <String 'Got an error'>>
                         103: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         106: <AASTORE>
                         107: <NEW java/util/Hashtable>
                         110: <DUP>
                         111: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         114: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         119: <POP>
                         120: <ACONST_NULL>
                         121: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/BaseException: 0-45 [48]
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 3
                                 49: 5
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
                 Code (158 bytes)
                     Max stack: 7
                     Max locals: 0
                     Bytecode: (122 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GOTO 75>
                          48: <POP>
                          49: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          52: <LDC <String 'print'>>
                          54: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          57: <DUP>
                          58: <IFNONNULL 27>
                          61: <POP>
                          62: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          65: <LDC <String 'print'>>
                          67: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          70: <DUP>
                          71: <IFNONNULL 14>
                          74: <POP>
                          75: <NEW org/python/exceptions/NameError>
                          78: <DUP>
                          79: <LDC <String 'print'>>
                          81: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          84: <ATHROW>
                          85: <CHECKCAST <Class org/python/Object>>
                          88: <CHECKCAST <Class org/python/Callable>>
                          91: <ICONST_1>
                          92: <ANEWARRAY org/python/Object>
                          95: <DUP>
                          96: <ICONST_0>
                          97: <NEW org/python/Object>
                         100: <DUP>
                         101: <LDC <String 'Got an error'>>
                         103: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         106: <AASTORE>
                         107: <NEW java/util/Hashtable>
                         110: <DUP>
                         111: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         114: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         119: <POP>
                         120: <ACONST_NULL>
                         121: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/AttributeError: 0-45 [48]
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 3
                                 49: 5
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
                 Code (171 bytes)
                     Max stack: 7
                     Max locals: 1
                     Bytecode: (135 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GOTO 88>
                          48: <ASTORE_0>
                          49: <NEW org/python/Object>
                          52: <DUP>
                          53: <ALOAD_0>
                          54: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                          57: <ASTORE_0>
                          58: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 27>
                          70: <POP>
                          71: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          74: <LDC <String 'print'>>
                          76: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          79: <DUP>
                          80: <IFNONNULL 14>
                          83: <POP>
                          84: <NEW org/python/exceptions/NameError>
                          87: <DUP>
                          88: <LDC <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_2>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/Object>
                         109: <DUP>
                         110: <LDC <String 'Got an error'>>
                         112: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         115: <AASTORE>
                         116: <DUP>
                         117: <ICONST_1>
                         118: <ALOAD_0>
                         119: <AASTORE>
                         120: <NEW java/util/Hashtable>
                         123: <DUP>
                         124: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         127: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         132: <POP>
                         133: <ACONST_NULL>
                         134: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/AttributeError: 0-45 [48]
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 3
                                 58: 5
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
                 Code (245 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (197 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GOTO 150>
                          48: <POP>
                          49: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          52: <LDC <String 'print'>>
                          54: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          57: <DUP>
                          58: <IFNONNULL 27>
                          61: <POP>
                          62: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          65: <LDC <String 'print'>>
                          67: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          70: <DUP>
                          71: <IFNONNULL 14>
                          74: <POP>
                          75: <NEW org/python/exceptions/NameError>
                          78: <DUP>
                          79: <LDC <String 'print'>>
                          81: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          84: <ATHROW>
                          85: <CHECKCAST <Class org/python/Object>>
                          88: <CHECKCAST <Class org/python/Callable>>
                          91: <ICONST_1>
                          92: <ANEWARRAY org/python/Object>
                          95: <DUP>
                          96: <ICONST_0>
                          97: <NEW org/python/Object>
                         100: <DUP>
                         101: <LDC <String 'Got an AttributeError'>>
                         103: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         106: <AASTORE>
                         107: <NEW java/util/Hashtable>
                         110: <DUP>
                         111: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         114: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         119: <POP>
                         120: <GOTO 75>
                         123: <POP>
                         124: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         127: <LDC <String 'print'>>
                         129: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         132: <DUP>
                         133: <IFNONNULL 27>
                         136: <POP>
                         137: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         140: <LDC <String 'print'>>
                         142: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         145: <DUP>
                         146: <IFNONNULL 14>
                         149: <POP>
                         150: <NEW org/python/exceptions/NameError>
                         153: <DUP>
                         154: <LDC <String 'print'>>
                         156: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         159: <ATHROW>
                         160: <CHECKCAST <Class org/python/Object>>
                         163: <CHECKCAST <Class org/python/Callable>>
                         166: <ICONST_1>
                         167: <ANEWARRAY org/python/Object>
                         170: <DUP>
                         171: <ICONST_0>
                         172: <NEW org/python/Object>
                         175: <DUP>
                         176: <LDC <String 'Got a NameError'>>
                         178: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         181: <AASTORE>
                         182: <NEW java/util/Hashtable>
                         185: <DUP>
                         186: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         189: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         194: <POP>
                         195: <ACONST_NULL>
                         196: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-45 [48]
                         org/python/exceptions/NameError: 0-45 [123]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 49: 5
                                 124: 7
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
                 Code (271 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (223 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GOTO 176>
                          48: <ASTORE_0>
                          49: <NEW org/python/Object>
                          52: <DUP>
                          53: <ALOAD_0>
                          54: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                          57: <ASTORE_0>
                          58: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 27>
                          70: <POP>
                          71: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          74: <LDC <String 'print'>>
                          76: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          79: <DUP>
                          80: <IFNONNULL 14>
                          83: <POP>
                          84: <NEW org/python/exceptions/NameError>
                          87: <DUP>
                          88: <LDC <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_2>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/Object>
                         109: <DUP>
                         110: <LDC <String 'Got an AttributeError'>>
                         112: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         115: <AASTORE>
                         116: <DUP>
                         117: <ICONST_1>
                         118: <ALOAD_0>
                         119: <AASTORE>
                         120: <NEW java/util/Hashtable>
                         123: <DUP>
                         124: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         127: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         132: <POP>
                         133: <GOTO 88>
                         136: <ASTORE_0>
                         137: <NEW org/python/Object>
                         140: <DUP>
                         141: <ALOAD_0>
                         142: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                         145: <ASTORE_0>
                         146: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         149: <LDC <String 'print'>>
                         151: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         154: <DUP>
                         155: <IFNONNULL 27>
                         158: <POP>
                         159: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         162: <LDC <String 'print'>>
                         164: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         167: <DUP>
                         168: <IFNONNULL 14>
                         171: <POP>
                         172: <NEW org/python/exceptions/NameError>
                         175: <DUP>
                         176: <LDC <String 'print'>>
                         178: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         181: <ATHROW>
                         182: <CHECKCAST <Class org/python/Object>>
                         185: <CHECKCAST <Class org/python/Callable>>
                         188: <ICONST_2>
                         189: <ANEWARRAY org/python/Object>
                         192: <DUP>
                         193: <ICONST_0>
                         194: <NEW org/python/Object>
                         197: <DUP>
                         198: <LDC <String 'Got a NameError'>>
                         200: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         203: <AASTORE>
                         204: <DUP>
                         205: <ICONST_1>
                         206: <ALOAD_0>
                         207: <AASTORE>
                         208: <NEW java/util/Hashtable>
                         211: <DUP>
                         212: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         215: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         220: <POP>
                         221: <ACONST_NULL>
                         222: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-45 [48]
                         org/python/exceptions/NameError: 0-45 [136]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 58: 5
                                 146: 7
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
                 Code (245 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (197 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GOTO 150>
                          48: <POP>
                          49: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          52: <LDC <String 'print'>>
                          54: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          57: <DUP>
                          58: <IFNONNULL 27>
                          61: <POP>
                          62: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          65: <LDC <String 'print'>>
                          67: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          70: <DUP>
                          71: <IFNONNULL 14>
                          74: <POP>
                          75: <NEW org/python/exceptions/NameError>
                          78: <DUP>
                          79: <LDC <String 'print'>>
                          81: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          84: <ATHROW>
                          85: <CHECKCAST <Class org/python/Object>>
                          88: <CHECKCAST <Class org/python/Callable>>
                          91: <ICONST_1>
                          92: <ANEWARRAY org/python/Object>
                          95: <DUP>
                          96: <ICONST_0>
                          97: <NEW org/python/Object>
                         100: <DUP>
                         101: <LDC <String 'Got an AttributeError'>>
                         103: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         106: <AASTORE>
                         107: <NEW java/util/Hashtable>
                         110: <DUP>
                         111: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         114: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         119: <POP>
                         120: <GOTO 75>
                         123: <POP>
                         124: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         127: <LDC <String 'print'>>
                         129: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         132: <DUP>
                         133: <IFNONNULL 27>
                         136: <POP>
                         137: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         140: <LDC <String 'print'>>
                         142: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         145: <DUP>
                         146: <IFNONNULL 14>
                         149: <POP>
                         150: <NEW org/python/exceptions/NameError>
                         153: <DUP>
                         154: <LDC <String 'print'>>
                         156: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         159: <ATHROW>
                         160: <CHECKCAST <Class org/python/Object>>
                         163: <CHECKCAST <Class org/python/Callable>>
                         166: <ICONST_1>
                         167: <ANEWARRAY org/python/Object>
                         170: <DUP>
                         171: <ICONST_0>
                         172: <NEW org/python/Object>
                         175: <DUP>
                         176: <LDC <String 'Got a NameError'>>
                         178: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         181: <AASTORE>
                         182: <NEW java/util/Hashtable>
                         185: <DUP>
                         186: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         189: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         194: <POP>
                         195: <ACONST_NULL>
                         196: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-45 [48]
                         org/python/exceptions/NameError: 0-45 [123]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 49: 5
                                 124: 7
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
                 Code (271 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (223 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GOTO 176>
                          48: <ASTORE_0>
                          49: <NEW org/python/Object>
                          52: <DUP>
                          53: <ALOAD_0>
                          54: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                          57: <ASTORE_0>
                          58: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 27>
                          70: <POP>
                          71: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          74: <LDC <String 'print'>>
                          76: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          79: <DUP>
                          80: <IFNONNULL 14>
                          83: <POP>
                          84: <NEW org/python/exceptions/NameError>
                          87: <DUP>
                          88: <LDC <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_2>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/Object>
                         109: <DUP>
                         110: <LDC <String 'Got an AttributeError'>>
                         112: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         115: <AASTORE>
                         116: <DUP>
                         117: <ICONST_1>
                         118: <ALOAD_0>
                         119: <AASTORE>
                         120: <NEW java/util/Hashtable>
                         123: <DUP>
                         124: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         127: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         132: <POP>
                         133: <GOTO 88>
                         136: <ASTORE_0>
                         137: <NEW org/python/Object>
                         140: <DUP>
                         141: <ALOAD_0>
                         142: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                         145: <ASTORE_0>
                         146: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         149: <LDC <String 'print'>>
                         151: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         154: <DUP>
                         155: <IFNONNULL 27>
                         158: <POP>
                         159: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         162: <LDC <String 'print'>>
                         164: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         167: <DUP>
                         168: <IFNONNULL 14>
                         171: <POP>
                         172: <NEW org/python/exceptions/NameError>
                         175: <DUP>
                         176: <LDC <String 'print'>>
                         178: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         181: <ATHROW>
                         182: <CHECKCAST <Class org/python/Object>>
                         185: <CHECKCAST <Class org/python/Callable>>
                         188: <ICONST_2>
                         189: <ANEWARRAY org/python/Object>
                         192: <DUP>
                         193: <ICONST_0>
                         194: <NEW org/python/Object>
                         197: <DUP>
                         198: <LDC <String 'Got a NameError'>>
                         200: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         203: <AASTORE>
                         204: <DUP>
                         205: <ICONST_1>
                         206: <ALOAD_0>
                         207: <AASTORE>
                         208: <NEW java/util/Hashtable>
                         211: <DUP>
                         212: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         215: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         220: <POP>
                         221: <ACONST_NULL>
                         222: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-45 [48]
                         org/python/exceptions/NameError: 0-45 [136]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 58: 5
                                 146: 7
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
                 Code (258 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (210 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GOTO 163>
                          48: <POP>
                          49: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          52: <LDC <String 'print'>>
                          54: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          57: <DUP>
                          58: <IFNONNULL 27>
                          61: <POP>
                          62: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          65: <LDC <String 'print'>>
                          67: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          70: <DUP>
                          71: <IFNONNULL 14>
                          74: <POP>
                          75: <NEW org/python/exceptions/NameError>
                          78: <DUP>
                          79: <LDC <String 'print'>>
                          81: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          84: <ATHROW>
                          85: <CHECKCAST <Class org/python/Object>>
                          88: <CHECKCAST <Class org/python/Callable>>
                          91: <ICONST_1>
                          92: <ANEWARRAY org/python/Object>
                          95: <DUP>
                          96: <ICONST_0>
                          97: <NEW org/python/Object>
                         100: <DUP>
                         101: <LDC <String 'Got an AttributeError'>>
                         103: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         106: <AASTORE>
                         107: <NEW java/util/Hashtable>
                         110: <DUP>
                         111: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         114: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         119: <POP>
                         120: <GOTO 88>
                         123: <ASTORE_0>
                         124: <NEW org/python/Object>
                         127: <DUP>
                         128: <ALOAD_0>
                         129: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                         132: <ASTORE_0>
                         133: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         136: <LDC <String 'print'>>
                         138: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         141: <DUP>
                         142: <IFNONNULL 27>
                         145: <POP>
                         146: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         149: <LDC <String 'print'>>
                         151: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         154: <DUP>
                         155: <IFNONNULL 14>
                         158: <POP>
                         159: <NEW org/python/exceptions/NameError>
                         162: <DUP>
                         163: <LDC <String 'print'>>
                         165: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         168: <ATHROW>
                         169: <CHECKCAST <Class org/python/Object>>
                         172: <CHECKCAST <Class org/python/Callable>>
                         175: <ICONST_2>
                         176: <ANEWARRAY org/python/Object>
                         179: <DUP>
                         180: <ICONST_0>
                         181: <NEW org/python/Object>
                         184: <DUP>
                         185: <LDC <String 'Got a NameError'>>
                         187: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         190: <AASTORE>
                         191: <DUP>
                         192: <ICONST_1>
                         193: <ALOAD_0>
                         194: <AASTORE>
                         195: <NEW java/util/Hashtable>
                         198: <DUP>
                         199: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         202: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         207: <POP>
                         208: <ACONST_NULL>
                         209: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-45 [48]
                         org/python/exceptions/NameError: 0-45 [123]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 49: 5
                                 133: 7
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
                 Code (258 bytes)
                     Max stack: 8
                     Max locals: 1
                     Bytecode: (210 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GOTO 163>
                          48: <ASTORE_0>
                          49: <NEW org/python/Object>
                          52: <DUP>
                          53: <ALOAD_0>
                          54: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                          57: <ASTORE_0>
                          58: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 27>
                          70: <POP>
                          71: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          74: <LDC <String 'print'>>
                          76: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          79: <DUP>
                          80: <IFNONNULL 14>
                          83: <POP>
                          84: <NEW org/python/exceptions/NameError>
                          87: <DUP>
                          88: <LDC <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_2>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/Object>
                         109: <DUP>
                         110: <LDC <String 'Got an AttributeError'>>
                         112: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         115: <AASTORE>
                         116: <DUP>
                         117: <ICONST_1>
                         118: <ALOAD_0>
                         119: <AASTORE>
                         120: <NEW java/util/Hashtable>
                         123: <DUP>
                         124: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         127: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         132: <POP>
                         133: <GOTO 75>
                         136: <POP>
                         137: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         140: <LDC <String 'print'>>
                         142: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         145: <DUP>
                         146: <IFNONNULL 27>
                         149: <POP>
                         150: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         153: <LDC <String 'print'>>
                         155: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         158: <DUP>
                         159: <IFNONNULL 14>
                         162: <POP>
                         163: <NEW org/python/exceptions/NameError>
                         166: <DUP>
                         167: <LDC <String 'print'>>
                         169: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         172: <ATHROW>
                         173: <CHECKCAST <Class org/python/Object>>
                         176: <CHECKCAST <Class org/python/Callable>>
                         179: <ICONST_1>
                         180: <ANEWARRAY org/python/Object>
                         183: <DUP>
                         184: <ICONST_0>
                         185: <NEW org/python/Object>
                         188: <DUP>
                         189: <LDC <String 'Got a NameError'>>
                         191: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         194: <AASTORE>
                         195: <NEW java/util/Hashtable>
                         198: <DUP>
                         199: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         202: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         207: <POP>
                         208: <ACONST_NULL>
                         209: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-45 [48]
                         org/python/exceptions/NameError: 0-45 [136]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 58: 5
                                 137: 7
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
                 Code (345 bytes)
                     Max stack: 9
                     Max locals: 1
                     Bytecode: (285 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GOTO 238>
                          48: <ASTORE_0>
                          49: <NEW org/python/Object>
                          52: <DUP>
                          53: <ALOAD_0>
                          54: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                          57: <ASTORE_0>
                          58: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 27>
                          70: <POP>
                          71: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          74: <LDC <String 'print'>>
                          76: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          79: <DUP>
                          80: <IFNONNULL 14>
                          83: <POP>
                          84: <NEW org/python/exceptions/NameError>
                          87: <DUP>
                          88: <LDC <String 'print'>>
                          90: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          93: <ATHROW>
                          94: <CHECKCAST <Class org/python/Object>>
                          97: <CHECKCAST <Class org/python/Callable>>
                         100: <ICONST_2>
                         101: <ANEWARRAY org/python/Object>
                         104: <DUP>
                         105: <ICONST_0>
                         106: <NEW org/python/Object>
                         109: <DUP>
                         110: <LDC <String 'Got an AttributeError'>>
                         112: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         115: <AASTORE>
                         116: <DUP>
                         117: <ICONST_1>
                         118: <ALOAD_0>
                         119: <AASTORE>
                         120: <NEW java/util/Hashtable>
                         123: <DUP>
                         124: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         127: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         132: <POP>
                         133: <GOTO 150>
                         136: <POP>
                         137: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         140: <LDC <String 'print'>>
                         142: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         145: <DUP>
                         146: <IFNONNULL 27>
                         149: <POP>
                         150: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         153: <LDC <String 'print'>>
                         155: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         158: <DUP>
                         159: <IFNONNULL 14>
                         162: <POP>
                         163: <NEW org/python/exceptions/NameError>
                         166: <DUP>
                         167: <LDC <String 'print'>>
                         169: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         172: <ATHROW>
                         173: <CHECKCAST <Class org/python/Object>>
                         176: <CHECKCAST <Class org/python/Callable>>
                         179: <ICONST_1>
                         180: <ANEWARRAY org/python/Object>
                         183: <DUP>
                         184: <ICONST_0>
                         185: <NEW org/python/Object>
                         188: <DUP>
                         189: <LDC <String 'Got a NameError'>>
                         191: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         194: <AASTORE>
                         195: <NEW java/util/Hashtable>
                         198: <DUP>
                         199: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         202: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         207: <POP>
                         208: <GOTO 75>
                         211: <POP>
                         212: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         215: <LDC <String 'print'>>
                         217: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         220: <DUP>
                         221: <IFNONNULL 27>
                         224: <POP>
                         225: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         228: <LDC <String 'print'>>
                         230: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         233: <DUP>
                         234: <IFNONNULL 14>
                         237: <POP>
                         238: <NEW org/python/exceptions/NameError>
                         241: <DUP>
                         242: <LDC <String 'print'>>
                         244: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         247: <ATHROW>
                         248: <CHECKCAST <Class org/python/Object>>
                         251: <CHECKCAST <Class org/python/Callable>>
                         254: <ICONST_1>
                         255: <ANEWARRAY org/python/Object>
                         258: <DUP>
                         259: <ICONST_0>
                         260: <NEW org/python/Object>
                         263: <DUP>
                         264: <LDC <String 'Got an anonymous error'>>
                         266: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         269: <AASTORE>
                         270: <NEW java/util/Hashtable>
                         273: <DUP>
                         274: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         277: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         282: <POP>
                         283: <ACONST_NULL>
                         284: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-45 [48]
                         org/python/exceptions/NameError: 0-45 [136]
                         org/python/exceptions/BaseException: 0-45 [211]
                     Attributes: (1)
                         LineNumberTable (18 bytes)
                             Line numbers (4 total):
                                 0: 3
                                 58: 5
                                 137: 7
                                 212: 9
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
                           0: <NEW org/python/Object>
                           3: <DUP>
                           4: <ICONST_3>
                           5: <INVOKESPECIAL org/python/Object.<init> (I)V>
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
                          45: <CHECKCAST <Class org/python/Object>>
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
                         120: <CHECKCAST <Class org/python/Object>>
                         123: <CHECKCAST <Class org/python/Callable>>
                         126: <ICONST_1>
                         127: <ANEWARRAY org/python/Object>
                         130: <DUP>
                         131: <ICONST_0>
                         132: <NEW org/python/Object>
                         135: <DUP>
                         136: <LDC <String 'Do final cleanup'>>
                         138: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
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
                 Code (405 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (341 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          48: <LDC <String 'print'>>
                          50: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          53: <DUP>
                          54: <IFNONNULL 27>
                          57: <POP>
                          58: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 14>
                          70: <POP>
                          71: <NEW org/python/exceptions/NameError>
                          74: <DUP>
                          75: <LDC <String 'print'>>
                          77: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          80: <ATHROW>
                          81: <CHECKCAST <Class org/python/Object>>
                          84: <CHECKCAST <Class org/python/Callable>>
                          87: <ICONST_1>
                          88: <ANEWARRAY org/python/Object>
                          91: <DUP>
                          92: <ICONST_0>
                          93: <NEW org/python/Object>
                          96: <DUP>
                          97: <LDC <String 'Do final cleanup'>>
                          99: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         102: <AASTORE>
                         103: <NEW java/util/Hashtable>
                         106: <DUP>
                         107: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         110: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         115: <POP>
                         116: <GOTO 223>
                         119: <POP>
                         120: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         123: <LDC <String 'print'>>
                         125: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         128: <DUP>
                         129: <IFNONNULL 27>
                         132: <POP>
                         133: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         136: <LDC <String 'print'>>
                         138: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         141: <DUP>
                         142: <IFNONNULL 14>
                         145: <POP>
                         146: <NEW org/python/exceptions/NameError>
                         149: <DUP>
                         150: <LDC <String 'print'>>
                         152: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         155: <ATHROW>
                         156: <CHECKCAST <Class org/python/Object>>
                         159: <CHECKCAST <Class org/python/Callable>>
                         162: <ICONST_1>
                         163: <ANEWARRAY org/python/Object>
                         166: <DUP>
                         167: <ICONST_0>
                         168: <NEW org/python/Object>
                         171: <DUP>
                         172: <LDC <String 'Got an error'>>
                         174: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         177: <AASTORE>
                         178: <NEW java/util/Hashtable>
                         181: <DUP>
                         182: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         185: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         190: <POP>
                         191: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         194: <LDC <String 'print'>>
                         196: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         199: <DUP>
                         200: <IFNONNULL 27>
                         203: <POP>
                         204: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         207: <LDC <String 'print'>>
                         209: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         212: <DUP>
                         213: <IFNONNULL 14>
                         216: <POP>
                         217: <NEW org/python/exceptions/NameError>
                         220: <DUP>
                         221: <LDC <String 'print'>>
                         223: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         226: <ATHROW>
                         227: <CHECKCAST <Class org/python/Object>>
                         230: <CHECKCAST <Class org/python/Callable>>
                         233: <ICONST_1>
                         234: <ANEWARRAY org/python/Object>
                         237: <DUP>
                         238: <ICONST_0>
                         239: <NEW org/python/Object>
                         242: <DUP>
                         243: <LDC <String 'Do final cleanup'>>
                         245: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         248: <AASTORE>
                         249: <NEW java/util/Hashtable>
                         252: <DUP>
                         253: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         256: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         261: <POP>
                         262: <GOTO 77>
                         265: <ASTORE_0>
                         266: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         269: <LDC <String 'print'>>
                         271: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         274: <DUP>
                         275: <IFNONNULL 27>
                         278: <POP>
                         279: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         282: <LDC <String 'print'>>
                         284: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         287: <DUP>
                         288: <IFNONNULL 14>
                         291: <POP>
                         292: <NEW org/python/exceptions/NameError>
                         295: <DUP>
                         296: <LDC <String 'print'>>
                         298: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         301: <ATHROW>
                         302: <CHECKCAST <Class org/python/Object>>
                         305: <CHECKCAST <Class org/python/Callable>>
                         308: <ICONST_1>
                         309: <ANEWARRAY org/python/Object>
                         312: <DUP>
                         313: <ICONST_0>
                         314: <NEW org/python/Object>
                         317: <DUP>
                         318: <LDC <String 'Do final cleanup'>>
                         320: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         323: <AASTORE>
                         324: <NEW java/util/Hashtable>
                         327: <DUP>
                         328: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         331: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         336: <POP>
                         337: <ALOAD_0>
                         338: <ATHROW>
                         339: <ACONST_NULL>
                         340: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/BaseException: 0-45 [119]
                         finally: 0-45 [265]
                         finally: 119-191 [265]
                     Attributes: (1)
                         LineNumberTable (22 bytes)
                             Line numbers (5 total):
                                 0: 3
                                 45: 7
                                 120: 5
                                 191: 7
                                 266: 7
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
                 Code (405 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (341 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          48: <LDC <String 'print'>>
                          50: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          53: <DUP>
                          54: <IFNONNULL 27>
                          57: <POP>
                          58: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 14>
                          70: <POP>
                          71: <NEW org/python/exceptions/NameError>
                          74: <DUP>
                          75: <LDC <String 'print'>>
                          77: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          80: <ATHROW>
                          81: <CHECKCAST <Class org/python/Object>>
                          84: <CHECKCAST <Class org/python/Callable>>
                          87: <ICONST_1>
                          88: <ANEWARRAY org/python/Object>
                          91: <DUP>
                          92: <ICONST_0>
                          93: <NEW org/python/Object>
                          96: <DUP>
                          97: <LDC <String 'Do final cleanup'>>
                          99: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         102: <AASTORE>
                         103: <NEW java/util/Hashtable>
                         106: <DUP>
                         107: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         110: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         115: <POP>
                         116: <GOTO 223>
                         119: <POP>
                         120: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         123: <LDC <String 'print'>>
                         125: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         128: <DUP>
                         129: <IFNONNULL 27>
                         132: <POP>
                         133: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         136: <LDC <String 'print'>>
                         138: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         141: <DUP>
                         142: <IFNONNULL 14>
                         145: <POP>
                         146: <NEW org/python/exceptions/NameError>
                         149: <DUP>
                         150: <LDC <String 'print'>>
                         152: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         155: <ATHROW>
                         156: <CHECKCAST <Class org/python/Object>>
                         159: <CHECKCAST <Class org/python/Callable>>
                         162: <ICONST_1>
                         163: <ANEWARRAY org/python/Object>
                         166: <DUP>
                         167: <ICONST_0>
                         168: <NEW org/python/Object>
                         171: <DUP>
                         172: <LDC <String 'Got an error'>>
                         174: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         177: <AASTORE>
                         178: <NEW java/util/Hashtable>
                         181: <DUP>
                         182: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         185: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         190: <POP>
                         191: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         194: <LDC <String 'print'>>
                         196: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         199: <DUP>
                         200: <IFNONNULL 27>
                         203: <POP>
                         204: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         207: <LDC <String 'print'>>
                         209: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         212: <DUP>
                         213: <IFNONNULL 14>
                         216: <POP>
                         217: <NEW org/python/exceptions/NameError>
                         220: <DUP>
                         221: <LDC <String 'print'>>
                         223: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         226: <ATHROW>
                         227: <CHECKCAST <Class org/python/Object>>
                         230: <CHECKCAST <Class org/python/Callable>>
                         233: <ICONST_1>
                         234: <ANEWARRAY org/python/Object>
                         237: <DUP>
                         238: <ICONST_0>
                         239: <NEW org/python/Object>
                         242: <DUP>
                         243: <LDC <String 'Do final cleanup'>>
                         245: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         248: <AASTORE>
                         249: <NEW java/util/Hashtable>
                         252: <DUP>
                         253: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         256: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         261: <POP>
                         262: <GOTO 77>
                         265: <ASTORE_0>
                         266: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         269: <LDC <String 'print'>>
                         271: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         274: <DUP>
                         275: <IFNONNULL 27>
                         278: <POP>
                         279: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         282: <LDC <String 'print'>>
                         284: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         287: <DUP>
                         288: <IFNONNULL 14>
                         291: <POP>
                         292: <NEW org/python/exceptions/NameError>
                         295: <DUP>
                         296: <LDC <String 'print'>>
                         298: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         301: <ATHROW>
                         302: <CHECKCAST <Class org/python/Object>>
                         305: <CHECKCAST <Class org/python/Callable>>
                         308: <ICONST_1>
                         309: <ANEWARRAY org/python/Object>
                         312: <DUP>
                         313: <ICONST_0>
                         314: <NEW org/python/Object>
                         317: <DUP>
                         318: <LDC <String 'Do final cleanup'>>
                         320: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         323: <AASTORE>
                         324: <NEW java/util/Hashtable>
                         327: <DUP>
                         328: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         331: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         336: <POP>
                         337: <ALOAD_0>
                         338: <ATHROW>
                         339: <ACONST_NULL>
                         340: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-45 [119]
                         finally: 0-45 [265]
                         finally: 119-191 [265]
                     Attributes: (1)
                         LineNumberTable (22 bytes)
                             Line numbers (5 total):
                                 0: 3
                                 45: 7
                                 120: 5
                                 191: 7
                                 266: 7
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
                 Code (418 bytes)
                     Max stack: 10
                     Max locals: 2
                     Bytecode: (354 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          48: <LDC <String 'print'>>
                          50: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          53: <DUP>
                          54: <IFNONNULL 27>
                          57: <POP>
                          58: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 14>
                          70: <POP>
                          71: <NEW org/python/exceptions/NameError>
                          74: <DUP>
                          75: <LDC <String 'print'>>
                          77: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          80: <ATHROW>
                          81: <CHECKCAST <Class org/python/Object>>
                          84: <CHECKCAST <Class org/python/Callable>>
                          87: <ICONST_1>
                          88: <ANEWARRAY org/python/Object>
                          91: <DUP>
                          92: <ICONST_0>
                          93: <NEW org/python/Object>
                          96: <DUP>
                          97: <LDC <String 'Do final cleanup'>>
                          99: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         102: <AASTORE>
                         103: <NEW java/util/Hashtable>
                         106: <DUP>
                         107: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         110: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         115: <POP>
                         116: <GOTO 236>
                         119: <ASTORE_0>
                         120: <NEW org/python/Object>
                         123: <DUP>
                         124: <ALOAD_0>
                         125: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                         128: <ASTORE_0>
                         129: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         132: <LDC <String 'print'>>
                         134: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         137: <DUP>
                         138: <IFNONNULL 27>
                         141: <POP>
                         142: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         145: <LDC <String 'print'>>
                         147: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         150: <DUP>
                         151: <IFNONNULL 14>
                         154: <POP>
                         155: <NEW org/python/exceptions/NameError>
                         158: <DUP>
                         159: <LDC <String 'print'>>
                         161: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         164: <ATHROW>
                         165: <CHECKCAST <Class org/python/Object>>
                         168: <CHECKCAST <Class org/python/Callable>>
                         171: <ICONST_2>
                         172: <ANEWARRAY org/python/Object>
                         175: <DUP>
                         176: <ICONST_0>
                         177: <NEW org/python/Object>
                         180: <DUP>
                         181: <LDC <String 'Got an AttributeError'>>
                         183: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         186: <AASTORE>
                         187: <DUP>
                         188: <ICONST_1>
                         189: <ALOAD_0>
                         190: <AASTORE>
                         191: <NEW java/util/Hashtable>
                         194: <DUP>
                         195: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         198: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         203: <POP>
                         204: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         207: <LDC <String 'print'>>
                         209: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         212: <DUP>
                         213: <IFNONNULL 27>
                         216: <POP>
                         217: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         220: <LDC <String 'print'>>
                         222: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         225: <DUP>
                         226: <IFNONNULL 14>
                         229: <POP>
                         230: <NEW org/python/exceptions/NameError>
                         233: <DUP>
                         234: <LDC <String 'print'>>
                         236: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         239: <ATHROW>
                         240: <CHECKCAST <Class org/python/Object>>
                         243: <CHECKCAST <Class org/python/Callable>>
                         246: <ICONST_1>
                         247: <ANEWARRAY org/python/Object>
                         250: <DUP>
                         251: <ICONST_0>
                         252: <NEW org/python/Object>
                         255: <DUP>
                         256: <LDC <String 'Do final cleanup'>>
                         258: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         261: <AASTORE>
                         262: <NEW java/util/Hashtable>
                         265: <DUP>
                         266: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         269: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         274: <POP>
                         275: <GOTO 77>
                         278: <ASTORE_1>
                         279: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         282: <LDC <String 'print'>>
                         284: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         287: <DUP>
                         288: <IFNONNULL 27>
                         291: <POP>
                         292: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         295: <LDC <String 'print'>>
                         297: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         300: <DUP>
                         301: <IFNONNULL 14>
                         304: <POP>
                         305: <NEW org/python/exceptions/NameError>
                         308: <DUP>
                         309: <LDC <String 'print'>>
                         311: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         314: <ATHROW>
                         315: <CHECKCAST <Class org/python/Object>>
                         318: <CHECKCAST <Class org/python/Callable>>
                         321: <ICONST_1>
                         322: <ANEWARRAY org/python/Object>
                         325: <DUP>
                         326: <ICONST_0>
                         327: <NEW org/python/Object>
                         330: <DUP>
                         331: <LDC <String 'Do final cleanup'>>
                         333: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         336: <AASTORE>
                         337: <NEW java/util/Hashtable>
                         340: <DUP>
                         341: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         344: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         349: <POP>
                         350: <ALOAD_1>
                         351: <ATHROW>
                         352: <ACONST_NULL>
                         353: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-45 [119]
                         finally: 0-45 [278]
                         finally: 119-204 [278]
                     Attributes: (1)
                         LineNumberTable (22 bytes)
                             Line numbers (5 total):
                                 0: 3
                                 45: 7
                                 129: 5
                                 204: 7
                                 279: 7
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
                 Code (588 bytes)
                     Max stack: 12
                     Max locals: 2
                     Bytecode: (500 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          48: <LDC <String 'print'>>
                          50: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          53: <DUP>
                          54: <IFNONNULL 27>
                          57: <POP>
                          58: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 14>
                          70: <POP>
                          71: <NEW org/python/exceptions/NameError>
                          74: <DUP>
                          75: <LDC <String 'print'>>
                          77: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          80: <ATHROW>
                          81: <CHECKCAST <Class org/python/Object>>
                          84: <CHECKCAST <Class org/python/Callable>>
                          87: <ICONST_1>
                          88: <ANEWARRAY org/python/Object>
                          91: <DUP>
                          92: <ICONST_0>
                          93: <NEW org/python/Object>
                          96: <DUP>
                          97: <LDC <String 'Do final cleanup'>>
                          99: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         102: <AASTORE>
                         103: <NEW java/util/Hashtable>
                         106: <DUP>
                         107: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         110: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         115: <POP>
                         116: <GOTO 382>
                         119: <POP>
                         120: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         123: <LDC <String 'print'>>
                         125: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         128: <DUP>
                         129: <IFNONNULL 27>
                         132: <POP>
                         133: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         136: <LDC <String 'print'>>
                         138: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         141: <DUP>
                         142: <IFNONNULL 14>
                         145: <POP>
                         146: <NEW org/python/exceptions/NameError>
                         149: <DUP>
                         150: <LDC <String 'print'>>
                         152: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         155: <ATHROW>
                         156: <CHECKCAST <Class org/python/Object>>
                         159: <CHECKCAST <Class org/python/Callable>>
                         162: <ICONST_1>
                         163: <ANEWARRAY org/python/Object>
                         166: <DUP>
                         167: <ICONST_0>
                         168: <NEW org/python/Object>
                         171: <DUP>
                         172: <LDC <String 'Got an AttributeError'>>
                         174: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         177: <AASTORE>
                         178: <NEW java/util/Hashtable>
                         181: <DUP>
                         182: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         185: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         190: <POP>
                         191: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         194: <LDC <String 'print'>>
                         196: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         199: <DUP>
                         200: <IFNONNULL 27>
                         203: <POP>
                         204: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         207: <LDC <String 'print'>>
                         209: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         212: <DUP>
                         213: <IFNONNULL 14>
                         216: <POP>
                         217: <NEW org/python/exceptions/NameError>
                         220: <DUP>
                         221: <LDC <String 'print'>>
                         223: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         226: <ATHROW>
                         227: <CHECKCAST <Class org/python/Object>>
                         230: <CHECKCAST <Class org/python/Callable>>
                         233: <ICONST_1>
                         234: <ANEWARRAY org/python/Object>
                         237: <DUP>
                         238: <ICONST_0>
                         239: <NEW org/python/Object>
                         242: <DUP>
                         243: <LDC <String 'Do final cleanup'>>
                         245: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         248: <AASTORE>
                         249: <NEW java/util/Hashtable>
                         252: <DUP>
                         253: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         256: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         261: <POP>
                         262: <GOTO 236>
                         265: <ASTORE_0>
                         266: <NEW org/python/Object>
                         269: <DUP>
                         270: <ALOAD_0>
                         271: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                         274: <ASTORE_0>
                         275: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         278: <LDC <String 'print'>>
                         280: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         283: <DUP>
                         284: <IFNONNULL 27>
                         287: <POP>
                         288: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         291: <LDC <String 'print'>>
                         293: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         296: <DUP>
                         297: <IFNONNULL 14>
                         300: <POP>
                         301: <NEW org/python/exceptions/NameError>
                         304: <DUP>
                         305: <LDC <String 'print'>>
                         307: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         310: <ATHROW>
                         311: <CHECKCAST <Class org/python/Object>>
                         314: <CHECKCAST <Class org/python/Callable>>
                         317: <ICONST_2>
                         318: <ANEWARRAY org/python/Object>
                         321: <DUP>
                         322: <ICONST_0>
                         323: <NEW org/python/Object>
                         326: <DUP>
                         327: <LDC <String 'Got a NameError'>>
                         329: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         332: <AASTORE>
                         333: <DUP>
                         334: <ICONST_1>
                         335: <ALOAD_0>
                         336: <AASTORE>
                         337: <NEW java/util/Hashtable>
                         340: <DUP>
                         341: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         344: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         349: <POP>
                         350: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         353: <LDC <String 'print'>>
                         355: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         358: <DUP>
                         359: <IFNONNULL 27>
                         362: <POP>
                         363: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         366: <LDC <String 'print'>>
                         368: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         371: <DUP>
                         372: <IFNONNULL 14>
                         375: <POP>
                         376: <NEW org/python/exceptions/NameError>
                         379: <DUP>
                         380: <LDC <String 'print'>>
                         382: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         385: <ATHROW>
                         386: <CHECKCAST <Class org/python/Object>>
                         389: <CHECKCAST <Class org/python/Callable>>
                         392: <ICONST_1>
                         393: <ANEWARRAY org/python/Object>
                         396: <DUP>
                         397: <ICONST_0>
                         398: <NEW org/python/Object>
                         401: <DUP>
                         402: <LDC <String 'Do final cleanup'>>
                         404: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         407: <AASTORE>
                         408: <NEW java/util/Hashtable>
                         411: <DUP>
                         412: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         415: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         420: <POP>
                         421: <GOTO 77>
                         424: <ASTORE_1>
                         425: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         428: <LDC <String 'print'>>
                         430: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         433: <DUP>
                         434: <IFNONNULL 27>
                         437: <POP>
                         438: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         441: <LDC <String 'print'>>
                         443: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         446: <DUP>
                         447: <IFNONNULL 14>
                         450: <POP>
                         451: <NEW org/python/exceptions/NameError>
                         454: <DUP>
                         455: <LDC <String 'print'>>
                         457: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         460: <ATHROW>
                         461: <CHECKCAST <Class org/python/Object>>
                         464: <CHECKCAST <Class org/python/Callable>>
                         467: <ICONST_1>
                         468: <ANEWARRAY org/python/Object>
                         471: <DUP>
                         472: <ICONST_0>
                         473: <NEW org/python/Object>
                         476: <DUP>
                         477: <LDC <String 'Do final cleanup'>>
                         479: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         482: <AASTORE>
                         483: <NEW java/util/Hashtable>
                         486: <DUP>
                         487: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         490: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         495: <POP>
                         496: <ALOAD_1>
                         497: <ATHROW>
                         498: <ACONST_NULL>
                         499: <ARETURN>
                     Exceptions: (5)
                         org/python/exceptions/AttributeError: 0-45 [119]
                         org/python/exceptions/NameError: 0-45 [265]
                         finally: 0-45 [424]
                         finally: 119-191 [424]
                         finally: 265-350 [424]
                     Attributes: (1)
                         LineNumberTable (30 bytes)
                             Line numbers (7 total):
                                 0: 3
                                 45: 9
                                 120: 5
                                 191: 9
                                 275: 7
                                 350: 9
                                 425: 9
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
                 Code (233 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (193 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          48: <LDC <String 'print'>>
                          50: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          53: <DUP>
                          54: <IFNONNULL 27>
                          57: <POP>
                          58: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 14>
                          70: <POP>
                          71: <NEW org/python/exceptions/NameError>
                          74: <DUP>
                          75: <LDC <String 'print'>>
                          77: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          80: <ATHROW>
                          81: <CHECKCAST <Class org/python/Object>>
                          84: <CHECKCAST <Class org/python/Callable>>
                          87: <ICONST_1>
                          88: <ANEWARRAY org/python/Object>
                          91: <DUP>
                          92: <ICONST_0>
                          93: <NEW org/python/Object>
                          96: <DUP>
                          97: <LDC <String 'Do else handling'>>
                          99: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         102: <AASTORE>
                         103: <NEW java/util/Hashtable>
                         106: <DUP>
                         107: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         110: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         115: <POP>
                         116: <GOTO 75>
                         119: <POP>
                         120: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         123: <LDC <String 'print'>>
                         125: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         128: <DUP>
                         129: <IFNONNULL 27>
                         132: <POP>
                         133: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         136: <LDC <String 'print'>>
                         138: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         141: <DUP>
                         142: <IFNONNULL 14>
                         145: <POP>
                         146: <NEW org/python/exceptions/NameError>
                         149: <DUP>
                         150: <LDC <String 'print'>>
                         152: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         155: <ATHROW>
                         156: <CHECKCAST <Class org/python/Object>>
                         159: <CHECKCAST <Class org/python/Callable>>
                         162: <ICONST_1>
                         163: <ANEWARRAY org/python/Object>
                         166: <DUP>
                         167: <ICONST_0>
                         168: <NEW org/python/Object>
                         171: <DUP>
                         172: <LDC <String 'Got an error'>>
                         174: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         177: <AASTORE>
                         178: <NEW java/util/Hashtable>
                         181: <DUP>
                         182: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         185: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         190: <POP>
                         191: <ACONST_NULL>
                         192: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/BaseException: 0-45 [119]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 45: 7
                                 120: 5
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
                 Code (233 bytes)
                     Max stack: 8
                     Max locals: 0
                     Bytecode: (193 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          48: <LDC <String 'print'>>
                          50: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          53: <DUP>
                          54: <IFNONNULL 27>
                          57: <POP>
                          58: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 14>
                          70: <POP>
                          71: <NEW org/python/exceptions/NameError>
                          74: <DUP>
                          75: <LDC <String 'print'>>
                          77: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          80: <ATHROW>
                          81: <CHECKCAST <Class org/python/Object>>
                          84: <CHECKCAST <Class org/python/Callable>>
                          87: <ICONST_1>
                          88: <ANEWARRAY org/python/Object>
                          91: <DUP>
                          92: <ICONST_0>
                          93: <NEW org/python/Object>
                          96: <DUP>
                          97: <LDC <String 'Do else handling'>>
                          99: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         102: <AASTORE>
                         103: <NEW java/util/Hashtable>
                         106: <DUP>
                         107: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         110: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         115: <POP>
                         116: <GOTO 75>
                         119: <POP>
                         120: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         123: <LDC <String 'print'>>
                         125: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         128: <DUP>
                         129: <IFNONNULL 27>
                         132: <POP>
                         133: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         136: <LDC <String 'print'>>
                         138: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         141: <DUP>
                         142: <IFNONNULL 14>
                         145: <POP>
                         146: <NEW org/python/exceptions/NameError>
                         149: <DUP>
                         150: <LDC <String 'print'>>
                         152: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         155: <ATHROW>
                         156: <CHECKCAST <Class org/python/Object>>
                         159: <CHECKCAST <Class org/python/Callable>>
                         162: <ICONST_1>
                         163: <ANEWARRAY org/python/Object>
                         166: <DUP>
                         167: <ICONST_0>
                         168: <NEW org/python/Object>
                         171: <DUP>
                         172: <LDC <String 'Got an error'>>
                         174: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         177: <AASTORE>
                         178: <NEW java/util/Hashtable>
                         181: <DUP>
                         182: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         185: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         190: <POP>
                         191: <ACONST_NULL>
                         192: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/AttributeError: 0-45 [119]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 3
                                 45: 7
                                 120: 5
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
                 Code (333 bytes)
                     Max stack: 9
                     Max locals: 1
                     Bytecode: (281 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          48: <LDC <String 'print'>>
                          50: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          53: <DUP>
                          54: <IFNONNULL 27>
                          57: <POP>
                          58: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 14>
                          70: <POP>
                          71: <NEW org/python/exceptions/NameError>
                          74: <DUP>
                          75: <LDC <String 'print'>>
                          77: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          80: <ATHROW>
                          81: <CHECKCAST <Class org/python/Object>>
                          84: <CHECKCAST <Class org/python/Callable>>
                          87: <ICONST_1>
                          88: <ANEWARRAY org/python/Object>
                          91: <DUP>
                          92: <ICONST_0>
                          93: <NEW org/python/Object>
                          96: <DUP>
                          97: <LDC <String 'Do else handling'>>
                          99: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         102: <AASTORE>
                         103: <NEW java/util/Hashtable>
                         106: <DUP>
                         107: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         110: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         115: <POP>
                         116: <GOTO 163>
                         119: <POP>
                         120: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         123: <LDC <String 'print'>>
                         125: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         128: <DUP>
                         129: <IFNONNULL 27>
                         132: <POP>
                         133: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         136: <LDC <String 'print'>>
                         138: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         141: <DUP>
                         142: <IFNONNULL 14>
                         145: <POP>
                         146: <NEW org/python/exceptions/NameError>
                         149: <DUP>
                         150: <LDC <String 'print'>>
                         152: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         155: <ATHROW>
                         156: <CHECKCAST <Class org/python/Object>>
                         159: <CHECKCAST <Class org/python/Callable>>
                         162: <ICONST_1>
                         163: <ANEWARRAY org/python/Object>
                         166: <DUP>
                         167: <ICONST_0>
                         168: <NEW org/python/Object>
                         171: <DUP>
                         172: <LDC <String 'Got an AttributeError'>>
                         174: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         177: <AASTORE>
                         178: <NEW java/util/Hashtable>
                         181: <DUP>
                         182: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         185: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         190: <POP>
                         191: <GOTO 88>
                         194: <ASTORE_0>
                         195: <NEW org/python/Object>
                         198: <DUP>
                         199: <ALOAD_0>
                         200: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                         203: <ASTORE_0>
                         204: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         207: <LDC <String 'print'>>
                         209: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         212: <DUP>
                         213: <IFNONNULL 27>
                         216: <POP>
                         217: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         220: <LDC <String 'print'>>
                         222: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         225: <DUP>
                         226: <IFNONNULL 14>
                         229: <POP>
                         230: <NEW org/python/exceptions/NameError>
                         233: <DUP>
                         234: <LDC <String 'print'>>
                         236: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         239: <ATHROW>
                         240: <CHECKCAST <Class org/python/Object>>
                         243: <CHECKCAST <Class org/python/Callable>>
                         246: <ICONST_2>
                         247: <ANEWARRAY org/python/Object>
                         250: <DUP>
                         251: <ICONST_0>
                         252: <NEW org/python/Object>
                         255: <DUP>
                         256: <LDC <String 'Got a NameError'>>
                         258: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         261: <AASTORE>
                         262: <DUP>
                         263: <ICONST_1>
                         264: <ALOAD_0>
                         265: <AASTORE>
                         266: <NEW java/util/Hashtable>
                         269: <DUP>
                         270: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         273: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         278: <POP>
                         279: <ACONST_NULL>
                         280: <ARETURN>
                     Exceptions: (2)
                         org/python/exceptions/AttributeError: 0-45 [119]
                         org/python/exceptions/NameError: 0-45 [194]
                     Attributes: (1)
                         LineNumberTable (18 bytes)
                             Line numbers (4 total):
                                 0: 3
                                 45: 9
                                 120: 5
                                 204: 7
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
                 Code (480 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (412 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          48: <LDC <String 'print'>>
                          50: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          53: <DUP>
                          54: <IFNONNULL 27>
                          57: <POP>
                          58: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 14>
                          70: <POP>
                          71: <NEW org/python/exceptions/NameError>
                          74: <DUP>
                          75: <LDC <String 'print'>>
                          77: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          80: <ATHROW>
                          81: <CHECKCAST <Class org/python/Object>>
                          84: <CHECKCAST <Class org/python/Callable>>
                          87: <ICONST_1>
                          88: <ANEWARRAY org/python/Object>
                          91: <DUP>
                          92: <ICONST_0>
                          93: <NEW org/python/Object>
                          96: <DUP>
                          97: <LDC <String 'Do else handling'>>
                          99: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         102: <AASTORE>
                         103: <NEW java/util/Hashtable>
                         106: <DUP>
                         107: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         110: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         115: <POP>
                         116: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         119: <LDC <String 'print'>>
                         121: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         124: <DUP>
                         125: <IFNONNULL 27>
                         128: <POP>
                         129: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         132: <LDC <String 'print'>>
                         134: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         137: <DUP>
                         138: <IFNONNULL 14>
                         141: <POP>
                         142: <NEW org/python/exceptions/NameError>
                         145: <DUP>
                         146: <LDC <String 'print'>>
                         148: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         151: <ATHROW>
                         152: <CHECKCAST <Class org/python/Object>>
                         155: <CHECKCAST <Class org/python/Callable>>
                         158: <ICONST_1>
                         159: <ANEWARRAY org/python/Object>
                         162: <DUP>
                         163: <ICONST_0>
                         164: <NEW org/python/Object>
                         167: <DUP>
                         168: <LDC <String 'Do final cleanup'>>
                         170: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         173: <AASTORE>
                         174: <NEW java/util/Hashtable>
                         177: <DUP>
                         178: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         181: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         186: <POP>
                         187: <GOTO 223>
                         190: <POP>
                         191: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         194: <LDC <String 'print'>>
                         196: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         199: <DUP>
                         200: <IFNONNULL 27>
                         203: <POP>
                         204: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         207: <LDC <String 'print'>>
                         209: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         212: <DUP>
                         213: <IFNONNULL 14>
                         216: <POP>
                         217: <NEW org/python/exceptions/NameError>
                         220: <DUP>
                         221: <LDC <String 'print'>>
                         223: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         226: <ATHROW>
                         227: <CHECKCAST <Class org/python/Object>>
                         230: <CHECKCAST <Class org/python/Callable>>
                         233: <ICONST_1>
                         234: <ANEWARRAY org/python/Object>
                         237: <DUP>
                         238: <ICONST_0>
                         239: <NEW org/python/Object>
                         242: <DUP>
                         243: <LDC <String 'Got an error'>>
                         245: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         248: <AASTORE>
                         249: <NEW java/util/Hashtable>
                         252: <DUP>
                         253: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         256: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         261: <POP>
                         262: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         265: <LDC <String 'print'>>
                         267: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         270: <DUP>
                         271: <IFNONNULL 27>
                         274: <POP>
                         275: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         278: <LDC <String 'print'>>
                         280: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         283: <DUP>
                         284: <IFNONNULL 14>
                         287: <POP>
                         288: <NEW org/python/exceptions/NameError>
                         291: <DUP>
                         292: <LDC <String 'print'>>
                         294: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         297: <ATHROW>
                         298: <CHECKCAST <Class org/python/Object>>
                         301: <CHECKCAST <Class org/python/Callable>>
                         304: <ICONST_1>
                         305: <ANEWARRAY org/python/Object>
                         308: <DUP>
                         309: <ICONST_0>
                         310: <NEW org/python/Object>
                         313: <DUP>
                         314: <LDC <String 'Do final cleanup'>>
                         316: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         319: <AASTORE>
                         320: <NEW java/util/Hashtable>
                         323: <DUP>
                         324: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         327: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         332: <POP>
                         333: <GOTO 77>
                         336: <ASTORE_0>
                         337: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         340: <LDC <String 'print'>>
                         342: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         345: <DUP>
                         346: <IFNONNULL 27>
                         349: <POP>
                         350: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         353: <LDC <String 'print'>>
                         355: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         358: <DUP>
                         359: <IFNONNULL 14>
                         362: <POP>
                         363: <NEW org/python/exceptions/NameError>
                         366: <DUP>
                         367: <LDC <String 'print'>>
                         369: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         372: <ATHROW>
                         373: <CHECKCAST <Class org/python/Object>>
                         376: <CHECKCAST <Class org/python/Callable>>
                         379: <ICONST_1>
                         380: <ANEWARRAY org/python/Object>
                         383: <DUP>
                         384: <ICONST_0>
                         385: <NEW org/python/Object>
                         388: <DUP>
                         389: <LDC <String 'Do final cleanup'>>
                         391: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         394: <AASTORE>
                         395: <NEW java/util/Hashtable>
                         398: <DUP>
                         399: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         402: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         407: <POP>
                         408: <ALOAD_0>
                         409: <ATHROW>
                         410: <ACONST_NULL>
                         411: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/BaseException: 0-45 [190]
                         finally: 0-45 [336]
                         finally: 190-262 [336]
                     Attributes: (1)
                         LineNumberTable (26 bytes)
                             Line numbers (6 total):
                                 0: 3
                                 45: 7
                                 116: 9
                                 191: 5
                                 262: 9
                                 337: 9
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
                 Code (480 bytes)
                     Max stack: 10
                     Max locals: 1
                     Bytecode: (412 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          48: <LDC <String 'print'>>
                          50: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          53: <DUP>
                          54: <IFNONNULL 27>
                          57: <POP>
                          58: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 14>
                          70: <POP>
                          71: <NEW org/python/exceptions/NameError>
                          74: <DUP>
                          75: <LDC <String 'print'>>
                          77: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          80: <ATHROW>
                          81: <CHECKCAST <Class org/python/Object>>
                          84: <CHECKCAST <Class org/python/Callable>>
                          87: <ICONST_1>
                          88: <ANEWARRAY org/python/Object>
                          91: <DUP>
                          92: <ICONST_0>
                          93: <NEW org/python/Object>
                          96: <DUP>
                          97: <LDC <String 'Do else handling'>>
                          99: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         102: <AASTORE>
                         103: <NEW java/util/Hashtable>
                         106: <DUP>
                         107: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         110: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         115: <POP>
                         116: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         119: <LDC <String 'print'>>
                         121: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         124: <DUP>
                         125: <IFNONNULL 27>
                         128: <POP>
                         129: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         132: <LDC <String 'print'>>
                         134: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         137: <DUP>
                         138: <IFNONNULL 14>
                         141: <POP>
                         142: <NEW org/python/exceptions/NameError>
                         145: <DUP>
                         146: <LDC <String 'print'>>
                         148: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         151: <ATHROW>
                         152: <CHECKCAST <Class org/python/Object>>
                         155: <CHECKCAST <Class org/python/Callable>>
                         158: <ICONST_1>
                         159: <ANEWARRAY org/python/Object>
                         162: <DUP>
                         163: <ICONST_0>
                         164: <NEW org/python/Object>
                         167: <DUP>
                         168: <LDC <String 'Do final cleanup'>>
                         170: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         173: <AASTORE>
                         174: <NEW java/util/Hashtable>
                         177: <DUP>
                         178: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         181: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         186: <POP>
                         187: <GOTO 223>
                         190: <POP>
                         191: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         194: <LDC <String 'print'>>
                         196: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         199: <DUP>
                         200: <IFNONNULL 27>
                         203: <POP>
                         204: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         207: <LDC <String 'print'>>
                         209: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         212: <DUP>
                         213: <IFNONNULL 14>
                         216: <POP>
                         217: <NEW org/python/exceptions/NameError>
                         220: <DUP>
                         221: <LDC <String 'print'>>
                         223: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         226: <ATHROW>
                         227: <CHECKCAST <Class org/python/Object>>
                         230: <CHECKCAST <Class org/python/Callable>>
                         233: <ICONST_1>
                         234: <ANEWARRAY org/python/Object>
                         237: <DUP>
                         238: <ICONST_0>
                         239: <NEW org/python/Object>
                         242: <DUP>
                         243: <LDC <String 'Got an error'>>
                         245: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         248: <AASTORE>
                         249: <NEW java/util/Hashtable>
                         252: <DUP>
                         253: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         256: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         261: <POP>
                         262: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         265: <LDC <String 'print'>>
                         267: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         270: <DUP>
                         271: <IFNONNULL 27>
                         274: <POP>
                         275: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         278: <LDC <String 'print'>>
                         280: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         283: <DUP>
                         284: <IFNONNULL 14>
                         287: <POP>
                         288: <NEW org/python/exceptions/NameError>
                         291: <DUP>
                         292: <LDC <String 'print'>>
                         294: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         297: <ATHROW>
                         298: <CHECKCAST <Class org/python/Object>>
                         301: <CHECKCAST <Class org/python/Callable>>
                         304: <ICONST_1>
                         305: <ANEWARRAY org/python/Object>
                         308: <DUP>
                         309: <ICONST_0>
                         310: <NEW org/python/Object>
                         313: <DUP>
                         314: <LDC <String 'Do final cleanup'>>
                         316: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         319: <AASTORE>
                         320: <NEW java/util/Hashtable>
                         323: <DUP>
                         324: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         327: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         332: <POP>
                         333: <GOTO 77>
                         336: <ASTORE_0>
                         337: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         340: <LDC <String 'print'>>
                         342: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         345: <DUP>
                         346: <IFNONNULL 27>
                         349: <POP>
                         350: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         353: <LDC <String 'print'>>
                         355: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         358: <DUP>
                         359: <IFNONNULL 14>
                         362: <POP>
                         363: <NEW org/python/exceptions/NameError>
                         366: <DUP>
                         367: <LDC <String 'print'>>
                         369: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         372: <ATHROW>
                         373: <CHECKCAST <Class org/python/Object>>
                         376: <CHECKCAST <Class org/python/Callable>>
                         379: <ICONST_1>
                         380: <ANEWARRAY org/python/Object>
                         383: <DUP>
                         384: <ICONST_0>
                         385: <NEW org/python/Object>
                         388: <DUP>
                         389: <LDC <String 'Do final cleanup'>>
                         391: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         394: <AASTORE>
                         395: <NEW java/util/Hashtable>
                         398: <DUP>
                         399: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         402: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         407: <POP>
                         408: <ALOAD_0>
                         409: <ATHROW>
                         410: <ACONST_NULL>
                         411: <ARETURN>
                     Exceptions: (3)
                         org/python/exceptions/AttributeError: 0-45 [190]
                         finally: 0-45 [336]
                         finally: 190-262 [336]
                     Attributes: (1)
                         LineNumberTable (26 bytes)
                             Line numbers (6 total):
                                 0: 3
                                 45: 7
                                 116: 9
                                 191: 5
                                 262: 9
                                 337: 9
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
                 Code (663 bytes)
                     Max stack: 12
                     Max locals: 2
                     Bytecode: (571 bytes)
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
                          36: <CHECKCAST <Class org/python/Object>>
                          39: <LDC <String 'no_such_attribute'>>
                          41: <INVOKEVIRTUAL org/python/Object.__getattr__ (Ljava/lang/String;)Lorg/python/Object;>
                          44: <POP>
                          45: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          48: <LDC <String 'print'>>
                          50: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          53: <DUP>
                          54: <IFNONNULL 27>
                          57: <POP>
                          58: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          61: <LDC <String 'print'>>
                          63: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          66: <DUP>
                          67: <IFNONNULL 14>
                          70: <POP>
                          71: <NEW org/python/exceptions/NameError>
                          74: <DUP>
                          75: <LDC <String 'print'>>
                          77: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          80: <ATHROW>
                          81: <CHECKCAST <Class org/python/Object>>
                          84: <CHECKCAST <Class org/python/Callable>>
                          87: <ICONST_1>
                          88: <ANEWARRAY org/python/Object>
                          91: <DUP>
                          92: <ICONST_0>
                          93: <NEW org/python/Object>
                          96: <DUP>
                          97: <LDC <String 'Do else handling'>>
                          99: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         102: <AASTORE>
                         103: <NEW java/util/Hashtable>
                         106: <DUP>
                         107: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         110: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         115: <POP>
                         116: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         119: <LDC <String 'print'>>
                         121: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         124: <DUP>
                         125: <IFNONNULL 27>
                         128: <POP>
                         129: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         132: <LDC <String 'print'>>
                         134: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         137: <DUP>
                         138: <IFNONNULL 14>
                         141: <POP>
                         142: <NEW org/python/exceptions/NameError>
                         145: <DUP>
                         146: <LDC <String 'print'>>
                         148: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         151: <ATHROW>
                         152: <CHECKCAST <Class org/python/Object>>
                         155: <CHECKCAST <Class org/python/Callable>>
                         158: <ICONST_1>
                         159: <ANEWARRAY org/python/Object>
                         162: <DUP>
                         163: <ICONST_0>
                         164: <NEW org/python/Object>
                         167: <DUP>
                         168: <LDC <String 'Do final cleanup'>>
                         170: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         173: <AASTORE>
                         174: <NEW java/util/Hashtable>
                         177: <DUP>
                         178: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         181: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         186: <POP>
                         187: <GOTO 382>
                         190: <POP>
                         191: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         194: <LDC <String 'print'>>
                         196: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         199: <DUP>
                         200: <IFNONNULL 27>
                         203: <POP>
                         204: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         207: <LDC <String 'print'>>
                         209: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         212: <DUP>
                         213: <IFNONNULL 14>
                         216: <POP>
                         217: <NEW org/python/exceptions/NameError>
                         220: <DUP>
                         221: <LDC <String 'print'>>
                         223: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         226: <ATHROW>
                         227: <CHECKCAST <Class org/python/Object>>
                         230: <CHECKCAST <Class org/python/Callable>>
                         233: <ICONST_1>
                         234: <ANEWARRAY org/python/Object>
                         237: <DUP>
                         238: <ICONST_0>
                         239: <NEW org/python/Object>
                         242: <DUP>
                         243: <LDC <String 'Got an AttributeError'>>
                         245: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         248: <AASTORE>
                         249: <NEW java/util/Hashtable>
                         252: <DUP>
                         253: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         256: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         261: <POP>
                         262: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         265: <LDC <String 'print'>>
                         267: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         270: <DUP>
                         271: <IFNONNULL 27>
                         274: <POP>
                         275: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         278: <LDC <String 'print'>>
                         280: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         283: <DUP>
                         284: <IFNONNULL 14>
                         287: <POP>
                         288: <NEW org/python/exceptions/NameError>
                         291: <DUP>
                         292: <LDC <String 'print'>>
                         294: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         297: <ATHROW>
                         298: <CHECKCAST <Class org/python/Object>>
                         301: <CHECKCAST <Class org/python/Callable>>
                         304: <ICONST_1>
                         305: <ANEWARRAY org/python/Object>
                         308: <DUP>
                         309: <ICONST_0>
                         310: <NEW org/python/Object>
                         313: <DUP>
                         314: <LDC <String 'Do final cleanup'>>
                         316: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         319: <AASTORE>
                         320: <NEW java/util/Hashtable>
                         323: <DUP>
                         324: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         327: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         332: <POP>
                         333: <GOTO 236>
                         336: <ASTORE_0>
                         337: <NEW org/python/Object>
                         340: <DUP>
                         341: <ALOAD_0>
                         342: <INVOKESPECIAL org/python/Object.<init> (Lorg/python/exceptions/BaseException;)V>
                         345: <ASTORE_0>
                         346: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         349: <LDC <String 'print'>>
                         351: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         354: <DUP>
                         355: <IFNONNULL 27>
                         358: <POP>
                         359: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         362: <LDC <String 'print'>>
                         364: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         367: <DUP>
                         368: <IFNONNULL 14>
                         371: <POP>
                         372: <NEW org/python/exceptions/NameError>
                         375: <DUP>
                         376: <LDC <String 'print'>>
                         378: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         381: <ATHROW>
                         382: <CHECKCAST <Class org/python/Object>>
                         385: <CHECKCAST <Class org/python/Callable>>
                         388: <ICONST_2>
                         389: <ANEWARRAY org/python/Object>
                         392: <DUP>
                         393: <ICONST_0>
                         394: <NEW org/python/Object>
                         397: <DUP>
                         398: <LDC <String 'Got a NameError'>>
                         400: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         403: <AASTORE>
                         404: <DUP>
                         405: <ICONST_1>
                         406: <ALOAD_0>
                         407: <AASTORE>
                         408: <NEW java/util/Hashtable>
                         411: <DUP>
                         412: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         415: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         420: <POP>
                         421: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         424: <LDC <String 'print'>>
                         426: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         429: <DUP>
                         430: <IFNONNULL 27>
                         433: <POP>
                         434: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         437: <LDC <String 'print'>>
                         439: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         442: <DUP>
                         443: <IFNONNULL 14>
                         446: <POP>
                         447: <NEW org/python/exceptions/NameError>
                         450: <DUP>
                         451: <LDC <String 'print'>>
                         453: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         456: <ATHROW>
                         457: <CHECKCAST <Class org/python/Object>>
                         460: <CHECKCAST <Class org/python/Callable>>
                         463: <ICONST_1>
                         464: <ANEWARRAY org/python/Object>
                         467: <DUP>
                         468: <ICONST_0>
                         469: <NEW org/python/Object>
                         472: <DUP>
                         473: <LDC <String 'Do final cleanup'>>
                         475: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         478: <AASTORE>
                         479: <NEW java/util/Hashtable>
                         482: <DUP>
                         483: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         486: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         491: <POP>
                         492: <GOTO 77>
                         495: <ASTORE_1>
                         496: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                         499: <LDC <String 'print'>>
                         501: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         504: <DUP>
                         505: <IFNONNULL 27>
                         508: <POP>
                         509: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                         512: <LDC <String 'print'>>
                         514: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                         517: <DUP>
                         518: <IFNONNULL 14>
                         521: <POP>
                         522: <NEW org/python/exceptions/NameError>
                         525: <DUP>
                         526: <LDC <String 'print'>>
                         528: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                         531: <ATHROW>
                         532: <CHECKCAST <Class org/python/Object>>
                         535: <CHECKCAST <Class org/python/Callable>>
                         538: <ICONST_1>
                         539: <ANEWARRAY org/python/Object>
                         542: <DUP>
                         543: <ICONST_0>
                         544: <NEW org/python/Object>
                         547: <DUP>
                         548: <LDC <String 'Do final cleanup'>>
                         550: <INVOKESPECIAL org/python/Object.<init> (Ljava/lang/String;)V>
                         553: <AASTORE>
                         554: <NEW java/util/Hashtable>
                         557: <DUP>
                         558: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         561: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         566: <POP>
                         567: <ALOAD_1>
                         568: <ATHROW>
                         569: <ACONST_NULL>
                         570: <ARETURN>
                     Exceptions: (5)
                         org/python/exceptions/AttributeError: 0-45 [190]
                         org/python/exceptions/NameError: 0-45 [336]
                         finally: 0-45 [495]
                         finally: 190-262 [495]
                         finally: 336-421 [495]
                     Attributes: (1)
                         LineNumberTable (34 bytes)
                             Line numbers (8 total):
                                 0: 3
                                 45: 9
                                 116: 11
                                 191: 5
                                 262: 11
                                 346: 7
                                 421: 11
                                 496: 11
                """)
