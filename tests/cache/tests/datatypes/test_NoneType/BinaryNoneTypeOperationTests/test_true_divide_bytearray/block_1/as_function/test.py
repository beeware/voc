def test_function():
    try:
        print('>>> x = None')
        print('>>> y = bytearray()')
        print('>>> x / y')
        x = None
        y = bytearray()
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = bytearray(1)')
        print('>>> x / y')
        x = None
        y = bytearray(1)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x / y')
        x = None
        y = bytearray([1, 2, 3])
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()