def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2)')
        print('>>> y = range(0)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2)
        y = range(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2)')
        print('>>> y = range(5)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2)
        y = range(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2)')
        print('>>> y = range(2, 7)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2)
        y = range(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2)')
        print('>>> y = range(2, 7, 2)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2)
        y = range(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2)')
        print('>>> y = range(7, 2, -1)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2)
        y = range(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2)')
        print('>>> y = range(7, 2, -2)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2)
        y = range(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = range(0)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = range(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = range(5)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = range(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = range(2, 7)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = range(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = range(2, 7, 2)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = range(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = range(7, 2, -1)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = range(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = range(7, 2, -2)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = range(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = range(0)')
        print('>>> f(x, y)')
        f = getattr
        x = (3, 1.2, True, )
        y = range(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = range(5)')
        print('>>> f(x, y)')
        f = getattr
        x = (3, 1.2, True, )
        y = range(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = range(2, 7)')
        print('>>> f(x, y)')
        f = getattr
        x = (3, 1.2, True, )
        y = range(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = range(2, 7, 2)')
        print('>>> f(x, y)')
        f = getattr
        x = (3, 1.2, True, )
        y = range(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = range(7, 2, -1)')
        print('>>> f(x, y)')
        f = getattr
        x = (3, 1.2, True, )
        y = range(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = range(7, 2, -2)')
        print('>>> f(x, y)')
        f = getattr
        x = (3, 1.2, True, )
        y = range(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = range(0)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2.3456, "another")
        y = range(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = range(5)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2.3456, "another")
        y = range(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = range(2, 7)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2.3456, "another")
        y = range(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = range(2, 7, 2)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2.3456, "another")
        y = range(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = range(7, 2, -1)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2.3456, "another")
        y = range(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = range(7, 2, -2)')
        print('>>> f(x, y)')
        f = getattr
        x = (1, 2.3456, "another")
        y = range(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()