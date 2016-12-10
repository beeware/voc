def test_function():
    def myfunc(a, b, *c, d=3):
        return 'ok'
    
    print(myfunc(1))
    
test_function()