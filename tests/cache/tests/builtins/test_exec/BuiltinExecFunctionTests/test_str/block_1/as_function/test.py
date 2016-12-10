def test_function():
    try:
        print('>>> f = exec')
        print('>>> x = ""')
        print('>>> f(x)')
        f = exec
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = exec')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = exec
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = exec')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = exec
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = exec')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = exec
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = exec')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = exec
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = exec')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = exec
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()