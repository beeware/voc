def test_function():
    try:
        print('>>> x = bytearray()')
        print('>>> y = b""')
        print('>>> x |= y')
        print('>>> x')
        x = bytearray()
        y = b""
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray()')
        print('>>> y = b"This is another string of bytes"')
        print('>>> x |= y')
        print('>>> x')
        x = bytearray()
        y = b"This is another string of bytes"
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = b""')
        print('>>> x |= y')
        print('>>> x')
        x = bytearray(1)
        y = b""
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = b"This is another string of bytes"')
        print('>>> x |= y')
        print('>>> x')
        x = bytearray(1)
        y = b"This is another string of bytes"
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = b""')
        print('>>> x |= y')
        print('>>> x')
        x = bytearray([1, 2, 3])
        y = b""
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = b"This is another string of bytes"')
        print('>>> x |= y')
        print('>>> x')
        x = bytearray([1, 2, 3])
        y = b"This is another string of bytes"
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()