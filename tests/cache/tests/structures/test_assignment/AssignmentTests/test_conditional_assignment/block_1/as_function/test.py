def test_function():
    x = 42
    y = 99 if x else 37
    print(y)
    x = 0
    y = 99 if x else 37
    print(y)
    print('Done.')
    
test_function()