def test_function():
    try:
        print('>>> x = b""')
        print('>>> y = b""')
        print('>>> x ^= y')
        print('>>> x')
        x = b""
        y = b""
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = b"This is another string of bytes"')
        print('>>> x ^= y')
        print('>>> x')
        x = b""
        y = b"This is another string of bytes"
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = b""')
        print('>>> x ^= y')
        print('>>> x')
        x = b"This is another string of bytes"
        y = b""
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = b"This is another string of bytes"')
        print('>>> x ^= y')
        print('>>> x')
        x = b"This is another string of bytes"
        y = b"This is another string of bytes"
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()