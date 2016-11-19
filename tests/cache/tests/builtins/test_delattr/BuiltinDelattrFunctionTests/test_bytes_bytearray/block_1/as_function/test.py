def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = b""')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = delattr
        x = b""
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = b""')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = delattr
        x = b""
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = b""')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = delattr
        x = b""
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = delattr
        x = b"This is another string of bytes"
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = delattr
        x = b"This is another string of bytes"
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = delattr
        x = b"This is another string of bytes"
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()