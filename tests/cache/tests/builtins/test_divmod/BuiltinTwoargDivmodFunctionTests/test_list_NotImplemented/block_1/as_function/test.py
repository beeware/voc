def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = []')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = divmod
        x = []
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = [3, 4, 5]')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = divmod
        x = [3, 4, 5]
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = divmod
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = ["a","b","c"]')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = divmod
        x = ["a","b","c"]
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()