def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = ""')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = ""
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = ""')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = ""
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "3"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = "3"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "3"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = "3"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "This is another string"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = "This is another string"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "This is another string"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = "This is another string"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "One arg: %s"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = "One arg: %s"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "One arg: %s"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = "One arg: %s"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = "Three args: %s | %s | %s"
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = "Three args: %s | %s | %s"
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()