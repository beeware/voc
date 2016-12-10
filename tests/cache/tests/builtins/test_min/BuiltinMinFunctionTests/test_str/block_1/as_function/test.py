def test_function():
    try:
        print('>>> f = min')
        print('>>> x = ""')
        print('>>> f(x)')
        f = min
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = min')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = min
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = min')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = min
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = min')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = min
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = min')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = min
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = min')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = min
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()