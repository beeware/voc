def test_function():
    try:
        print('>>> f = classmethod')
        print('>>> x = ""')
        print('>>> f(x)')
        f = classmethod
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = classmethod')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = classmethod
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = classmethod')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = classmethod
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = classmethod')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = classmethod
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = classmethod')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = classmethod
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = classmethod')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = classmethod
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()