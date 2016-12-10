def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = 3')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = 3
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = 3')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = 3
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = 0')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = 0
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = 0')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = 0
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = -5')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = -5
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = -5')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = -5
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = -3')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = -3
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = -3')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = -3
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = 5')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = 5
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = 5')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = 5
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = 1')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = 1
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = 1')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = 1
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()