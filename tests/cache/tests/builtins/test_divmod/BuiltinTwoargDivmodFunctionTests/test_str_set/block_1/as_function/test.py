def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = ""')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = divmod
        x = ""
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = ""')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = divmod
        x = ""
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "3"')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = divmod
        x = "3"
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "3"')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = divmod
        x = "3"
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "This is another string"')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = divmod
        x = "This is another string"
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "This is another string"')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = divmod
        x = "This is another string"
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = divmod
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = divmod
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "One arg: %s"')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = divmod
        x = "One arg: %s"
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "One arg: %s"')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = divmod
        x = "One arg: %s"
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = divmod
        x = "Three args: %s | %s | %s"
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = divmod
        x = "Three args: %s | %s | %s"
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()