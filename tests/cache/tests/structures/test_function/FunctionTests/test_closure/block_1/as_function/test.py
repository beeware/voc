def test_function():
    def myfunc(value):
        print(value * 3)
    
        def myinner(value2):
            print(value2 * value)
            return value2 + 6
    
        print("inner value =", myinner(10))
        return value + 5
    
    print("outer =", myfunc(5))
    print('Done.')
    
test_function()