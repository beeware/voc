from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class SortedTests(TranspileTestCase):
    def test_minimal(self):
        self.assertCodeExecution("""
            samples = [
                ([1, 5, 3, 2, 4, 9, 12], None),
                (["foo", "bar"], None),
                (["foo", "bar"], "invalid"),
                (["one", "two", "three", "four"], len),
                ([(1, 2), (5, 6), (3, 4)], None),
                ([(1, 2), (3, 4), (5, 6, 7)], len),
            ]
            for seq, key in samples:
                try:
                    print('Sample:', seq)
                    print('Sorted:', sorted(seq, key=key))
                    print('Reverse sorted:', sorted(seq, key=key, reverse=True))
                except Exception as e:
                    print(e)
            """, run_in_function=False)


class BuiltinSortedFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["sorted"]

    not_implemented = [
        'test_fozenset',
    ]
