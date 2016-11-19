def test_function():
    try:
        print('>>> x = set()')
        print('>>> y = ""')
        print('>>> x **= y')
        print('>>> x')
        x = set()
        y = ""
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = "3"')
        print('>>> x **= y')
        print('>>> x')
        x = set()
        y = "3"
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = "This is another string"')
        print('>>> x **= y')
        print('>>> x')
        x = set()
        y = "This is another string"
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x **= y')
        print('>>> x')
        x = set()
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = "One arg: %s"')
        print('>>> x **= y')
        print('>>> x')
        x = set()
        y = "One arg: %s"
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x **= y')
        print('>>> x')
        x = set()
        y = "Three args: %s | %s | %s"
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = ""')
        print('>>> x **= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = ""
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = "3"')
        print('>>> x **= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = "3"
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = "This is another string"')
        print('>>> x **= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = "This is another string"
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> x **= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = "One arg: %s"')
        print('>>> x **= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = "One arg: %s"
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = "Three args: %s | %s | %s"')
        print('>>> x **= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = "Three args: %s | %s | %s"
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()