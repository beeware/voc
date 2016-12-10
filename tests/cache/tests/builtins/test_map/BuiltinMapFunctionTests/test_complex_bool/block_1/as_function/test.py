def test_function():
    try:
        print('>>> f = map')
        print('>>> x = 1j')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = map
        x = 1j
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = 1j')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = map
        x = 1j
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = 3.14159265j')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = map
        x = 3.14159265j
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = 3.14159265j')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = map
        x = 3.14159265j
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = 1+2j')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = map
        x = 1+2j
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = 1+2j')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = map
        x = 1+2j
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = 3-4j')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = map
        x = 3-4j
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = 3-4j')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = map
        x = 3-4j
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = -5j')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = map
        x = -5j
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = -5j')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = map
        x = -5j
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()