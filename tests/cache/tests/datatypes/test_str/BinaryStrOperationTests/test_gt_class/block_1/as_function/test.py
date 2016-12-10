def test_function():
    try:
        print('>>> x = ""')
        print('>>> y = type(1)')
        print('>>> x > y')
        x = ""
        y = type(1)
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ""')
        print('>>> y = type("a")')
        print('>>> x > y')
        x = ""
        y = type("a")
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ""')
        print('>>> y = type(object())')
        print('>>> x > y')
        x = ""
        y = type(object())
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ""')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x > y')
        x = ""
        y = type("MyClass", (object,), {})
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = type(1)')
        print('>>> x > y')
        x = "3"
        y = type(1)
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = type("a")')
        print('>>> x > y')
        x = "3"
        y = type("a")
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = type(object())')
        print('>>> x > y')
        x = "3"
        y = type(object())
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "3"')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x > y')
        x = "3"
        y = type("MyClass", (object,), {})
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = type(1)')
        print('>>> x > y')
        x = "This is another string"
        y = type(1)
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = type("a")')
        print('>>> x > y')
        x = "This is another string"
        y = type("a")
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = type(object())')
        print('>>> x > y')
        x = "This is another string"
        y = type(object())
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "This is another string"')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x > y')
        x = "This is another string"
        y = type("MyClass", (object,), {})
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = type(1)')
        print('>>> x > y')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = type(1)
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = type("a")')
        print('>>> x > y')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = type("a")
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = type(object())')
        print('>>> x > y')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = type(object())
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x > y')
        x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
        y = type("MyClass", (object,), {})
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = type(1)')
        print('>>> x > y')
        x = "One arg: %s"
        y = type(1)
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = type("a")')
        print('>>> x > y')
        x = "One arg: %s"
        y = type("a")
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = type(object())')
        print('>>> x > y')
        x = "One arg: %s"
        y = type(object())
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "One arg: %s"')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x > y')
        x = "One arg: %s"
        y = type("MyClass", (object,), {})
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = type(1)')
        print('>>> x > y')
        x = "Three args: %s | %s | %s"
        y = type(1)
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = type("a")')
        print('>>> x > y')
        x = "Three args: %s | %s | %s"
        y = type("a")
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = type(object())')
        print('>>> x > y')
        x = "Three args: %s | %s | %s"
        y = type(object())
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = "Three args: %s | %s | %s"')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x > y')
        x = "Three args: %s | %s | %s"
        y = type("MyClass", (object,), {})
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()