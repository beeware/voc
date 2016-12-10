def test_function():
    try:
        print('>>> x = b""')
        print('>>> y = bytearray()')
        print('>>> x <= y')
        x = b""
        y = bytearray()
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = bytearray(1)')
        print('>>> x <= y')
        x = b""
        y = bytearray(1)
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x <= y')
        x = b""
        y = bytearray([1, 2, 3])
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = bytearray()')
        print('>>> x <= y')
        x = b"This is another string of bytes"
        y = bytearray()
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = bytearray(1)')
        print('>>> x <= y')
        x = b"This is another string of bytes"
        y = bytearray(1)
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x <= y')
        x = b"This is another string of bytes"
        y = bytearray([1, 2, 3])
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()