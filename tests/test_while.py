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
                 Code (115 bytes)
                     Max stack: 5
                     Max locals: 2
                     Bytecode: (75 bytes)
                           0: <NEW org/python/types/Int>
                           3: <DUP>
                           4: <ICONST_0>
                           5: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                           8: <ASTORE_0>
                           9: <NEW org/python/types/Int>
                          12: <DUP>
                          13: <ICONST_0>
                          14: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          17: <ASTORE_1>
                          18: <ALOAD_0>
                          19: <NEW org/python/types/Int>
                          22: <DUP>
                          23: <SIPUSH 10>
                          26: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          29: <INVOKEINTERFACE org/python/Object.__lt__ (Lorg/python/Object;)Lorg/python/Object;>
                          34: <INVOKEINTERFACE org/python/Object.__bool__ ()Lorg/python/types/Bool;>
                          39: <GETFIELD org/python/types/Bool.value (Z)>
                          42: <IFEQ 31>
                          45: <ALOAD_0>
                          46: <DUP>
                          47: <NEW org/python/types/Int>
                          50: <DUP>
                          51: <ICONST_1>
                          52: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          55: <INVOKEINTERFACE org/python/Object.__iadd__ (Lorg/python/Object;)V>
                          60: <ASTORE_0>
                          61: <ALOAD_1>
                          62: <DUP>
                          63: <ALOAD_0>
                          64: <INVOKEINTERFACE org/python/Object.__iadd__ (Lorg/python/Object;)V>
                          69: <ASTORE_1>
                          70: <GOTO -52>
                          73: <ACONST_NULL>
                          74: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (22 bytes)
                             Line numbers (5 total):
                                 0: 2
                                 9: 3
                                 18: 4
                                 45: 5
                                 61: 6
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
