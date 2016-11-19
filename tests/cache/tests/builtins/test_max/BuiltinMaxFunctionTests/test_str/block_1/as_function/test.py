def test_function():
    try:
        print('>>> f = max')
        print('>>> x = ""')
        print('>>> f(x)')
        f = max
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = max')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = max
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = max')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = max
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = max')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = max
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = max')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = max
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = max')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = max
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()