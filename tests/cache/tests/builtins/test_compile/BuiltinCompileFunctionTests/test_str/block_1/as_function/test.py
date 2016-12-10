def test_function():
    try:
        print('>>> f = compile')
        print('>>> x = ""')
        print('>>> f(x)')
        f = compile
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = compile
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = compile
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = compile
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = compile
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = compile
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()