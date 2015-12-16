from unittest import expectedFailure

from ..utils import TranspileTestCase


class ExtendsTests(TranspileTestCase):
    def test_extends(self):
        self.assertJavaExecution(
            """
            from java.util import HashMap

            class MyHashMap(extends=java.util.HashMap):
                def push_button(self):
                    return "Bing!"

            mymap = MyHashMap()

            mymap.put("The answer", "42")

            print(mymap.get("The answer"))
            print("The machine goes " + mymap.push_button())
            print("Done.")
            """,
            """
            42
            The machine goes Bing!
            Done.
            """, run_in_function=False)
