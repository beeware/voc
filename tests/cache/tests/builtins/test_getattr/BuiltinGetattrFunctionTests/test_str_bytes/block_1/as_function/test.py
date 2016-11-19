def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = ""')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = getattr
        x = ""
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = ""')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = getattr
        x = ""
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "3"')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = getattr
        x = "3"
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "3"')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = getattr
        x = "3"
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "This is another string"')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = getattr
        x = "This is another string"
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "This is another string"')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = getattr
        x = "This is another string"
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = getattr
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = getattr
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "One arg: %s"')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = getattr
        x = "One arg: %s"
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "One arg: %s"')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = getattr
        x = "One arg: %s"
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = getattr
        x = "Three args: %s | %s | %s"
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = getattr
        x = "Three args: %s | %s | %s"
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()