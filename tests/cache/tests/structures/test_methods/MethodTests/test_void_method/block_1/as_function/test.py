def test_function():
    class TestObj:
        def myfunc(self, value):
            print(value * 3)
    
    obj = TestObj()
    obj.myfunc(5)
    print('Done.')
    
test_function()