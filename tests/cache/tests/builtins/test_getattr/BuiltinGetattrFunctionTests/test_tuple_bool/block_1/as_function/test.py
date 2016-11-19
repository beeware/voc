def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2)')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2)
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2)')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2)
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = (3, 1.2, True, )
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = (3, 1.2, True, )
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2.3456, "another")
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2.3456, "another")
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()