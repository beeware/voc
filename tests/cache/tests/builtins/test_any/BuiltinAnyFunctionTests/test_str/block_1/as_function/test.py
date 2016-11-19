def test_function():
    try:
        print('>>> f = any')
        print('>>> x = ""')
        print('>>> f(x)')
        f = any
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = any')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = any
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = any')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = any
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = any')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = any
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = any')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = any
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = any')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = any
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()