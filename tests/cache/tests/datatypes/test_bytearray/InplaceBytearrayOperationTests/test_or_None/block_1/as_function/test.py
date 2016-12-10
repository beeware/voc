def test_function():
    try:
        print('>>> x = bytearray()')
        print('>>> y = None')
        print('>>> x |= y')
        print('>>> x')
        x = bytearray()
        y = None
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = None')
        print('>>> x |= y')
        print('>>> x')
        x = bytearray(1)
        y = None
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = None')
        print('>>> x |= y')
        print('>>> x')
        x = bytearray([1, 2, 3])
        y = None
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()