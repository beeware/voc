def test_function():
    try:
        print('>>> f = filter')
        print('>>> x = set()')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = set()
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = {1, 2.3456, "another"}
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()