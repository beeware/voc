def test_function():
    def otherfunc(a, b, c, d, e, f=3):
        return 'ok'
    
    print(otherfunc(1))
    
test_function()