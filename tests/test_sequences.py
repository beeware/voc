from .utils import TranspileTestCase


class SequenceTests(TranspileTestCase):
    def test_unpack_seqeunce(self):
        self.assertBlock(
            python="""
                x = [1, 2, 3, 4, 5]
                a, b, c, d, e = x
                """,
            java="""
                 Code (146 bytes)
                     Max stack: 7
                     Max locals: 7
                     Bytecode: (118 bytes)
                           0: <NEW org/python/Object>
                           3: <DUP>
                           4: <NEW java/util/ArrayList>
                           7: <DUP>
                           8: <ICONST_5>
                           9: <INVOKESPECIAL java/util/ArrayList.<init> (I)V>
                          12: <DUP>
                          13: <NEW org/python/Object>
                          16: <DUP>
                          17: <ICONST_1>
                          18: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          21: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          24: <POP>
                          25: <DUP>
                          26: <NEW org/python/Object>
                          29: <DUP>
                          30: <ICONST_2>
                          31: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          34: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          37: <POP>
                          38: <DUP>
                          39: <NEW org/python/Object>
                          42: <DUP>
                          43: <ICONST_3>
                          44: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          47: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          50: <POP>
                          51: <DUP>
                          52: <NEW org/python/Object>
                          55: <DUP>
                          56: <ICONST_4>
                          57: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          60: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          63: <POP>
                          64: <DUP>
                          65: <NEW org/python/Object>
                          68: <DUP>
                          69: <ICONST_5>
                          70: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          73: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          76: <POP>
                          77: <INVOKESPECIAL org/python/Object.<init> (Ljava/util/ArrayList;)V>
                          80: <ASTORE_0>
                          81: <ALOAD_0>
                          82: <ASTORE_1>
                          83: <ALOAD_1>
                          84: <ICONST_4>
                          85: <INVOKEVIRTUAL org/python/Object.__getitem__ (I)Lorg/python/Object;>
                          88: <ALOAD_1>
                          89: <ICONST_3>
                          90: <INVOKEVIRTUAL org/python/Object.__getitem__ (I)Lorg/python/Object;>
                          93: <ALOAD_1>
                          94: <ICONST_2>
                          95: <INVOKEVIRTUAL org/python/Object.__getitem__ (I)Lorg/python/Object;>
                          98: <ALOAD_1>
                          99: <ICONST_1>
                         100: <INVOKEVIRTUAL org/python/Object.__getitem__ (I)Lorg/python/Object;>
                         103: <ALOAD_1>
                         104: <ICONST_0>
                         105: <INVOKEVIRTUAL org/python/Object.__getitem__ (I)Lorg/python/Object;>
                         108: <ASTORE_2>
                         109: <ASTORE_3>
                         110: <ASTORE 4>
                         112: <ASTORE 5>
                         114: <ASTORE 6>
                         116: <ACONST_NULL>
                         117: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 13: 2
                                 81: 3
                """)
