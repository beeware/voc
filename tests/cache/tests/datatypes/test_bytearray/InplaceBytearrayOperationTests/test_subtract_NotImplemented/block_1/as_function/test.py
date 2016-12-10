def test_function():
    try:
        print('>>> x = bytearray()')
        print('>>> y = NotImplemented')
        print('>>> x -= y')
        print('>>> x')
        x = bytearray()
        y = NotImplemented
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = NotImplemented')
        print('>>> x -= y')
        print('>>> x')
        x = bytearray(1)
        y = NotImplemented
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = NotImplemented')
        print('>>> x -= y')
        print('>>> x')
        x = bytearray([1, 2, 3])
        y = NotImplemented
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()