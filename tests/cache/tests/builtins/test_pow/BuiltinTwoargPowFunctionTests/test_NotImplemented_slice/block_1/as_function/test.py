def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = NotImplemented')
        print('>>> y = slice(0)')
        print('>>> f(x, y)')
        f = pow
        x = NotImplemented
        y = slice(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = NotImplemented')
        print('>>> y = slice(5)')
        print('>>> f(x, y)')
        f = pow
        x = NotImplemented
        y = slice(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = NotImplemented')
        print('>>> y = slice(2, 7)')
        print('>>> f(x, y)')
        f = pow
        x = NotImplemented
        y = slice(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = NotImplemented')
        print('>>> y = slice(2, 7, 2)')
        print('>>> f(x, y)')
        f = pow
        x = NotImplemented
        y = slice(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = NotImplemented')
        print('>>> y = slice(7, 2, -1)')
        print('>>> f(x, y)')
        f = pow
        x = NotImplemented
        y = slice(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = NotImplemented')
        print('>>> y = slice(7, 2, -2)')
        print('>>> f(x, y)')
        f = pow
        x = NotImplemented
        y = slice(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()