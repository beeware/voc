def test_function():
    try:
        print('>>> f = isinstance')
        print('>>> x = ""')
        print('>>> f(x)')
        f = isinstance
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = isinstance')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = isinstance
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = isinstance')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = isinstance
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = isinstance')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = isinstance
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = isinstance')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = isinstance
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = isinstance')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = isinstance
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()