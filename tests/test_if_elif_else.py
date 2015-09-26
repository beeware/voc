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
                 Code (88 bytes)
                     Max stack: 4
                     Max locals: 2
                     Bytecode: (52 bytes)
                           0: <NEW org/python/types/Int>
                           3: <DUP>
                           4: <SIPUSH 10>
                           7: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          10: <ASTORE_0>
                          11: <NEW org/python/types/Int>
                          14: <DUP>
                          15: <ICONST_0>
                          16: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          19: <ASTORE_1>
                          20: <ALOAD_0>
                          21: <NEW org/python/types/Int>
                          24: <DUP>
                          25: <ICONST_5>
                          26: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          29: <INVOKEINTERFACE org/python/Object.__lt__ (Lorg/python/Object;)Lorg/python/Object;>
                          34: <INVOKEINTERFACE org/python/Object.__bool__ ()Lorg/python/types/Bool;>
                          39: <GETFIELD org/python/types/Bool.value (Z)>
                          42: <IFEQ 8>
                          45: <ALOAD_0>
                          46: <ASTORE_1>
                          47: <GOTO 3>
                          50: <ACONST_NULL>
                          51: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (18 bytes)
                             Line numbers (4 total):
                                 0: 2
                                 11: 3
                                 20: 4
                                 45: 5
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
                 Code (90 bytes)
                     Max stack: 4
                     Max locals: 2
                     Bytecode: (54 bytes)
                           0: <NEW org/python/types/Int>
                           3: <DUP>
                           4: <SIPUSH 10>
                           7: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          10: <ASTORE_0>
                          11: <ALOAD_0>
                          12: <NEW org/python/types/Int>
                          15: <DUP>
                          16: <ICONST_5>
                          17: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          20: <INVOKEINTERFACE org/python/Object.__lt__ (Lorg/python/Object;)Lorg/python/Object;>
                          25: <INVOKEINTERFACE org/python/Object.__bool__ ()Lorg/python/types/Bool;>
                          30: <GETFIELD org/python/types/Bool.value (Z)>
                          33: <IFEQ 8>
                          36: <ALOAD_0>
                          37: <ASTORE_1>
                          38: <GOTO 14>
                          41: <NEW org/python/types/Int>
                          44: <DUP>
                          45: <SIPUSH -999>
                          48: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          51: <ASTORE_1>
                          52: <ACONST_NULL>
                          53: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (18 bytes)
                             Line numbers (4 total):
                                 0: 2
                                 11: 3
                                 36: 4
                                 41: 6
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
                 Code (139 bytes)
                     Max stack: 4
                     Max locals: 2
                     Bytecode: (95 bytes)
                           0: <NEW org/python/types/Int>
                           3: <DUP>
                           4: <SIPUSH 10>
                           7: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          10: <ASTORE_0>
                          11: <ALOAD_0>
                          12: <NEW org/python/types/Int>
                          15: <DUP>
                          16: <ICONST_5>
                          17: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          20: <INVOKEINTERFACE org/python/Object.__lt__ (Lorg/python/Object;)Lorg/python/Object;>
                          25: <INVOKEINTERFACE org/python/Object.__bool__ ()Lorg/python/types/Bool;>
                          30: <GETFIELD org/python/types/Bool.value (Z)>
                          33: <IFEQ 8>
                          36: <ALOAD_0>
                          37: <ASTORE_1>
                          38: <GOTO 55>
                          41: <ALOAD_0>
                          42: <NEW org/python/types/Int>
                          45: <DUP>
                          46: <SIPUSH 50>
                          49: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          52: <INVOKEINTERFACE org/python/Object.__lt__ (Lorg/python/Object;)Lorg/python/Object;>
                          57: <INVOKEINTERFACE org/python/Object.__bool__ ()Lorg/python/types/Bool;>
                          62: <GETFIELD org/python/types/Bool.value (Z)>
                          65: <IFEQ 17>
                          68: <NEW org/python/types/Int>
                          71: <DUP>
                          72: <SIPUSH -50>
                          75: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          78: <ASTORE_1>
                          79: <GOTO 14>
                          82: <NEW org/python/types/Int>
                          85: <DUP>
                          86: <SIPUSH -999>
                          89: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          92: <ASTORE_1>
                          93: <ACONST_NULL>
                          94: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (26 bytes)
                             Line numbers (6 total):
                                 0: 2
                                 11: 3
                                 36: 4
                                 41: 5
                                 68: 6
                                 82: 8
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
                 Code (201 bytes)
                     Max stack: 4
                     Max locals: 2
                     Bytecode: (145 bytes)
                           0: <NEW org/python/types/Int>
                           3: <DUP>
                           4: <SIPUSH 10>
                           7: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          10: <ASTORE_0>
                          11: <NEW org/python/types/Int>
                          14: <DUP>
                          15: <ICONST_0>
                          16: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          19: <ASTORE_1>
                          20: <ALOAD_0>
                          21: <NEW org/python/types/Int>
                          24: <DUP>
                          25: <ICONST_5>
                          26: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          29: <INVOKEINTERFACE org/python/Object.__lt__ (Lorg/python/Object;)Lorg/python/Object;>
                          34: <INVOKEINTERFACE org/python/Object.__bool__ ()Lorg/python/types/Bool;>
                          39: <GETFIELD org/python/types/Bool.value (Z)>
                          42: <IFEQ 8>
                          45: <ALOAD_0>
                          46: <ASTORE_1>
                          47: <GOTO 96>
                          50: <ALOAD_0>
                          51: <NEW org/python/types/Int>
                          54: <DUP>
                          55: <SIPUSH 50>
                          58: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          61: <INVOKEINTERFACE org/python/Object.__lt__ (Lorg/python/Object;)Lorg/python/Object;>
                          66: <INVOKEINTERFACE org/python/Object.__bool__ ()Lorg/python/types/Bool;>
                          71: <GETFIELD org/python/types/Bool.value (Z)>
                          74: <IFEQ 17>
                          77: <NEW org/python/types/Int>
                          80: <DUP>
                          81: <SIPUSH -50>
                          84: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          87: <ASTORE_1>
                          88: <GOTO 55>
                          91: <ALOAD_0>
                          92: <NEW org/python/types/Int>
                          95: <DUP>
                          96: <SIPUSH 500>
                          99: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                         102: <INVOKEINTERFACE org/python/Object.__lt__ (Lorg/python/Object;)Lorg/python/Object;>
                         107: <INVOKEINTERFACE org/python/Object.__bool__ ()Lorg/python/types/Bool;>
                         112: <GETFIELD org/python/types/Bool.value (Z)>
                         115: <IFEQ 17>
                         118: <NEW org/python/types/Int>
                         121: <DUP>
                         122: <SIPUSH -500>
                         125: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                         128: <ASTORE_1>
                         129: <GOTO 14>
                         132: <NEW org/python/types/Int>
                         135: <DUP>
                         136: <SIPUSH -999>
                         139: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                         142: <ASTORE_1>
                         143: <ACONST_NULL>
                         144: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (38 bytes)
                             Line numbers (9 total):
                                 0: 2
                                 11: 3
                                 20: 4
                                 45: 5
                                 50: 6
                                 77: 7
                                 91: 8
                                 118: 9
                                 132: 11
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
                 Code (201 bytes)
                     Max stack: 4
                     Max locals: 2
                     Bytecode: (145 bytes)
                           0: <NEW org/python/types/Int>
                           3: <DUP>
                           4: <SIPUSH 10>
                           7: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          10: <ASTORE_0>
                          11: <NEW org/python/types/Int>
                          14: <DUP>
                          15: <ICONST_0>
                          16: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          19: <ASTORE_1>
                          20: <ALOAD_0>
                          21: <NEW org/python/types/Int>
                          24: <DUP>
                          25: <ICONST_5>
                          26: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          29: <INVOKEINTERFACE org/python/Object.__lt__ (Lorg/python/Object;)Lorg/python/Object;>
                          34: <INVOKEINTERFACE org/python/Object.__bool__ ()Lorg/python/types/Bool;>
                          39: <GETFIELD org/python/types/Bool.value (Z)>
                          42: <IFEQ 8>
                          45: <ALOAD_0>
                          46: <ASTORE_1>
                          47: <GOTO 96>
                          50: <ALOAD_0>
                          51: <NEW org/python/types/Int>
                          54: <DUP>
                          55: <SIPUSH 50>
                          58: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          61: <INVOKEINTERFACE org/python/Object.__lt__ (Lorg/python/Object;)Lorg/python/Object;>
                          66: <INVOKEINTERFACE org/python/Object.__bool__ ()Lorg/python/types/Bool;>
                          71: <GETFIELD org/python/types/Bool.value (Z)>
                          74: <IFEQ 17>
                          77: <NEW org/python/types/Int>
                          80: <DUP>
                          81: <SIPUSH -50>
                          84: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          87: <ASTORE_1>
                          88: <GOTO 55>
                          91: <ALOAD_0>
                          92: <NEW org/python/types/Int>
                          95: <DUP>
                          96: <SIPUSH 500>
                          99: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                         102: <INVOKEINTERFACE org/python/Object.__lt__ (Lorg/python/Object;)Lorg/python/Object;>
                         107: <INVOKEINTERFACE org/python/Object.__bool__ ()Lorg/python/types/Bool;>
                         112: <GETFIELD org/python/types/Bool.value (Z)>
                         115: <IFEQ 17>
                         118: <NEW org/python/types/Int>
                         121: <DUP>
                         122: <SIPUSH -500>
                         125: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                         128: <ASTORE_1>
                         129: <GOTO 14>
                         132: <NEW org/python/types/Int>
                         135: <DUP>
                         136: <SIPUSH -999>
                         139: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                         142: <ASTORE_1>
                         143: <ACONST_NULL>
                         144: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (38 bytes)
                             Line numbers (9 total):
                                 0: 2
                                 11: 3
                                 20: 4
                                 45: 5
                                 50: 6
                                 77: 7
                                 91: 8
                                 118: 9
                                 132: 11
                """)
