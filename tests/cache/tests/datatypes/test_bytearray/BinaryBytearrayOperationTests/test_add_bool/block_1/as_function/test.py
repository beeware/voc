def test_function():
    try:
        print('>>> x = bytearray()')
        print('>>> y = True')
        print('>>> x + y')
        x = bytearray()
        y = True
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray()')
        print('>>> y = False')
        print('>>> x + y')
        x = bytearray()
        y = False
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = True')
        print('>>> x + y')
        x = bytearray(1)
        y = True
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = False')
        print('>>> x + y')
        x = bytearray(1)
        y = False
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = True')
        print('>>> x + y')
        x = bytearray([1, 2, 3])
        y = True
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = False')
        print('>>> x + y')
        x = bytearray([1, 2, 3])
        y = False
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()