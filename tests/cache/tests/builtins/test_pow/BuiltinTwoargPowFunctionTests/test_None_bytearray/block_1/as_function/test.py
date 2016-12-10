def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = None')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = pow
        x = None
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = None')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = pow
        x = None
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = None')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = pow
        x = None
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()