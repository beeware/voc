from .. utils import TranspileTestCase


class NamedTupleTests(TranspileTestCase):
    def test_creation(self):
        self.assertCodeExecution("""
            Point = namedtuple('sad','asd')
            print(Point)

            Point1 = namedtuple(Point, ['x', 'y'])
            print(Point)

            Point = namedtuple()
            print(Point)

            Point = namedtuple('Point')
            print(Point)

            Point = namedtuple('Point1', ['x', 'y'])
            print(Point)

            """)
