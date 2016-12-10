def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = {}')
        print('>>> y = ""')
        print('>>> f(x, y)')
        f = getattr
        x = {}
        y = ""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {}')
        print('>>> y = "3"')
        print('>>> f(x, y)')
        f = getattr
        x = {}
        y = "3"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {}')
        print('>>> y = "This is another string"')
        print('>>> f(x, y)')
        f = getattr
        x = {}
        y = "This is another string"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {}')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x, y)')
        f = getattr
        x = {}
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {}')
        print('>>> y = "One arg: %s"')
        print('>>> f(x, y)')
        f = getattr
        x = {}
        y = "One arg: %s"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {}')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> f(x, y)')
        f = getattr
        x = {}
        y = "Three args: %s | %s | %s"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = ""')
        print('>>> f(x, y)')
        f = getattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = ""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = "3"')
        print('>>> f(x, y)')
        f = getattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = "3"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = "This is another string"')
        print('>>> f(x, y)')
        f = getattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = "This is another string"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x, y)')
        f = getattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = "One arg: %s"')
        print('>>> f(x, y)')
        f = getattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = "One arg: %s"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> f(x, y)')
        f = getattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = "Three args: %s | %s | %s"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()