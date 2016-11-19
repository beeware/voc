def test_function():
    try:
        print('>>> f = ord')
        print('>>> x = ""')
        print('>>> f(x)')
        f = ord
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = ord')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = ord
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = ord')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = ord
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = ord')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = ord
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = ord')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = ord
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = ord')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = ord
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()