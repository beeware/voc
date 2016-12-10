def test_function():
    try:
        print('>>> x = ""')
        print('>>> y = NotImplemented')
        print('>>> x <= y')
        x = ""
        y = NotImplemented
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = NotImplemented')
        print('>>> x <= y')
        x = "3"
        y = NotImplemented
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = NotImplemented')
        print('>>> x <= y')
        x = "This is another string"
        y = NotImplemented
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = NotImplemented')
        print('>>> x <= y')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = NotImplemented
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = NotImplemented')
        print('>>> x <= y')
        x = "One arg: %s"
        y = NotImplemented
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = NotImplemented')
        print('>>> x <= y')
        x = "Three args: %s | %s | %s"
        y = NotImplemented
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()