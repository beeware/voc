def test_function():
    try:
        print('>>> f = issubclass')
        print('>>> x = ""')
        print('>>> f(x)')
        f = issubclass
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = issubclass')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = issubclass
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = issubclass')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = issubclass
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = issubclass')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = issubclass
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = issubclass')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = issubclass
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = issubclass')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = issubclass
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()