def test_function():
    try:
        print('>>> x = None')
        print('>>> y = type(1)')
        print('>>> x / y')
        x = None
        y = type(1)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = type("a")')
        print('>>> x / y')
        x = None
        y = type("a")
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = type(object())')
        print('>>> x / y')
        x = None
        y = type(object())
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x / y')
        x = None
        y = type("MyClass", (object,), {})
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()