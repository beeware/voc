def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = ""')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = delattr
        x = ""
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "3"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = delattr
        x = "3"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "This is another string"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = delattr
        x = "This is another string"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = delattr
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "One arg: %s"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = delattr
        x = "One arg: %s"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = delattr
        x = "Three args: %s | %s | %s"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()