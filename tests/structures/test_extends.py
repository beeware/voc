from ..utils import TranspileTestCase


class ExtendsTests(TranspileTestCase):
    def test_extends(self):
        self.assertJavaExecution(
            """
            from java.util import HashMap

            class MyHashMap(extends=java.util.HashMap):
                def push_button(self):
                    return "Bing!"

                def put(self, key: java.lang.Object, value: java.lang.Object) -> java.lang.Object:
                    print("I WANT TO SET", key, "TO", value)
                    return super().put(key, value)

            mymap = MyHashMap()
            print(mymap)
            mymap.put("The answer", "42")
            print(mymap)
            print("The answer is", mymap.get("The answer"))
            print("The question is", mymap.get("The question"))
            print("The machine goes " + mymap.push_button())
            print("Done.")
            """,
            """
            {}
            I WANT TO SET The answer TO 42
            {The answer=42}
            The answer is 42
            The question is None
            The machine goes Bing!
            Done.
            """, run_in_function=False)

    def test_no_default_constructor(self):
        self.assertJavaExecution(
            """
            class MyClass(extends=com.example.BaseClass):
                @super({v * 3: int})
                def __init__(self, v):
                    pass

                def peek(self):
                    return self.base_value


            obj = MyClass(42)
            print("POKE:", obj.poke())
            print("PEEK:", obj.peek())
            """,
            java={
                'com/example/BaseClass': """
                package com.example;

                public class BaseClass {
                    public int base_value;

                    public BaseClass(int v) {
                        base_value = v;
                    }

                    public int poke() {
                        return 2 * base_value;
                    }
                }
                """
            },
            out="""
            POKE: 252
            PEEK: 126
            """,
            run_in_function=False)

    def test_protected_access(self):
        self.assertJavaExecution(
            """
            class MyClass(extends=com.example.BaseClass):
                @super({v: int})
                def __init__(self, v):
                    pass

                def peek(self):
                    return self.poke()


            obj = MyClass(42)
            print("PEEK:", obj.peek())
            """,
            java={
                'com/example/BaseClass': """
                package com.example;

                public class BaseClass {
                    public int base_value;

                    public BaseClass(int v) {
                        base_value = v;
                    }

                    protected int poke() {
                        return 2 * base_value;
                    }
                }
                """
            },
            out="""
            PEEK: 84
            """,
            run_in_function=False)
