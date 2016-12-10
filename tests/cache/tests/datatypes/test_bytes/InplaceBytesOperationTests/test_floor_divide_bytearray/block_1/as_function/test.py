def test_function():
    try:
        print('>>> x = b""')
        print('>>> y = bytearray()')
        print('>>> x //= y')
        print('>>> x')
        x = b""
        y = bytearray()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = bytearray(1)')
        print('>>> x //= y')
        print('>>> x')
        x = b""
        y = bytearray(1)
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x //= y')
        print('>>> x')
        x = b""
        y = bytearray([1, 2, 3])
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = bytearray()')
        print('>>> x //= y')
        print('>>> x')
        x = b"This is another string of bytes"
        y = bytearray()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = bytearray(1)')
        print('>>> x //= y')
        print('>>> x')
        x = b"This is another string of bytes"
        y = bytearray(1)
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x //= y')
        print('>>> x')
        x = b"This is another string of bytes"
        y = bytearray([1, 2, 3])
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()