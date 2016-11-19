def test_function():
    try:
        print('>>> x = {}')
        print('>>> y = bytearray()')
        print('>>> x *= y')
        print('>>> x')
        x = {}
        y = bytearray()
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = bytearray(1)')
        print('>>> x *= y')
        print('>>> x')
        x = {}
        y = bytearray(1)
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x *= y')
        print('>>> x')
        x = {}
        y = bytearray([1, 2, 3])
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = bytearray()')
        print('>>> x *= y')
        print('>>> x')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = bytearray()
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = bytearray(1)')
        print('>>> x *= y')
        print('>>> x')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = bytearray(1)
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x *= y')
        print('>>> x')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = bytearray([1, 2, 3])
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()