def test_function():
    try:
        print('>>> x = bytearray()')
        print('>>> y = True')
        print('>>> x %= y')
        print('>>> x')
        x = bytearray()
        y = True
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray()')
        print('>>> y = False')
        print('>>> x %= y')
        print('>>> x')
        x = bytearray()
        y = False
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = True')
        print('>>> x %= y')
        print('>>> x')
        x = bytearray(1)
        y = True
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = False')
        print('>>> x %= y')
        print('>>> x')
        x = bytearray(1)
        y = False
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = True')
        print('>>> x %= y')
        print('>>> x')
        x = bytearray([1, 2, 3])
        y = True
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = False')
        print('>>> x %= y')
        print('>>> x')
        x = bytearray([1, 2, 3])
        y = False
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()