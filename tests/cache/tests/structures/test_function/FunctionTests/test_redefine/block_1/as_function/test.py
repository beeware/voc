def test_function():
    def myfunc(value):
        print(value * 3)
        return value + 5
    
    def myfunc(value):
        print(value * 4)
        return value + 6
    
    print("value =", myfunc(5))
    print('Done.')
    
test_function()