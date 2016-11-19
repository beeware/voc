def test_function():
    try:
        print('>>> f = len')
        print('>>> x = ""')
        print('>>> f(x)')
        f = len
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = len')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = len
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = len')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = len
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = len')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = len
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = len')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = len
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = len')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = len
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()