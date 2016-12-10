def test_function():
    try:
        print('>>> f = reversed')
        print('>>> x = ""')
        print('>>> f(x)')
        f = reversed
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = reversed')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = reversed
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = reversed')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = reversed
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = reversed')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = reversed
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = reversed')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = reversed
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = reversed')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = reversed
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()