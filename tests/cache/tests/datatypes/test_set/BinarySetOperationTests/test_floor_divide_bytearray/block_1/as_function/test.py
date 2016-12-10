def test_function():
    try:
        print('>>> x = set()')
        print('>>> y = bytearray()')
        print('>>> x // y')
        x = set()
        y = bytearray()
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = bytearray(1)')
        print('>>> x // y')
        x = set()
        y = bytearray(1)
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x // y')
        x = set()
        y = bytearray([1, 2, 3])
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = bytearray()')
        print('>>> x // y')
        x = {1, 2.3456, "another"}
        y = bytearray()
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = bytearray(1)')
        print('>>> x // y')
        x = {1, 2.3456, "another"}
        y = bytearray(1)
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x // y')
        x = {1, 2.3456, "another"}
        y = bytearray([1, 2, 3])
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()