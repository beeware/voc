def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = []')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = delattr
        x = []
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = []')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = delattr
        x = []
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = [3, 4, 5]')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = delattr
        x = [3, 4, 5]
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = [3, 4, 5]')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = delattr
        x = [3, 4, 5]
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = delattr
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = delattr
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = ["a","b","c"]')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = delattr
        x = ["a","b","c"]
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = ["a","b","c"]')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = delattr
        x = ["a","b","c"]
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()