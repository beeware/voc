def test_function():
    def foo(x):
        print("Testing", x)
        if x == 0:
            return 42
        else:
            return 37
    y = foo(100)
    print("Result", y)
    print('Done')
    
test_function()