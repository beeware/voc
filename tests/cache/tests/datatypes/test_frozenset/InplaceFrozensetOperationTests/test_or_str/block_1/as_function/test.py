def test_function():
    try:
        print('>>> x = frozenset()')
        print('>>> y = ""')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset()
        y = ""
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = "3"')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset()
        y = "3"
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = "This is another string"')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset()
        y = "This is another string"
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset()
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = "One arg: %s"')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset()
        y = "One arg: %s"
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset()
        y = "Three args: %s | %s | %s"
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = ""')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = ""
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = "3"')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = "3"
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = "This is another string"')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = "This is another string"
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = "One arg: %s"')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = "One arg: %s"
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = "Three args: %s | %s | %s"
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()