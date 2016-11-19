def test_function():
    try:
        print('>>> f = hasattr')
        print('>>> x = []')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = hasattr
        x = []
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = []')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = hasattr
        x = []
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = [3, 4, 5]')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = hasattr
        x = [3, 4, 5]
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = [3, 4, 5]')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = hasattr
        x = [3, 4, 5]
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = hasattr
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = hasattr
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = ["a","b","c"]')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = hasattr
        x = ["a","b","c"]
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = ["a","b","c"]')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = hasattr
        x = ["a","b","c"]
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()