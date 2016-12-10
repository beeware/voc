def test_function():
    try:
        print('>>> f = set')
        print('>>> x = ""')
        print('>>> f(x)')
        f = set
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = set')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = set
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = set')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = set
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = set')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = set
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = set')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = set
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = set')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = set
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()