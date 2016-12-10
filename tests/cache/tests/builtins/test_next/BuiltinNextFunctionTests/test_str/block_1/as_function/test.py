def test_function():
    try:
        print('>>> f = next')
        print('>>> x = ""')
        print('>>> f(x)')
        f = next
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = next')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = next
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = next')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = next
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = next')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = next
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = next')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = next
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = next')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = next
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()