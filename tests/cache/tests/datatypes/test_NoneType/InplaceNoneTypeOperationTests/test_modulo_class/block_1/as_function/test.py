def test_function():
    try:
        print('>>> x = None')
        print('>>> y = type(1)')
        print('>>> x %= y')
        print('>>> x')
        x = None
        y = type(1)
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = type("a")')
        print('>>> x %= y')
        print('>>> x')
        x = None
        y = type("a")
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = type(object())')
        print('>>> x %= y')
        print('>>> x')
        x = None
        y = type(object())
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x %= y')
        print('>>> x')
        x = None
        y = type("MyClass", (object,), {})
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()