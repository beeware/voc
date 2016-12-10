def test_function():
    try:
        print('>>> x = {}')
        print('>>> y = type(1)')
        print('>>> x >>= y')
        print('>>> x')
        x = {}
        y = type(1)
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = type("a")')
        print('>>> x >>= y')
        print('>>> x')
        x = {}
        y = type("a")
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = type(object())')
        print('>>> x >>= y')
        print('>>> x')
        x = {}
        y = type(object())
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x >>= y')
        print('>>> x')
        x = {}
        y = type("MyClass", (object,), {})
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = type(1)')
        print('>>> x >>= y')
        print('>>> x')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = type(1)
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = type("a")')
        print('>>> x >>= y')
        print('>>> x')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = type("a")
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = type(object())')
        print('>>> x >>= y')
        print('>>> x')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = type(object())
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x >>= y')
        print('>>> x')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = type("MyClass", (object,), {})
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()