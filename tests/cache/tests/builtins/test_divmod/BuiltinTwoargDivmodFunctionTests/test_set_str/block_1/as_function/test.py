def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = set()')
        print('>>> y = ""')
        print('>>> f(x, y)')
        f = divmod
        x = set()
        y = ""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = set()')
        print('>>> y = "3"')
        print('>>> f(x, y)')
        f = divmod
        x = set()
        y = "3"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = set()')
        print('>>> y = "This is another string"')
        print('>>> f(x, y)')
        f = divmod
        x = set()
        y = "This is another string"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = set()')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x, y)')
        f = divmod
        x = set()
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = set()')
        print('>>> y = "One arg: %s"')
        print('>>> f(x, y)')
        f = divmod
        x = set()
        y = "One arg: %s"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = set()')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> f(x, y)')
        f = divmod
        x = set()
        y = "Three args: %s | %s | %s"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = ""')
        print('>>> f(x, y)')
        f = divmod
        x = {1, 2.3456, "another"}
        y = ""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = "3"')
        print('>>> f(x, y)')
        f = divmod
        x = {1, 2.3456, "another"}
        y = "3"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = "This is another string"')
        print('>>> f(x, y)')
        f = divmod
        x = {1, 2.3456, "another"}
        y = "This is another string"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x, y)')
        f = divmod
        x = {1, 2.3456, "another"}
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = "One arg: %s"')
        print('>>> f(x, y)')
        f = divmod
        x = {1, 2.3456, "another"}
        y = "One arg: %s"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> f(x, y)')
        f = divmod
        x = {1, 2.3456, "another"}
        y = "Three args: %s | %s | %s"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()