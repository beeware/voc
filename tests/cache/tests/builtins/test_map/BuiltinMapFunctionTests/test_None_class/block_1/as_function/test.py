def test_function():
    try:
        print('>>> f = map')
        print('>>> x = None')
        print('>>> y = type(1)')
        print('>>> f(x, y)')
        f = map
        x = None
        y = type(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = None')
        print('>>> y = type("a")')
        print('>>> f(x, y)')
        f = map
        x = None
        y = type("a")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = None')
        print('>>> y = type(object())')
        print('>>> f(x, y)')
        f = map
        x = None
        y = type(object())
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = None')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> f(x, y)')
        f = map
        x = None
        y = type("MyClass", (object,), {})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()