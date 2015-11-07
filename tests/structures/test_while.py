from ..utils import TranspileTestCase


class WhileLoopTests(TranspileTestCase):
    def test_while(self):
        self.assertCodeExecution("""
            i = 0
            total = 0
            while i < 10:
                i += 1
                total += i
                print(i, total)
            print('Done.')
            """)

    def test_break(self):
        self.assertCodeExecution(
            code="""
                i = 0
                while i < 10:
                    i = i + 1
                    print(i, i % 5)
                    if i % 5 == 0:
                        break
                    print ("after")
                print("Done")
            """)

    def test_continue(self):
        self.assertCodeExecution(
            code="""
                i = 0
                while i < 10:
                    i = i + 1
                    print(i, i % 5)
                    if i % 5 == 0:
                        continue
                    print ("after")
                print("Done")
            """)
