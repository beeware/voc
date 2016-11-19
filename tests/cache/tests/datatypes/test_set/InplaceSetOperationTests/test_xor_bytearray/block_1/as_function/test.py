def test_function():
    try:
        print('>>> x = set()')
        print('>>> y = bytearray()')
        print('>>> x ^= y')
        print('>>> x')
        x = set()
        y = bytearray()
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = bytearray(1)')
        print('>>> x ^= y')
        print('>>> x')
        x = set()
        y = bytearray(1)
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x ^= y')
        print('>>> x')
        x = set()
        y = bytearray([1, 2, 3])
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = bytearray()')
        print('>>> x ^= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = bytearray()
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = bytearray(1)')
        print('>>> x ^= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = bytearray(1)
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x ^= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = bytearray([1, 2, 3])
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()