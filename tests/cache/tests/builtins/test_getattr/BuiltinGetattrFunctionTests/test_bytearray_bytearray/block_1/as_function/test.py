def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray()')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray()
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray()')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray()
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray()')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray()
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray(1)')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray(1)
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray(1)')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray(1)
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray(1)')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray(1)
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray([1, 2, 3])
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray([1, 2, 3])
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray([1, 2, 3])
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()