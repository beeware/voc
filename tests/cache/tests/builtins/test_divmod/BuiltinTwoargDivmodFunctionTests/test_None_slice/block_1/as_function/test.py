def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = None')
        print('>>> y = slice(0)')
        print('>>> f(x, y)')
        f = divmod
        x = None
        y = slice(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = None')
        print('>>> y = slice(5)')
        print('>>> f(x, y)')
        f = divmod
        x = None
        y = slice(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = None')
        print('>>> y = slice(2, 7)')
        print('>>> f(x, y)')
        f = divmod
        x = None
        y = slice(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = None')
        print('>>> y = slice(2, 7, 2)')
        print('>>> f(x, y)')
        f = divmod
        x = None
        y = slice(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = None')
        print('>>> y = slice(7, 2, -1)')
        print('>>> f(x, y)')
        f = divmod
        x = None
        y = slice(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = None')
        print('>>> y = slice(7, 2, -2)')
        print('>>> f(x, y)')
        f = divmod
        x = None
        y = slice(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()