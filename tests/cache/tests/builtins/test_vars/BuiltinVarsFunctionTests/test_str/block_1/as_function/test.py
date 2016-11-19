def test_function():
    try:
        print('>>> f = vars')
        print('>>> x = ""')
        print('>>> f(x)')
        f = vars
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = vars')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = vars
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = vars')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = vars
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = vars')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = vars
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = vars')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = vars
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = vars')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = vars
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()