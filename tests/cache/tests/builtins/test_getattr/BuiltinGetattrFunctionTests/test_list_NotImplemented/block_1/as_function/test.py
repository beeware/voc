def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = []')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = getattr
        x = []
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = [3, 4, 5]')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = getattr
        x = [3, 4, 5]
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = getattr
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = ["a","b","c"]')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = getattr
        x = ["a","b","c"]
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()