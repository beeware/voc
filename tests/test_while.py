from .utils import TranspileTestCase


class WhileLoopTests(TranspileTestCase):
    def test_while(self):
        self.assertBlock(
            python="""
                i = 0
                total = 0
                while i < 10:
                    i += 1
                    total += i
                """,
            java="""
                 Code (110 bytes)
                     Max stack: 5
                     Max locals: 2
                     Bytecode: (70 bytes)
                           0: <NEW org/python/Object>
                           3: <DUP>
                           4: <ICONST_0>
                           5: <INVOKESPECIAL org/python/Object.<init> (I)V>
                           8: <ASTORE_0>
                           9: <NEW org/python/Object>
                          12: <DUP>
                          13: <ICONST_0>
                          14: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          17: <ASTORE_1>
                          18: <ALOAD_0>
                          19: <NEW org/python/Object>
                          22: <DUP>
                          23: <SIPUSH 10>
                          26: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          29: <INVOKEVIRTUAL org/python/Object.__lt__ (Lorg/python/Object;)Lorg/python/Object;>
                          32: <GETFIELD org/python/Object.value (Ljava/lang/Object;)>
                          35: <CHECKCAST <Class java/lang/Boolean>>
                          38: <INVOKEVIRTUAL java/lang/Boolean.booleanValue ()Z>
                          41: <IFEQ 27>
                          44: <ALOAD_0>
                          45: <DUP>
                          46: <NEW org/python/Object>
                          49: <DUP>
                          50: <ICONST_1>
                          51: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          54: <INVOKEVIRTUAL org/python/Object.__iadd__ (Lorg/python/Object;)V>
                          57: <ASTORE_0>
                          58: <ALOAD_1>
                          59: <DUP>
                          60: <ALOAD_0>
                          61: <INVOKEVIRTUAL org/python/Object.__iadd__ (Lorg/python/Object;)V>
                          64: <ASTORE_1>
                          65: <GOTO -47>
                          68: <ACONST_NULL>
                          69: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (22 bytes)
                             Line numbers (5 total):
                                 0: 2
                                 9: 3
                                 18: 4
                                 44: 5
                                 58: 6
                """)

    # def test_for_over_generator(self):
    #     self.assertBlock(
    #         python="""
    #             total = 0
    #             for i in [1, 2, 3, 5, 8, 13, 21]:
    #                 total = total + i
    #             """,
    #         java="""
    #          Code (159 bytes)
    #         """)
