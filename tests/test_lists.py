from .utils import TranspileTestCase


class ListTests(TranspileTestCase):
    def test_creation(self):
        self.assertBlock(
            python="""
                x = [1, 2, 3, 4, 5]
                """,
            java="""
                 Code (107 bytes)
                     Max stack: 7
                     Max locals: 1
                     Bytecode: (83 bytes)
                           0: <NEW org/python/types/List>
                           3: <DUP>
                           4: <NEW java/util/ArrayList>
                           7: <DUP>
                           8: <ICONST_5>
                           9: <INVOKESPECIAL java/util/ArrayList.<init> (I)V>
                          12: <DUP>
                          13: <NEW org/python/types/Int>
                          16: <DUP>
                          17: <ICONST_1>
                          18: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          21: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          24: <POP>
                          25: <DUP>
                          26: <NEW org/python/types/Int>
                          29: <DUP>
                          30: <ICONST_2>
                          31: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          34: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          37: <POP>
                          38: <DUP>
                          39: <NEW org/python/types/Int>
                          42: <DUP>
                          43: <ICONST_3>
                          44: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          47: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          50: <POP>
                          51: <DUP>
                          52: <NEW org/python/types/Int>
                          55: <DUP>
                          56: <ICONST_4>
                          57: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          60: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          63: <POP>
                          64: <DUP>
                          65: <NEW org/python/types/Int>
                          68: <DUP>
                          69: <ICONST_5>
                          70: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          73: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          76: <POP>
                          77: <INVOKESPECIAL org/python/types/List.<init> (Ljava/util/ArrayList;)V>
                          80: <ASTORE_0>
                          81: <ACONST_NULL>
                          82: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (6 bytes)
                             Line numbers (1 total):
                                 13: 2
                """)

    def test_getitem(self):
        self.assertBlock(
            python="""
                x = (1, 2)
                a = x[1]
                """,
            java="""
                 Code (87 bytes)
                     Max stack: 7
                     Max locals: 2
                     Bytecode: (59 bytes)
                           0: <NEW org/python/types/Tuple>
                           3: <DUP>
                           4: <NEW java/util/ArrayList>
                           7: <DUP>
                           8: <ICONST_2>
                           9: <INVOKESPECIAL java/util/ArrayList.<init> (I)V>
                          12: <DUP>
                          13: <NEW org/python/types/Int>
                          16: <DUP>
                          17: <ICONST_1>
                          18: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          21: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          24: <POP>
                          25: <DUP>
                          26: <NEW org/python/types/Int>
                          29: <DUP>
                          30: <ICONST_2>
                          31: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          34: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          37: <POP>
                          38: <INVOKESPECIAL org/python/types/Tuple.<init> (Ljava/util/ArrayList;)V>
                          41: <ASTORE_0>
                          42: <ALOAD_0>
                          43: <NEW org/python/types/Int>
                          46: <DUP>
                          47: <ICONST_1>
                          48: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          51: <INVOKEINTERFACE org/python/Object.__getitem__ (Lorg/python/Object;)Lorg/python/Object;>
                          56: <ASTORE_1>
                          57: <ACONST_NULL>
                          58: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 2
                                 42: 3
                """)

    # def test_list_comprehensions(self):
    #     self.assertModule(
    #         python="""
    #             x = [1, 2, 3]
    #             y = [v**2 for v in x]
    #             """,
    #         java=[
    #             ('test', 'test', {
    #                 (None, None): """

    #                 """
    #             })
    #         ])
