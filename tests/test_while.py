from .utils import TranspileTestCase


class WhileLoopTests(TranspileTestCase):
    def test_while(self):
        self.assertCode("""
            i = 0
            total = 0
            while i < 10:
                i += 1
                total += i
                print(i, total)
            print('Done.')
            """)
