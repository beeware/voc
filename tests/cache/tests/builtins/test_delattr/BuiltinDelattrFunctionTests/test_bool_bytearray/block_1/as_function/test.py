def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = True')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = delattr
        x = True
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = True')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = delattr
        x = True
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = True')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = delattr
        x = True
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = False')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = delattr
        x = False
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = False')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = delattr
        x = False
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = False')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = delattr
        x = False
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()