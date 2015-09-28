from .utils import TranspileTestCase


class ForLoopTests(TranspileTestCase):
    def test_for_over_range(self):
        self.assertBlock(
            python="""
                total = 0
                for i in range(0, 10):
                    total = total + i
                """,
            java="""
                 Code (181 bytes)
                     Max stack: 11
                     Max locals: 2
                     Bytecode: (141 bytes)
                           0: <NEW org/python/types/Int>
                           3: <DUP>
                           4: <ICONST_0>
                           5: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                           8: <ASTORE_0>
                           9: <ICONST_1>
                          10: <ANEWARRAY org/python/Object>
                          13: <DUP>
                          14: <ICONST_0>
                          15: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          18: <LDC_W <String 'range'>>
                          21: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          24: <DUP>
                          25: <IFNONNULL 29>
                          28: <POP>
                          29: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          32: <LDC_W <String 'range'>>
                          35: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          38: <DUP>
                          39: <IFNONNULL 15>
                          42: <POP>
                          43: <NEW org/python/exceptions/NameError>
                          46: <DUP>
                          47: <LDC_W <String 'range'>>
                          50: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          53: <ATHROW>
                          54: <CHECKCAST <Class org/python/types/Object>>
                          57: <CHECKCAST <Class org/python/Callable>>
                          60: <ICONST_2>
                          61: <ANEWARRAY org/python/Object>
                          64: <DUP>
                          65: <ICONST_0>
                          66: <NEW org/python/types/Int>
                          69: <DUP>
                          70: <ICONST_0>
                          71: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          74: <AASTORE>
                          75: <DUP>
                          76: <ICONST_1>
                          77: <NEW org/python/types/Int>
                          80: <DUP>
                          81: <SIPUSH 10>
                          84: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          87: <AASTORE>
                          88: <NEW java/util/Hashtable>
                          91: <DUP>
                          92: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          95: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                         100: <AASTORE>
                         101: <NEW java/util/Hashtable>
                         104: <DUP>
                         105: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         108: <INVOKESTATIC org/Python.iter ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Iterable;>
                         111: <CHECKCAST <Class org/python/Iterable>>
                         114: <DUP>
                         115: <INVOKEINTERFACE org/python/Iterable.__next__ ()Lorg/python/Object;>
                         120: <GOTO 7>
                         123: <POP>
                         124: <GOTO 15>
                         127: <ASTORE_1>
                         128: <ALOAD_0>
                         129: <ALOAD_1>
                         130: <INVOKEINTERFACE org/python/Object.__add__ (Lorg/python/Object;)Lorg/python/Object;>
                         135: <ASTORE_0>
                         136: <GOTO -22>
                         139: <ACONST_NULL>
                         140: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/StopIteration: 114-120 [123]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 2
                                 9: 3
                                 128: 4
                """)

    def test_for_over_iterable(self):
        self.assertBlock(
            python="""
                total = 0
                for i in [1, 2, 3, 5, 8, 13, 21]:
                    total = total + i
                """,
            java="""
                 Code (210 bytes)
                     Max stack: 11
                     Max locals: 2
                     Bytecode: (170 bytes)
                           0: <NEW org/python/types/Int>
                           3: <DUP>
                           4: <ICONST_0>
                           5: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                           8: <ASTORE_0>
                           9: <ICONST_1>
                          10: <ANEWARRAY org/python/Object>
                          13: <DUP>
                          14: <ICONST_0>
                          15: <NEW org/python/types/List>
                          18: <DUP>
                          19: <NEW java/util/ArrayList>
                          22: <DUP>
                          23: <SIPUSH 7>
                          26: <INVOKESPECIAL java/util/ArrayList.<init> (I)V>
                          29: <DUP>
                          30: <NEW org/python/types/Int>
                          33: <DUP>
                          34: <ICONST_1>
                          35: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          38: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          41: <POP>
                          42: <DUP>
                          43: <NEW org/python/types/Int>
                          46: <DUP>
                          47: <ICONST_2>
                          48: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          51: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          54: <POP>
                          55: <DUP>
                          56: <NEW org/python/types/Int>
                          59: <DUP>
                          60: <ICONST_3>
                          61: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          64: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          67: <POP>
                          68: <DUP>
                          69: <NEW org/python/types/Int>
                          72: <DUP>
                          73: <ICONST_5>
                          74: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          77: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          80: <POP>
                          81: <DUP>
                          82: <NEW org/python/types/Int>
                          85: <DUP>
                          86: <SIPUSH 8>
                          89: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          92: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          95: <POP>
                          96: <DUP>
                          97: <NEW org/python/types/Int>
                         100: <DUP>
                         101: <SIPUSH 13>
                         104: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                         107: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                         110: <POP>
                         111: <DUP>
                         112: <NEW org/python/types/Int>
                         115: <DUP>
                         116: <SIPUSH 21>
                         119: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                         122: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                         125: <POP>
                         126: <INVOKESPECIAL org/python/types/List.<init> (Ljava/util/ArrayList;)V>
                         129: <AASTORE>
                         130: <NEW java/util/Hashtable>
                         133: <DUP>
                         134: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         137: <INVOKESTATIC org/Python.iter ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Iterable;>
                         140: <CHECKCAST <Class org/python/Iterable>>
                         143: <DUP>
                         144: <INVOKEINTERFACE org/python/Iterable.__next__ ()Lorg/python/Object;>
                         149: <GOTO 7>
                         152: <POP>
                         153: <GOTO 15>
                         156: <ASTORE_1>
                         157: <ALOAD_0>
                         158: <ALOAD_1>
                         159: <INVOKEINTERFACE org/python/Object.__add__ (Lorg/python/Object;)Lorg/python/Object;>
                         164: <ASTORE_0>
                         165: <GOTO -22>
                         168: <ACONST_NULL>
                         169: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/StopIteration: 143-149 [152]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 2
                                 9: 3
                                 157: 4
                """)

    # def test_for_else(self):
    #     self.assertBlock(
    #         python="""
    #             total = 0
    #             for i in []:
    #                 total = total + i
    #             else:
    #                 total = -999
    #             """,
    #         java="""
    #          Code (159 bytes)
    #         """)
