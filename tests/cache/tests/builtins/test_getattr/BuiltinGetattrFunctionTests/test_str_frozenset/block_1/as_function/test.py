def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = ""')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = getattr
        x = ""
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = ""')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = getattr
        x = ""
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "3"')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = getattr
        x = "3"
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "3"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = getattr
        x = "3"
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "This is another string"')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = getattr
        x = "This is another string"
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "This is another string"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = getattr
        x = "This is another string"
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = getattr
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = getattr
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "One arg: %s"')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = getattr
        x = "One arg: %s"
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "One arg: %s"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = getattr
        x = "One arg: %s"
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = getattr
        x = "Three args: %s | %s | %s"
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = getattr
        x = "Three args: %s | %s | %s"
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()