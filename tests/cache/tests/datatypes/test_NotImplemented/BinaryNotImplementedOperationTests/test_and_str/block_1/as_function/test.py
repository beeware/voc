def test_function():
    try:
        print('>>> x = NotImplemented')
        print('>>> y = ""')
        print('>>> x & y')
        x = NotImplemented
        y = ""
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = "3"')
        print('>>> x & y')
        x = NotImplemented
        y = "3"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = "This is another string"')
        print('>>> x & y')
        x = NotImplemented
        y = "This is another string"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x & y')
        x = NotImplemented
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = "One arg: %s"')
        print('>>> x & y')
        x = NotImplemented
        y = "One arg: %s"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x & y')
        x = NotImplemented
        y = "Three args: %s | %s | %s"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()