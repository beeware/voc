def test_function():
    try:
        print('>>> f = bool')
        print('>>> x = ""')
        print('>>> f(x)')
        f = bool
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bool')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = bool
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bool')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = bool
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bool')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = bool
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bool')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = bool
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bool')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = bool
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()