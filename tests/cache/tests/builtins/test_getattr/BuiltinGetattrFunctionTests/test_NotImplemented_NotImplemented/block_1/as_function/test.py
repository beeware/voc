def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = NotImplemented')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = getattr
        x = NotImplemented
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()