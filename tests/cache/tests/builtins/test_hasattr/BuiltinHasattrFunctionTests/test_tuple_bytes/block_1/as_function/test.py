def test_function():
    try:
        print('>>> f = hasattr')
        print('>>> x = (1, 2)')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = hasattr
        x = (1, 2)
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = (1, 2)')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = hasattr
        x = (1, 2)
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = hasattr
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = hasattr
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = hasattr
        x = (3, 1.2, True, )
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = hasattr
        x = (3, 1.2, True, )
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = hasattr
        x = (1, 2.3456, "another")
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = hasattr
        x = (1, 2.3456, "another")
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()