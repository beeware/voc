def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = None')
        print('>>> y = 3')
        print('>>> f(x, y)')
        f = getattr
        x = None
        y = 3
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = None')
        print('>>> y = 0')
        print('>>> f(x, y)')
        f = getattr
        x = None
        y = 0
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = None')
        print('>>> y = -5')
        print('>>> f(x, y)')
        f = getattr
        x = None
        y = -5
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = None')
        print('>>> y = -3')
        print('>>> f(x, y)')
        f = getattr
        x = None
        y = -3
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = None')
        print('>>> y = 5')
        print('>>> f(x, y)')
        f = getattr
        x = None
        y = 5
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = None')
        print('>>> y = 1')
        print('>>> f(x, y)')
        f = getattr
        x = None
        y = 1
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()