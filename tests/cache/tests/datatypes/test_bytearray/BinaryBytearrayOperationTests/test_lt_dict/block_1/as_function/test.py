def test_function():
    try:
        print('>>> x = bytearray()')
        print('>>> y = {}')
        print('>>> x < y')
        x = bytearray()
        y = {}
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray()')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x < y')
        x = bytearray()
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = {}')
        print('>>> x < y')
        x = bytearray(1)
        y = {}
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x < y')
        x = bytearray(1)
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = {}')
        print('>>> x < y')
        x = bytearray([1, 2, 3])
        y = {}
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x < y')
        x = bytearray([1, 2, 3])
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()