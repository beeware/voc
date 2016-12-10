def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = ""')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = ""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = "3"')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = "3"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = "This is another string"')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = "This is another string"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = "One arg: %s"')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = "One arg: %s"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = "Three args: %s | %s | %s"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = ""')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = ""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = "3"')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = "3"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = "This is another string"')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = "This is another string"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = "One arg: %s"')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = "One arg: %s"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = "Three args: %s | %s | %s"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()