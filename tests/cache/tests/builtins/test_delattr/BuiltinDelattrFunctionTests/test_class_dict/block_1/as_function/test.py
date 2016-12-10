def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = type(1)')
        print('>>> y = {}')
        print('>>> f(x, y)')
        f = delattr
        x = type(1)
        y = {}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type(1)')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> f(x, y)')
        f = delattr
        x = type(1)
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type("a")')
        print('>>> y = {}')
        print('>>> f(x, y)')
        f = delattr
        x = type("a")
        y = {}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type("a")')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> f(x, y)')
        f = delattr
        x = type("a")
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type(object())')
        print('>>> y = {}')
        print('>>> f(x, y)')
        f = delattr
        x = type(object())
        y = {}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type(object())')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> f(x, y)')
        f = delattr
        x = type(object())
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = {}')
        print('>>> f(x, y)')
        f = delattr
        x = type("MyClass", (object,), {})
        y = {}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> f(x, y)')
        f = delattr
        x = type("MyClass", (object,), {})
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()