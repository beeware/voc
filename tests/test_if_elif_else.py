from .utils import TranspileTestCase


class IfElifElseTests(TranspileTestCase):
    def test_if(self):
        self.assertBlock(
            python="""
                x = 10
                y = 0
                if x < 5:
                    y = x
                """,
            java="""
                 Code (87 bytes)
                     Max stack: 4
                     Max locals: 2
                     Bytecode: (51 bytes)
                           0: <NEW org/python/types/Object>
                           3: <DUP>
                           4: <SIPUSH 10>
                           7: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          10: <ASTORE_0>
                          11: <NEW org/python/types/Object>
                          14: <DUP>
                          15: <ICONST_0>
                          16: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          19: <ASTORE_1>
                          20: <ALOAD_0>
                          21: <NEW org/python/types/Object>
                          24: <DUP>
                          25: <ICONST_5>
                          26: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          29: <INVOKEVIRTUAL org/python/types/Object.__lt__ (Lorg/python/types/Object;)Lorg/python/types/Object;>
                          32: <GETFIELD org/python/types/Object.value (Ljava/lang/Object;)>
                          35: <CHECKCAST <Class java/lang/Boolean>>
                          38: <INVOKEVIRTUAL java/lang/Boolean.booleanValue ()Z>
                          41: <IFEQ 8>
                          44: <ALOAD_0>
                          45: <ASTORE_1>
                          46: <GOTO 3>
                          49: <ACONST_NULL>
                          50: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (18 bytes)
                             Line numbers (4 total):
                                 0: 2
                                 11: 3
                                 20: 4
                                 44: 5
                """)

    def test_if_else(self):
        self.assertBlock(
            python="""
                x = 10
                if x < 5:
                    y = x
                else:
                    y = -999
                """,
            java="""
                 Code (89 bytes)
                     Max stack: 4
                     Max locals: 2
                     Bytecode: (53 bytes)
                           0: <NEW org/python/types/Object>
                           3: <DUP>
                           4: <SIPUSH 10>
                           7: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          10: <ASTORE_0>
                          11: <ALOAD_0>
                          12: <NEW org/python/types/Object>
                          15: <DUP>
                          16: <ICONST_5>
                          17: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          20: <INVOKEVIRTUAL org/python/types/Object.__lt__ (Lorg/python/types/Object;)Lorg/python/types/Object;>
                          23: <GETFIELD org/python/types/Object.value (Ljava/lang/Object;)>
                          26: <CHECKCAST <Class java/lang/Boolean>>
                          29: <INVOKEVIRTUAL java/lang/Boolean.booleanValue ()Z>
                          32: <IFEQ 8>
                          35: <ALOAD_0>
                          36: <ASTORE_1>
                          37: <GOTO 14>
                          40: <NEW org/python/types/Object>
                          43: <DUP>
                          44: <SIPUSH -999>
                          47: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          50: <ASTORE_1>
                          51: <ACONST_NULL>
                          52: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (18 bytes)
                             Line numbers (4 total):
                                 0: 2
                                 11: 3
                                 35: 4
                                 40: 6
                """)

    def test_if_elif_else(self):
        self.assertBlock(
            python="""
                x = 10
                if x < 5:
                    y = x
                elif x < 50:
                    y = -50
                else:
                    y = -999
                """,
            java="""
                 Code (137 bytes)
                     Max stack: 4
                     Max locals: 2
                     Bytecode: (93 bytes)
                           0: <NEW org/python/types/Object>
                           3: <DUP>
                           4: <SIPUSH 10>
                           7: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          10: <ASTORE_0>
                          11: <ALOAD_0>
                          12: <NEW org/python/types/Object>
                          15: <DUP>
                          16: <ICONST_5>
                          17: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          20: <INVOKEVIRTUAL org/python/types/Object.__lt__ (Lorg/python/types/Object;)Lorg/python/types/Object;>
                          23: <GETFIELD org/python/types/Object.value (Ljava/lang/Object;)>
                          26: <CHECKCAST <Class java/lang/Boolean>>
                          29: <INVOKEVIRTUAL java/lang/Boolean.booleanValue ()Z>
                          32: <IFEQ 8>
                          35: <ALOAD_0>
                          36: <ASTORE_1>
                          37: <GOTO 54>
                          40: <ALOAD_0>
                          41: <NEW org/python/types/Object>
                          44: <DUP>
                          45: <SIPUSH 50>
                          48: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          51: <INVOKEVIRTUAL org/python/types/Object.__lt__ (Lorg/python/types/Object;)Lorg/python/types/Object;>
                          54: <GETFIELD org/python/types/Object.value (Ljava/lang/Object;)>
                          57: <CHECKCAST <Class java/lang/Boolean>>
                          60: <INVOKEVIRTUAL java/lang/Boolean.booleanValue ()Z>
                          63: <IFEQ 17>
                          66: <NEW org/python/types/Object>
                          69: <DUP>
                          70: <SIPUSH -50>
                          73: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          76: <ASTORE_1>
                          77: <GOTO 14>
                          80: <NEW org/python/types/Object>
                          83: <DUP>
                          84: <SIPUSH -999>
                          87: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          90: <ASTORE_1>
                          91: <ACONST_NULL>
                          92: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (26 bytes)
                             Line numbers (6 total):
                                 0: 2
                                 11: 3
                                 35: 4
                                 40: 5
                                 66: 6
                                 80: 8
                """)

    def test_if_elif_elif_else(self):
        self.assertBlock(
            python="""
                x = 10
                y = 0
                if x < 5:
                    y = x
                elif x < 50:
                    y = -50
                elif x < 500:
                    y = -500
                else:
                    y = -999
                """,
            java="""
                 Code (198 bytes)
                     Max stack: 4
                     Max locals: 2
                     Bytecode: (142 bytes)
                           0: <NEW org/python/types/Object>
                           3: <DUP>
                           4: <SIPUSH 10>
                           7: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          10: <ASTORE_0>
                          11: <NEW org/python/types/Object>
                          14: <DUP>
                          15: <ICONST_0>
                          16: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          19: <ASTORE_1>
                          20: <ALOAD_0>
                          21: <NEW org/python/types/Object>
                          24: <DUP>
                          25: <ICONST_5>
                          26: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          29: <INVOKEVIRTUAL org/python/types/Object.__lt__ (Lorg/python/types/Object;)Lorg/python/types/Object;>
                          32: <GETFIELD org/python/types/Object.value (Ljava/lang/Object;)>
                          35: <CHECKCAST <Class java/lang/Boolean>>
                          38: <INVOKEVIRTUAL java/lang/Boolean.booleanValue ()Z>
                          41: <IFEQ 8>
                          44: <ALOAD_0>
                          45: <ASTORE_1>
                          46: <GOTO 94>
                          49: <ALOAD_0>
                          50: <NEW org/python/types/Object>
                          53: <DUP>
                          54: <SIPUSH 50>
                          57: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          60: <INVOKEVIRTUAL org/python/types/Object.__lt__ (Lorg/python/types/Object;)Lorg/python/types/Object;>
                          63: <GETFIELD org/python/types/Object.value (Ljava/lang/Object;)>
                          66: <CHECKCAST <Class java/lang/Boolean>>
                          69: <INVOKEVIRTUAL java/lang/Boolean.booleanValue ()Z>
                          72: <IFEQ 17>
                          75: <NEW org/python/types/Object>
                          78: <DUP>
                          79: <SIPUSH -50>
                          82: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          85: <ASTORE_1>
                          86: <GOTO 54>
                          89: <ALOAD_0>
                          90: <NEW org/python/types/Object>
                          93: <DUP>
                          94: <SIPUSH 500>
                          97: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                         100: <INVOKEVIRTUAL org/python/types/Object.__lt__ (Lorg/python/types/Object;)Lorg/python/types/Object;>
                         103: <GETFIELD org/python/types/Object.value (Ljava/lang/Object;)>
                         106: <CHECKCAST <Class java/lang/Boolean>>
                         109: <INVOKEVIRTUAL java/lang/Boolean.booleanValue ()Z>
                         112: <IFEQ 17>
                         115: <NEW org/python/types/Object>
                         118: <DUP>
                         119: <SIPUSH -500>
                         122: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                         125: <ASTORE_1>
                         126: <GOTO 14>
                         129: <NEW org/python/types/Object>
                         132: <DUP>
                         133: <SIPUSH -999>
                         136: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                         139: <ASTORE_1>
                         140: <ACONST_NULL>
                         141: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (38 bytes)
                             Line numbers (9 total):
                                 0: 2
                                 11: 3
                                 20: 4
                                 44: 5
                                 49: 6
                                 75: 7
                                 89: 8
                                 115: 9
                                 129: 11
                """)

    def test_if_elif_elif(self):
        self.assertBlock(
            python="""
                x = 10
                y = 0
                if x < 5:
                    y = x
                elif x < 50:
                    y = -50
                elif x < 500:
                    y = -500
                else:
                    y = -999
                """,
            java="""
                 Code (198 bytes)
                     Max stack: 4
                     Max locals: 2
                     Bytecode: (142 bytes)
                           0: <NEW org/python/types/Object>
                           3: <DUP>
                           4: <SIPUSH 10>
                           7: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          10: <ASTORE_0>
                          11: <NEW org/python/types/Object>
                          14: <DUP>
                          15: <ICONST_0>
                          16: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          19: <ASTORE_1>
                          20: <ALOAD_0>
                          21: <NEW org/python/types/Object>
                          24: <DUP>
                          25: <ICONST_5>
                          26: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          29: <INVOKEVIRTUAL org/python/types/Object.__lt__ (Lorg/python/types/Object;)Lorg/python/types/Object;>
                          32: <GETFIELD org/python/types/Object.value (Ljava/lang/Object;)>
                          35: <CHECKCAST <Class java/lang/Boolean>>
                          38: <INVOKEVIRTUAL java/lang/Boolean.booleanValue ()Z>
                          41: <IFEQ 8>
                          44: <ALOAD_0>
                          45: <ASTORE_1>
                          46: <GOTO 94>
                          49: <ALOAD_0>
                          50: <NEW org/python/types/Object>
                          53: <DUP>
                          54: <SIPUSH 50>
                          57: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          60: <INVOKEVIRTUAL org/python/types/Object.__lt__ (Lorg/python/types/Object;)Lorg/python/types/Object;>
                          63: <GETFIELD org/python/types/Object.value (Ljava/lang/Object;)>
                          66: <CHECKCAST <Class java/lang/Boolean>>
                          69: <INVOKEVIRTUAL java/lang/Boolean.booleanValue ()Z>
                          72: <IFEQ 17>
                          75: <NEW org/python/types/Object>
                          78: <DUP>
                          79: <SIPUSH -50>
                          82: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          85: <ASTORE_1>
                          86: <GOTO 54>
                          89: <ALOAD_0>
                          90: <NEW org/python/types/Object>
                          93: <DUP>
                          94: <SIPUSH 500>
                          97: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                         100: <INVOKEVIRTUAL org/python/types/Object.__lt__ (Lorg/python/types/Object;)Lorg/python/types/Object;>
                         103: <GETFIELD org/python/types/Object.value (Ljava/lang/Object;)>
                         106: <CHECKCAST <Class java/lang/Boolean>>
                         109: <INVOKEVIRTUAL java/lang/Boolean.booleanValue ()Z>
                         112: <IFEQ 17>
                         115: <NEW org/python/types/Object>
                         118: <DUP>
                         119: <SIPUSH -500>
                         122: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                         125: <ASTORE_1>
                         126: <GOTO 14>
                         129: <NEW org/python/types/Object>
                         132: <DUP>
                         133: <SIPUSH -999>
                         136: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                         139: <ASTORE_1>
                         140: <ACONST_NULL>
                         141: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (38 bytes)
                             Line numbers (9 total):
                                 0: 2
                                 11: 3
                                 20: 4
                                 44: 5
                                 49: 6
                                 75: 7
                                 89: 8
                                 115: 9
                                 129: 11
                """)
