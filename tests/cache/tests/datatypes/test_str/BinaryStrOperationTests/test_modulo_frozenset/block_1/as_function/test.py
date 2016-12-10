def test_function():
    try:
        print('>>> x = ""')
        print('>>> y = frozenset()')
        print('>>> x % y')
        x = ""
        y = frozenset()
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ""')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x % y')
        x = ""
        y = frozenset({1, 2.3456, "another"})
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = frozenset()')
        print('>>> x % y')
        x = "3"
        y = frozenset()
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x % y')
        x = "3"
        y = frozenset({1, 2.3456, "another"})
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = frozenset()')
        print('>>> x % y')
        x = "This is another string"
        y = frozenset()
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x % y')
        x = "This is another string"
        y = frozenset({1, 2.3456, "another"})
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = frozenset()')
        print('>>> x % y')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = frozenset()
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x % y')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = frozenset({1, 2.3456, "another"})
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = frozenset()')
        print('>>> x % y')
        x = "One arg: %s"
        y = frozenset()
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x % y')
        x = "One arg: %s"
        y = frozenset({1, 2.3456, "another"})
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = frozenset()')
        print('>>> x % y')
        x = "Three args: %s | %s | %s"
        y = frozenset()
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x % y')
        x = "Three args: %s | %s | %s"
        y = frozenset({1, 2.3456, "another"})
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()