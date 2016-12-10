def test_function():
    try:
        print('>>> f = property')
        print('>>> x = ""')
        print('>>> f(x)')
        f = property
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = property')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = property
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = property')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = property
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = property')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = property
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = property')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = property
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = property')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = property
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()