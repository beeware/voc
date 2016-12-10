def test_function():
    try:
        print('>>> x = {}')
        print('>>> y = ""')
        print('>>> x & y')
        x = {}
        y = ""
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = "3"')
        print('>>> x & y')
        x = {}
        y = "3"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = "This is another string"')
        print('>>> x & y')
        x = {}
        y = "This is another string"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x & y')
        x = {}
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = "One arg: %s"')
        print('>>> x & y')
        x = {}
        y = "One arg: %s"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x & y')
        x = {}
        y = "Three args: %s | %s | %s"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = ""')
        print('>>> x & y')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = ""
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = "3"')
        print('>>> x & y')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = "3"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = "This is another string"')
        print('>>> x & y')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = "This is another string"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x & y')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = "One arg: %s"')
        print('>>> x & y')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = "One arg: %s"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x & y')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = "Three args: %s | %s | %s"
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()