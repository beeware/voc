def test_function():
    def myfunc():
        print('Hello')
        return 5
    
    print("value =", myfunc())
    print('Done.')
    
test_function()