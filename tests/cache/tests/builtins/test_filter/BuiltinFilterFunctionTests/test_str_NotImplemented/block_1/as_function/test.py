def test_function():
    try:
        print('>>> f = filter')
        print('>>> x = ""')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = ""
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = "3"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = "3"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = "This is another string"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = "This is another string"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = "One arg: %s"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = "One arg: %s"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = "Three args: %s | %s | %s"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()