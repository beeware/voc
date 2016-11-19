def test_function():
    try:
        print('>>> f = dict')
        print('>>> x = ""')
        print('>>> f(x)')
        f = dict
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dict')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = dict
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dict')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = dict
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dict')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = dict
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dict')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = dict
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dict')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = dict
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()