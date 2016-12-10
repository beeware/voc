def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = ""')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = delattr
        x = ""
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = ""')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = delattr
        x = ""
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "3"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = delattr
        x = "3"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "3"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = delattr
        x = "3"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "This is another string"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = delattr
        x = "This is another string"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "This is another string"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = delattr
        x = "This is another string"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = delattr
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = delattr
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "One arg: %s"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = delattr
        x = "One arg: %s"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "One arg: %s"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = delattr
        x = "One arg: %s"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = delattr
        x = "Three args: %s | %s | %s"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = delattr
        x = "Three args: %s | %s | %s"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()