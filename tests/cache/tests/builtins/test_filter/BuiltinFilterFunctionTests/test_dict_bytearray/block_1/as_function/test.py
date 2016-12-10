def test_function():
    try:
        print('>>> f = filter')
        print('>>> x = {}')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = filter
        x = {}
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {}')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = filter
        x = {}
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {}')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = filter
        x = {}
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = filter
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = filter
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = filter
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()