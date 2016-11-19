class MyClass:
    def __init__(self, val):
        print("VAL: ", val)
        self.value = val

    def stuff(self, delta):
        print("DELTA: ", delta)
        return self.value + delta

    def stuff(self, delta):
        print("Redefined DELTA: ", delta)
        return self.value + delta * 2

obj = MyClass(4)
obj.stuff(5)

print('Done.')
