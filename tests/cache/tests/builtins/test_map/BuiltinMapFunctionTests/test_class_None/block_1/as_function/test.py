def test_function():
    try:
        print('>>> f = map')
        print('>>> x = type(1)')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = map
        x = type(1)
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = type("a")')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = map
        x = type("a")
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = type(object())')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = map
        x = type(object())
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = map
        x = type("MyClass", (object,), {})
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()