def test_function():
    try:
        print('>>> f = globals')
        print('>>> x = ""')
        print('>>> f(x)')
        f = globals
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = globals')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = globals
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = globals')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = globals
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = globals')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = globals
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = globals')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = globals
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = globals')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = globals
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()