def test_function():
    try:
        print('>>> x = b""')
        print('>>> y = (1, 2)')
        print('>>> x += y')
        print('>>> x')
        x = b""
        y = (1, 2)
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> x += y')
        print('>>> x')
        x = b""
        y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = (3, 1.2, True, )')
        print('>>> x += y')
        print('>>> x')
        x = b""
        y = (3, 1.2, True, )
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = (1, 2.3456, "another")')
        print('>>> x += y')
        print('>>> x')
        x = b""
        y = (1, 2.3456, "another")
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = (1, 2)')
        print('>>> x += y')
        print('>>> x')
        x = b"This is another string of bytes"
        y = (1, 2)
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> x += y')
        print('>>> x')
        x = b"This is another string of bytes"
        y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = (3, 1.2, True, )')
        print('>>> x += y')
        print('>>> x')
        x = b"This is another string of bytes"
        y = (3, 1.2, True, )
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = (1, 2.3456, "another")')
        print('>>> x += y')
        print('>>> x')
        x = b"This is another string of bytes"
        y = (1, 2.3456, "another")
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()