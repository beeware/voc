def test_function():
    try:
        print('>>> f = map')
        print('>>> x = b""')
        print('>>> y = range(0)')
        print('>>> f(x, y)')
        f = map
        x = b""
        y = range(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = b""')
        print('>>> y = range(5)')
        print('>>> f(x, y)')
        f = map
        x = b""
        y = range(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = b""')
        print('>>> y = range(2, 7)')
        print('>>> f(x, y)')
        f = map
        x = b""
        y = range(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = b""')
        print('>>> y = range(2, 7, 2)')
        print('>>> f(x, y)')
        f = map
        x = b""
        y = range(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = b""')
        print('>>> y = range(7, 2, -1)')
        print('>>> f(x, y)')
        f = map
        x = b""
        y = range(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = b""')
        print('>>> y = range(7, 2, -2)')
        print('>>> f(x, y)')
        f = map
        x = b""
        y = range(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = range(0)')
        print('>>> f(x, y)')
        f = map
        x = b"This is another string of bytes"
        y = range(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = range(5)')
        print('>>> f(x, y)')
        f = map
        x = b"This is another string of bytes"
        y = range(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = range(2, 7)')
        print('>>> f(x, y)')
        f = map
        x = b"This is another string of bytes"
        y = range(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = range(2, 7, 2)')
        print('>>> f(x, y)')
        f = map
        x = b"This is another string of bytes"
        y = range(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = range(7, 2, -1)')
        print('>>> f(x, y)')
        f = map
        x = b"This is another string of bytes"
        y = range(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = range(7, 2, -2)')
        print('>>> f(x, y)')
        f = map
        x = b"This is another string of bytes"
        y = range(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()