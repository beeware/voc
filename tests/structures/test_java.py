from ..utils import TranspileTestCase


class JavaTests(TranspileTestCase):

    def test_multiple_constructors(self):
        "The appropriate constructor for a native Java class can be interpolated from args"
        self.assertJavaExecution(
            """
            from java.lang import StringBuilder

            builder = StringBuilder("Hello, ")

            builder.append("world")

            print(builder)
            print("Done.")
            """,
            """
            Hello, world
            Done.
            """, run_in_function=False)
