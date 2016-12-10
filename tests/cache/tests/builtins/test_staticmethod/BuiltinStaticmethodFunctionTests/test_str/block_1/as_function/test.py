def test_function():
    try:
        print('>>> f = staticmethod')
        print('>>> x = ""')
        print('>>> f(x)')
        f = staticmethod
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = staticmethod')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = staticmethod
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = staticmethod')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = staticmethod
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = staticmethod')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = staticmethod
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = staticmethod')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = staticmethod
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = staticmethod')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = staticmethod
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()