def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = True')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = divmod
        x = True
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = True')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = divmod
        x = True
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = True')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = divmod
        x = True
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = False')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = divmod
        x = False
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = False')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = divmod
        x = False
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = False')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = divmod
        x = False
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()