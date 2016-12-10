def test_function():
    try:
        print('>>> x = ""')
        print('>>> y = frozenset()')
        print('>>> x -= y')
        print('>>> x')
        x = ""
        y = frozenset()
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ""')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x -= y')
        print('>>> x')
        x = ""
        y = frozenset({1, 2.3456, "another"})
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = frozenset()')
        print('>>> x -= y')
        print('>>> x')
        x = "3"
        y = frozenset()
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x -= y')
        print('>>> x')
        x = "3"
        y = frozenset({1, 2.3456, "another"})
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = frozenset()')
        print('>>> x -= y')
        print('>>> x')
        x = "This is another string"
        y = frozenset()
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x -= y')
        print('>>> x')
        x = "This is another string"
        y = frozenset({1, 2.3456, "another"})
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = frozenset()')
        print('>>> x -= y')
        print('>>> x')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = frozenset()
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x -= y')
        print('>>> x')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = frozenset({1, 2.3456, "another"})
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = frozenset()')
        print('>>> x -= y')
        print('>>> x')
        x = "One arg: %s"
        y = frozenset()
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x -= y')
        print('>>> x')
        x = "One arg: %s"
        y = frozenset({1, 2.3456, "another"})
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = frozenset()')
        print('>>> x -= y')
        print('>>> x')
        x = "Three args: %s | %s | %s"
        y = frozenset()
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x -= y')
        print('>>> x')
        x = "Three args: %s | %s | %s"
        y = frozenset({1, 2.3456, "another"})
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()