def test_function():
    try:
        print('>>> x = bytearray()')
        print('>>> y = bytearray()')
        print('>>> x / y')
        x = bytearray()
        y = bytearray()
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray()')
        print('>>> y = bytearray(1)')
        print('>>> x / y')
        x = bytearray()
        y = bytearray(1)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray()')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x / y')
        x = bytearray()
        y = bytearray([1, 2, 3])
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = bytearray()')
        print('>>> x / y')
        x = bytearray(1)
        y = bytearray()
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = bytearray(1)')
        print('>>> x / y')
        x = bytearray(1)
        y = bytearray(1)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x / y')
        x = bytearray(1)
        y = bytearray([1, 2, 3])
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = bytearray()')
        print('>>> x / y')
        x = bytearray([1, 2, 3])
        y = bytearray()
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = bytearray(1)')
        print('>>> x / y')
        x = bytearray([1, 2, 3])
        y = bytearray(1)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x / y')
        x = bytearray([1, 2, 3])
        y = bytearray([1, 2, 3])
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()