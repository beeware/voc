def test_function():
    try:
        print('>>> f = hasattr')
        print('>>> x = NotImplemented')
        print('>>> y = []')
        print('>>> f(x, y)')
        f = hasattr
        x = NotImplemented
        y = []
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = NotImplemented')
        print('>>> y = [3, 4, 5]')
        print('>>> f(x, y)')
        f = hasattr
        x = NotImplemented
        y = [3, 4, 5]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = NotImplemented')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> f(x, y)')
        f = hasattr
        x = NotImplemented
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = NotImplemented')
        print('>>> y = ["a","b","c"]')
        print('>>> f(x, y)')
        f = hasattr
        x = NotImplemented
        y = ["a","b","c"]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()