from .utils import TranspileTestCase


class ForLoopTests(TranspileTestCase):
    def test_for_over_range(self):
        # Normal range
        self.assertCode("""
            total = 0
            for i in range(0, 5):
                total = total + i
                print(i, total)
            print('Done.')
            """)

        # Empty range
        self.assertCode("""
              total = 0
              for i in range(0, 0):
                  total = total + i
                  print(i, total)
              print('Done.')
              """)

        # Stepped range
        self.assertCode("""
              total = 0
              for i in range(0, 10, 2):
                  total = total + i
                  print(i, total)
              print('Done.')
              """)

        # Reverse range
        self.assertCode("""
              total = 0
              for i in range(5, 0, -1):
                  total = total + i
                  print(i, total)
              print('Done.')
              """)

    def test_for_over_iterable(self):
        self.assertCode("""
            total = 0
            for i in [1, 2, 3, 5]:
                total = total + i
                print(i, total)
            print('Done.')
            """)

        self.assertCode("""
            total = 0
            for i in []:
                total = total + i
                print(i, total)
            print('Done.')
            """)

    # def test_for_else(self):
    #     self.assertCode(
    #         code="""
    #             total = 0
    #             for i in []:
    #                 total = total + i
    #             else:
    #                 total = -999
    #             """,
    #         expected="""
    #          Code (159 bytes)
    #         """)
