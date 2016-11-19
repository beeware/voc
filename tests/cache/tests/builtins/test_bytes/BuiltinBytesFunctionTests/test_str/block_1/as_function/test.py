def test_function():
    try:
        print('>>> f = bytes')
        print('>>> x = ""')
        print('>>> f(x)')
        f = bytes
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bytes')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = bytes
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bytes')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = bytes
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bytes')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = bytes
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bytes')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = bytes
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bytes')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = bytes
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()