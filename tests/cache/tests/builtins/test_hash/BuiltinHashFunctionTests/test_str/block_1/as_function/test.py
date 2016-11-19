def test_function():
    try:
        print('>>> f = hash')
        print('>>> x = ""')
        print('>>> f(x)')
        f = hash
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hash')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = hash
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hash')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = hash
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hash')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = hash
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hash')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = hash
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hash')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = hash
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()