def test_function():
    try:
        print('>>> f = str')
        print('>>> x = ""')
        print('>>> f(x)')
        f = str
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = str')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = str
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = str')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = str
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = str')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = str
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = str')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = str
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = str')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = str
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()