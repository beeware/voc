from unittest import expectedFailure

from ..utils import TranspileTestCase


class ExtendsTests(TranspileTestCase):
    @expectedFailure
    def test_extends(self):
        self.assertJavaExecution(
            """
            from java.util import HashMap

            class MyHashMap(extends=java.util.HashMap):
                def push_button(self):
                    return "Bing!"

            mymap = MyHashMap()

            mymap.put("X", "Y")

            print(mymap.get("X"))
            print("The machine goes " + mymap.push_button())
            print("Done.")
            """,
            """
            Hello, world
            Done.
            """, run_in_function=False)
