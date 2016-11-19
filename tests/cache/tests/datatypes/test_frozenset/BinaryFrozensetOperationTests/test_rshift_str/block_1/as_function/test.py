def test_function():
    try:
        print('>>> x = frozenset()')
        print('>>> y = ""')
        print('>>> x >> y')
        x = frozenset()
        y = ""
        print(x >> y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = "3"')
        print('>>> x >> y')
        x = frozenset()
        y = "3"
        print(x >> y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = "This is another string"')
        print('>>> x >> y')
        x = frozenset()
        y = "This is another string"
        print(x >> y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x >> y')
        x = frozenset()
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(x >> y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = "One arg: %s"')
        print('>>> x >> y')
        x = frozenset()
        y = "One arg: %s"
        print(x >> y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x >> y')
        x = frozenset()
        y = "Three args: %s | %s | %s"
        print(x >> y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = ""')
        print('>>> x >> y')
        x = frozenset({1, 2.3456, "another"})
        y = ""
        print(x >> y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = "3"')
        print('>>> x >> y')
        x = frozenset({1, 2.3456, "another"})
        y = "3"
        print(x >> y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = "This is another string"')
        print('>>> x >> y')
        x = frozenset({1, 2.3456, "another"})
        y = "This is another string"
        print(x >> y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x >> y')
        x = frozenset({1, 2.3456, "another"})
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(x >> y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = "One arg: %s"')
        print('>>> x >> y')
        x = frozenset({1, 2.3456, "another"})
        y = "One arg: %s"
        print(x >> y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x >> y')
        x = frozenset({1, 2.3456, "another"})
        y = "Three args: %s | %s | %s"
        print(x >> y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()