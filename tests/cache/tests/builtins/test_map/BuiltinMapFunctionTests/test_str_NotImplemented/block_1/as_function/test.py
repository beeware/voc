def test_function():
    try:
        print('>>> f = map')
        print('>>> x = ""')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = map
        x = ""
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "3"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = map
        x = "3"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "This is another string"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = map
        x = "This is another string"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = map
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "One arg: %s"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = map
        x = "One arg: %s"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = map
        x = "Three args: %s | %s | %s"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()