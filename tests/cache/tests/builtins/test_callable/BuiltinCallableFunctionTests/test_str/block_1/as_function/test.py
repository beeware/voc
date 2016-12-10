def test_function():
    try:
        print('>>> f = callable')
        print('>>> x = ""')
        print('>>> f(x)')
        f = callable
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = callable')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = callable
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = callable')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = callable
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = callable')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = callable
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = callable')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = callable
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = callable')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = callable
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()