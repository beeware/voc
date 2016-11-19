def test_function():
    try:
        print('>>> f = hasattr')
        print('>>> x = True')
        print('>>> y = []')
        print('>>> f(x, y)')
        f = hasattr
        x = True
        y = []
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = True')
        print('>>> y = [3, 4, 5]')
        print('>>> f(x, y)')
        f = hasattr
        x = True
        y = [3, 4, 5]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = True')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> f(x, y)')
        f = hasattr
        x = True
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = True')
        print('>>> y = ["a","b","c"]')
        print('>>> f(x, y)')
        f = hasattr
        x = True
        y = ["a","b","c"]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = False')
        print('>>> y = []')
        print('>>> f(x, y)')
        f = hasattr
        x = False
        y = []
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = False')
        print('>>> y = [3, 4, 5]')
        print('>>> f(x, y)')
        f = hasattr
        x = False
        y = [3, 4, 5]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = False')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> f(x, y)')
        f = hasattr
        x = False
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = False')
        print('>>> y = ["a","b","c"]')
        print('>>> f(x, y)')
        f = hasattr
        x = False
        y = ["a","b","c"]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()