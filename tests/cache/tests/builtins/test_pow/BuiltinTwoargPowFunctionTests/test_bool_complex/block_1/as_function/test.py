def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = 1j')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = 1j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = 3.14159265j')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = 3.14159265j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = 1+2j')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = 1+2j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = 3-4j')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = 3-4j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = -5j')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = -5j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = 1j')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = 1j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = 3.14159265j')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = 3.14159265j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = 1+2j')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = 1+2j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = 3-4j')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = 3-4j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = -5j')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = -5j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()