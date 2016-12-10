def test_function():
    try:
        print('>>> x = b""')
        print('>>> y = slice(0)')
        print('>>> x << y')
        x = b""
        y = slice(0)
        print(x << y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = slice(5)')
        print('>>> x << y')
        x = b""
        y = slice(5)
        print(x << y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = slice(2, 7)')
        print('>>> x << y')
        x = b""
        y = slice(2, 7)
        print(x << y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x << y')
        x = b""
        y = slice(2, 7, 2)
        print(x << y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x << y')
        x = b""
        y = slice(7, 2, -1)
        print(x << y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x << y')
        x = b""
        y = slice(7, 2, -2)
        print(x << y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = slice(0)')
        print('>>> x << y')
        x = b"This is another string of bytes"
        y = slice(0)
        print(x << y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = slice(5)')
        print('>>> x << y')
        x = b"This is another string of bytes"
        y = slice(5)
        print(x << y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = slice(2, 7)')
        print('>>> x << y')
        x = b"This is another string of bytes"
        y = slice(2, 7)
        print(x << y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x << y')
        x = b"This is another string of bytes"
        y = slice(2, 7, 2)
        print(x << y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x << y')
        x = b"This is another string of bytes"
        y = slice(7, 2, -1)
        print(x << y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x << y')
        x = b"This is another string of bytes"
        y = slice(7, 2, -2)
        print(x << y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()