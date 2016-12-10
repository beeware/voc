def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = bytearray()')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = pow
        x = bytearray()
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = bytearray()')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = pow
        x = bytearray()
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = bytearray()')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = pow
        x = bytearray()
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = bytearray(1)')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = pow
        x = bytearray(1)
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = bytearray(1)')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = pow
        x = bytearray(1)
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = bytearray(1)')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = pow
        x = bytearray(1)
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = pow
        x = bytearray([1, 2, 3])
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = pow
        x = bytearray([1, 2, 3])
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = pow
        x = bytearray([1, 2, 3])
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()