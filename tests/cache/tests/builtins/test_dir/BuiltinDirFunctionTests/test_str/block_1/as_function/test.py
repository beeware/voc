def test_function():
    try:
        print('>>> f = dir')
        print('>>> x = ""')
        print('>>> f(x)')
        f = dir
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dir')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = dir
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dir')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = dir
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dir')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = dir
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dir')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = dir
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dir')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = dir
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()