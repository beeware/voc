def test_function():
    try:
        print('>>> f = map')
        print('>>> x = True')
        print('>>> y = type(1)')
        print('>>> f(x, y)')
        f = map
        x = True
        y = type(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = True')
        print('>>> y = type("a")')
        print('>>> f(x, y)')
        f = map
        x = True
        y = type("a")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = True')
        print('>>> y = type(object())')
        print('>>> f(x, y)')
        f = map
        x = True
        y = type(object())
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = True')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> f(x, y)')
        f = map
        x = True
        y = type("MyClass", (object,), {})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = False')
        print('>>> y = type(1)')
        print('>>> f(x, y)')
        f = map
        x = False
        y = type(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = False')
        print('>>> y = type("a")')
        print('>>> f(x, y)')
        f = map
        x = False
        y = type("a")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = False')
        print('>>> y = type(object())')
        print('>>> f(x, y)')
        f = map
        x = False
        y = type(object())
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = False')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> f(x, y)')
        f = map
        x = False
        y = type("MyClass", (object,), {})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()