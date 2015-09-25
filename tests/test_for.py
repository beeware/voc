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
                 Code (177 bytes)
                     Max stack: 8
                     Max locals: 3
                     Bytecode: (137 bytes)
                           0: <NEW org/python/types/Object>
                           3: <DUP>
                           4: <ICONST_0>
                           5: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                           8: <ASTORE_0>
                           9: <GETSTATIC test/test.globals (Ljava/util/Hashtable;)>
                          12: <LDC <String 'range'>>
                          14: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          17: <DUP>
                          18: <IFNONNULL 27>
                          21: <POP>
                          22: <GETSTATIC org/Python.builtins (Ljava/util/Hashtable;)>
                          25: <LDC <String 'range'>>
                          27: <INVOKEVIRTUAL java/util/Hashtable.get (Ljava/lang/Object;)Ljava/lang/Object;>
                          30: <DUP>
                          31: <IFNONNULL 14>
                          34: <POP>
                          35: <NEW org/python/exceptions/NameError>
                          38: <DUP>
                          39: <LDC <String 'range'>>
                          41: <INVOKESPECIAL org/python/exceptions/NameError.<init> (Ljava/lang/String;)V>
                          44: <ATHROW>
                          45: <CHECKCAST <Class org/python/types/Object>>
                          48: <CHECKCAST <Class org/python/Callable>>
                          51: <ICONST_2>
                          52: <ANEWARRAY org/python/types/Object>
                          55: <DUP>
                          56: <ICONST_0>
                          57: <NEW org/python/types/Object>
                          60: <DUP>
                          61: <ICONST_0>
                          62: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          65: <AASTORE>
                          66: <DUP>
                          67: <ICONST_1>
                          68: <NEW org/python/types/Object>
                          71: <DUP>
                          72: <SIPUSH 10>
                          75: <INVOKESPECIAL org/python/types/Object.<init> (I)V>
                          78: <AASTORE>
                          79: <NEW java/util/Hashtable>
                          82: <DUP>
                          83: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                          86: <INVOKEINTERFACE org/python/Callable.invoke ([Lorg/python/types/Object;Ljava/util/Hashtable;)Lorg/python/types/Object;>
                          91: <ASTORE_1>
                          92: <ICONST_1>
                          93: <ANEWARRAY org/python/types/Object>
                          96: <DUP>
                          97: <ICONST_0>
                          98: <ALOAD_1>
                          99: <AASTORE>
                         100: <NEW java/util/Hashtable>
                         103: <DUP>
                         104: <INVOKESPECIAL java/util/Hashtable.<init> ()V>
                         107: <INVOKESTATIC org/Python.iter ([Lorg/python/types/Object;Ljava/util/Hashtable;)Lorg/python/types/Object;>
                         110: <CHECKCAST <Class org/python/Iterable>>
                         113: <DUP>
                         114: <INVOKEINTERFACE org/python/Iterable.__next__ ()Lorg/python/types/Object;>
                         119: <GOTO 6>
                         122: <GOTO 13>
                         125: <ASTORE_2>
                         126: <ALOAD_0>
                         127: <ALOAD_2>
                         128: <INVOKEVIRTUAL org/python/types/Object.__add__ (Lorg/python/types/Object;)Lorg/python/types/Object;>
                         131: <ASTORE_0>
                         132: <GOTO -19>
                         135: <ACONST_NULL>
                         136: <ARETURN>
                     Exceptions: (1)
                         org/python/exceptions/StopIteration: 113-119 [122]
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 2
                                 9: 3
                                 126: 4
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
