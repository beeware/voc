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
                 Code (159 bytes)
                     Max stack: 8
                     Max locals: 3
                     Bytecode: (119 bytes)
                           0: <NEW org/python/Object>
                           3: <DUP>
                           4: <ICONST_0>
                           5: <INVOKESPECIAL org/python/Object.<init> (I)V>
                           8: <ASTORE_0>
                           9: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          12: <LDC <String 'range'>>
                          14: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          17: <DUP>
                          18: <IFNONNULL 12>
                          21: <POP>
                          22: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          25: <LDC <String 'range'>>
                          27: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          30: <CHECKCAST <Class org/python/Callable>>
                          33: <ICONST_2>
                          34: <ANEWARRAY org/python/Object>
                          37: <DUP>
                          38: <ICONST_0>
                          39: <NEW org/python/Object>
                          42: <DUP>
                          43: <ICONST_0>
                          44: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          47: <AASTORE>
                          48: <DUP>
                          49: <ICONST_1>
                          50: <NEW org/python/Object>
                          53: <DUP>
                          54: <SIPUSH 10>
                          57: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          60: <AASTORE>
                          61: <NEW java/util/Hashtable>
                          64: <DUP>
                          65: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          68: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          73: <ASTORE_1>
                          74: <ICONST_1>
                          75: <ANEWARRAY org/python/Object>
                          78: <DUP>
                          79: <ICONST_0>
                          80: <ALOAD_1>
                          81: <AASTORE>
                          82: <NEW java/util/Hashtable>
                          85: <DUP>
                          86: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          89: <INVOKESTATIC org/Python.iter ([Lorg/python/Object;Ljava/util/Hashtable;)Lorg/python/Object;>
                          92: <CHECKCAST <Class org/python/Iterator>>
                          95: <DUP>
                          96: <INVOKEINTERFACE org/python/Iterator.__next__ ()Lorg/python/Object;>
                         101: <GOTO 6>
                         104: <GOTO 13>
                         107: <ASTORE_2>
                         108: <ALOAD_0>
                         109: <ALOAD_2>
                         110: <INVOKEVIRTUAL org/python/Object.__add__ (Lorg/python/Object;)Lorg/python/Object;>
                         113: <ASTORE_0>
                         114: <GOTO -19>
                         117: <ACONST_NULL>
                         118: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/StopIteration: 95-101 [104]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 2
                                 9: 3
                                 108: 4
                """)

    # def test_for_over_iterable(self):
    #     self.assertBlock(
    #         python="""
    #             total = 0
    #             for i in [1, 2, 3, 5, 8, 13, 21]:
    #                 total = total + i
    #             """,
    #         java="""
    #          Code (159 bytes)
    #         """)

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
