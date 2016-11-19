from com.example import View

class MyHandler(implements=com.example.View[Handler]):
    def event(self, view: com.example.View, name: java.lang.String) -> void:
        print("My handler for a", name, "event on", view)

view = View()

handler = MyHandler()

view.setHandler(handler)

view.doEvent("Stuff")

print("Done.")
