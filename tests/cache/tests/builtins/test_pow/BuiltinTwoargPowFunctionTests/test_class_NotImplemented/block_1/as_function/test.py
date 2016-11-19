def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = type(1)')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = pow
        x = type(1)
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = type("a")')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = pow
        x = type("a")
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = type(object())')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = pow
        x = type(object())
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = pow
        x = type("MyClass", (object,), {})
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()