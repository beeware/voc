def test_function():
    try:
        print('>>> x = b""')
        print('>>> y = ""')
        print('>>> x < y')
        x = b""
        y = ""
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = "3"')
        print('>>> x < y')
        x = b""
        y = "3"
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = "This is another string"')
        print('>>> x < y')
        x = b""
        y = "This is another string"
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x < y')
        x = b""
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = "One arg: %s"')
        print('>>> x < y')
        x = b""
        y = "One arg: %s"
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x < y')
        x = b""
        y = "Three args: %s | %s | %s"
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = ""')
        print('>>> x < y')
        x = b"This is another string of bytes"
        y = ""
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = "3"')
        print('>>> x < y')
        x = b"This is another string of bytes"
        y = "3"
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = "This is another string"')
        print('>>> x < y')
        x = b"This is another string of bytes"
        y = "This is another string"
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x < y')
        x = b"This is another string of bytes"
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = "One arg: %s"')
        print('>>> x < y')
        x = b"This is another string of bytes"
        y = "One arg: %s"
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x < y')
        x = b"This is another string of bytes"
        y = "Three args: %s | %s | %s"
        print(x < y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()