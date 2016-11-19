def test_function():
    try:
        print('>>> f = filter')
        print('>>> x = NotImplemented')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = filter
        x = NotImplemented
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()