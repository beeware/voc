from ..utils import TranspileTestCase


class ListComprehensionTests(TranspileTestCase):
    def test_list_comprehension(self):
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print([v**2 for v in x])
            print('Done.')
            """)
