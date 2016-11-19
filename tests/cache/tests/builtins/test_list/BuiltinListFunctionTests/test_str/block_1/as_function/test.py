def test_function():
    try:
        print('>>> f = list')
        print('>>> x = ""')
        print('>>> f(x)')
        f = list
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = list')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = list
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = list')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = list
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = list')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = list
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = list')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = list
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = list')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = list
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()