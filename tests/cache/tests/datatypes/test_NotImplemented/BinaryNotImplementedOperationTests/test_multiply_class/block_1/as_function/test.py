def test_function():
    try:
        print('>>> x = NotImplemented')
        print('>>> y = type(1)')
        print('>>> x * y')
        x = NotImplemented
        y = type(1)
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = type("a")')
        print('>>> x * y')
        x = NotImplemented
        y = type("a")
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = type(object())')
        print('>>> x * y')
        x = NotImplemented
        y = type(object())
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x * y')
        x = NotImplemented
        y = type("MyClass", (object,), {})
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()