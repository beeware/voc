def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray()')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray()
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray()')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray()
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray(1)')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray(1)
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray(1)')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray(1)
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray([1, 2, 3])
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray([1, 2, 3])
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()