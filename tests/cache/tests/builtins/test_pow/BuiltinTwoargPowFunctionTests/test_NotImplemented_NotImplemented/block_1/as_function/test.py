def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = NotImplemented')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = pow
        x = NotImplemented
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()