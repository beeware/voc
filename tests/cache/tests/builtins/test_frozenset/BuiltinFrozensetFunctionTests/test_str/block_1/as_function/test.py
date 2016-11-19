def test_function():
    try:
        print('>>> f = frozenset')
        print('>>> x = ""')
        print('>>> f(x)')
        f = frozenset
        x = ""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = frozenset')
        print('>>> x = "3"')
        print('>>> f(x)')
        f = frozenset
        x = "3"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = frozenset')
        print('>>> x = "This is another string"')
        print('>>> f(x)')
        f = frozenset
        x = "This is another string"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = frozenset')
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> f(x)')
        f = frozenset
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = frozenset')
        print('>>> x = "One arg: %s"')
        print('>>> f(x)')
        f = frozenset
        x = "One arg: %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = frozenset')
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> f(x)')
        f = frozenset
        x = "Three args: %s | %s | %s"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()