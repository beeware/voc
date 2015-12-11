from ..utils import TranspileTestCase


class InterfaceTests(TranspileTestCase):

    def test_implement_interface(self):
        "You can implement (and use) a native Java interface"
        self.assertJavaExecution(
            """
            from java.lang import StringBuilder

            class MyStringAnalog(implements=java.lang.CharSequence):
                def __init__(self, value):
                    self.value = value

                def charAt(self, index: int) -> char:
                    return 'x'

                def length(self) -> int:
                    return len(self.value)

                def subSequence(self, start: int, end: int) -> java.lang.CharSequence:
                    return MyStringAnalog(self.value[start:end])

                def toString(self) -> java.lang.String:
                    return self.value

            analog = MyStringAnalog("world")

            builder = StringBuilder()

            builder.append("Hello, ")
            builder.append(analog)

            print(builder)
            print("Done.")
            """,
            """
            Hello, world
            Done.
            """, run_in_function=False)
