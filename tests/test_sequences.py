from .utils import TranspileTestCase


class SequenceTests(TranspileTestCase):
    def test_unpack_seqeunce(self):
        self.assertBlock(
            python="""
                x = [1, 2, 3, 4, 5]
                a, b, c, d, e = x
                """,
            java="""
                 Code (156 bytes)
                     Max stack: 7
                     Max locals: 7
                     Bytecode: (128 bytes)
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
                          81: <ALOAD_0>
                          82: <ASTORE_1>
                          83: <ALOAD_1>
                          84: <ICONST_4>
                          85: <INVOKEINTERFACE org/python/Object.__getitem__ (I)Lorg/python/Object;>
                          90: <ALOAD_1>
                          91: <ICONST_3>
                          92: <INVOKEINTERFACE org/python/Object.__getitem__ (I)Lorg/python/Object;>
                          97: <ALOAD_1>
                          98: <ICONST_2>
                          99: <INVOKEINTERFACE org/python/Object.__getitem__ (I)Lorg/python/Object;>
                         104: <ALOAD_1>
                         105: <ICONST_1>
                         106: <INVOKEINTERFACE org/python/Object.__getitem__ (I)Lorg/python/Object;>
                         111: <ALOAD_1>
                         112: <ICONST_0>
                         113: <INVOKEINTERFACE org/python/Object.__getitem__ (I)Lorg/python/Object;>
                         118: <ASTORE_2>
                         119: <ASTORE_3>
                         120: <ASTORE 4>
                         122: <ASTORE 5>
                         124: <ASTORE 6>
                         126: <ACONST_NULL>
                         127: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 13: 2
                                 81: 3
                """)
