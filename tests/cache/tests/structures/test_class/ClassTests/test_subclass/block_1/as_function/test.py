def test_function():
    class MyBase:
        def __init__(self, x):
            self.x = x
    
        def __str__(self):
            return "Mybase instance %s" % self.x
    
        def first(self):
            return self.x * 2
    
    
    class MyObject(MyBase):
        def __init__(self, x, y):
            super().__init__(x)
            self.y = y
    
        def __str__(self):
            return "Myobject instance %s, %s" % (self.x, self.y)
    
        def second(self):
            return self.x * self.y
    
    obj = MyObject(37, 42)
    
    print(obj)
    print(obj.x)
    print(obj.first())
    print(obj.y)
    print(obj.second())
    print('Done.')
    
test_function()