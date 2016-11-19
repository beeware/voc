def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = slice(0)')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = slice(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = slice(5)')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = slice(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = slice(2, 7)')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = slice(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = slice(2, 7, 2)')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = slice(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = slice(7, 2, -1)')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = slice(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = slice(7, 2, -2)')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = slice(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = slice(0)')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = slice(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = slice(5)')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = slice(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = slice(2, 7)')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = slice(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = slice(2, 7, 2)')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = slice(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = slice(7, 2, -1)')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = slice(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = slice(7, 2, -2)')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = slice(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()