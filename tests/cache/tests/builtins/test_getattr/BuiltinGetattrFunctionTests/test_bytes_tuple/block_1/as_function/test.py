def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = b""')
        print('>>> y = (1, 2)')
        print('>>> f(x, y)')
        f = getattr
        x = b""
        y = (1, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = b""')
        print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> f(x, y)')
        f = getattr
        x = b""
        y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = b""')
        print('>>> y = (3, 1.2, True, )')
        print('>>> f(x, y)')
        f = getattr
        x = b""
        y = (3, 1.2, True, )
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = b""')
        print('>>> y = (1, 2.3456, "another")')
        print('>>> f(x, y)')
        f = getattr
        x = b""
        y = (1, 2.3456, "another")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = (1, 2)')
        print('>>> f(x, y)')
        f = getattr
        x = b"This is another string of bytes"
        y = (1, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> f(x, y)')
        f = getattr
        x = b"This is another string of bytes"
        y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = (3, 1.2, True, )')
        print('>>> f(x, y)')
        f = getattr
        x = b"This is another string of bytes"
        y = (3, 1.2, True, )
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = (1, 2.3456, "another")')
        print('>>> f(x, y)')
        f = getattr
        x = b"This is another string of bytes"
        y = (1, 2.3456, "another")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()