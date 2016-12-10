def test_function():
    class TestObj:
        def myfunc(self, ):
            print('Hello')
            return 5
    
    obj = TestObj()
    print("value =", obj.myfunc())
    print('Done.')
    
test_function()