def test_function():
    try:
        print('>>> f = map')
        print('>>> x = ""')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = map
        x = ""
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = ""')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = map
        x = ""
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "3"')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = map
        x = "3"
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "3"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = map
        x = "3"
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "This is another string"')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = map
        x = "This is another string"
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "This is another string"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = map
        x = "This is another string"
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = map
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = map
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "One arg: %s"')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = map
        x = "One arg: %s"
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "One arg: %s"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = map
        x = "One arg: %s"
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = map
        x = "Three args: %s | %s | %s"
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = map
        x = "Three args: %s | %s | %s"
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()