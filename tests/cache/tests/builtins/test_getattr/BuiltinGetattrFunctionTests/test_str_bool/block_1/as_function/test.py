def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = ""')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = ""
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = ""')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = ""
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "3"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = "3"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "3"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = "3"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "This is another string"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = "This is another string"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "This is another string"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = "This is another string"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "One arg: %s"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = "One arg: %s"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "One arg: %s"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = "One arg: %s"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = "Three args: %s | %s | %s"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = "Three args: %s | %s | %s"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()