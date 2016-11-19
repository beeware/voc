def test_function():
    try:
        print('>>> f = map')
        print('>>> x = type(1)')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = map
        x = type(1)
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = type(1)')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = map
        x = type(1)
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = type("a")')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = map
        x = type("a")
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = type("a")')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = map
        x = type("a")
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = type(object())')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = map
        x = type(object())
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = type(object())')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = map
        x = type(object())
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = map
        x = type("MyClass", (object,), {})
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = map
        x = type("MyClass", (object,), {})
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()