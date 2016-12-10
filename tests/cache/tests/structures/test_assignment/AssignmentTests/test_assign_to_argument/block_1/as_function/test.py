def test_function():
    def foo(arg):
        val = arg + 10
        arg = val - 2
        return arg
    print(foo(20))
    print('Done.')
    
test_function()