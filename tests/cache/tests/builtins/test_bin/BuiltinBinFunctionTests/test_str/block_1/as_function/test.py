def test_function():
    try:
        print('>>> f = bin')
        print('>>> x = ""')
        print('>>> f(x)')
        f = bin
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bin')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = bin
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bin')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = bin
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bin')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = bin
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bin')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = bin
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bin')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = bin
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()