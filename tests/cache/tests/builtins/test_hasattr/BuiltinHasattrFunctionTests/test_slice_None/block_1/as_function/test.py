def test_function():
    try:
        print('>>> f = hasattr')
        print('>>> x = slice(0)')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = hasattr
        x = slice(0)
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = slice(5)')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = hasattr
        x = slice(5)
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = slice(2, 7)')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = hasattr
        x = slice(2, 7)
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = slice(2, 7, 2)')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = hasattr
        x = slice(2, 7, 2)
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = slice(7, 2, -1)')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = hasattr
        x = slice(7, 2, -1)
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = slice(7, 2, -2)')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = hasattr
        x = slice(7, 2, -2)
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()