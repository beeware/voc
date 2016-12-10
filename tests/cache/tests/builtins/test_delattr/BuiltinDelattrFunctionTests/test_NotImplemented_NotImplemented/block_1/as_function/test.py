def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = NotImplemented')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = delattr
        x = NotImplemented
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()