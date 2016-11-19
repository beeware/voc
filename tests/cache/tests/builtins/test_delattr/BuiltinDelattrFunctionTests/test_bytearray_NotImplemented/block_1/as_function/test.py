def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = bytearray()')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = delattr
        x = bytearray()
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = bytearray(1)')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = delattr
        x = bytearray(1)
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = delattr
        x = bytearray([1, 2, 3])
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()