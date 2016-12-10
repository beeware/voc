def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = 1j')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = delattr
        x = 1j
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = 1j')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = delattr
        x = 1j
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = 3.14159265j')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = delattr
        x = 3.14159265j
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = 3.14159265j')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = delattr
        x = 3.14159265j
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = 1+2j')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = delattr
        x = 1+2j
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = 1+2j')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = delattr
        x = 1+2j
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = 3-4j')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = delattr
        x = 3-4j
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = 3-4j')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = delattr
        x = 3-4j
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = -5j')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = delattr
        x = -5j
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = -5j')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = delattr
        x = -5j
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()