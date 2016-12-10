def test_function():
    try:
        print('>>> f = abs')
        print('>>> x = ""')
        print('>>> f(x)')
        f = abs
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = abs')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = abs
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = abs')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = abs
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = abs')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = abs
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = abs')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = abs
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = abs')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = abs
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()