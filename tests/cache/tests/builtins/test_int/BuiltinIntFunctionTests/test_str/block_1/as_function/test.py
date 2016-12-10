def test_function():
    try:
        print('>>> f = int')
        print('>>> x = ""')
        print('>>> f(x)')
        f = int
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = int')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = int
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = int')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = int
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = int')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = int
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = int')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = int
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = int')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = int
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()