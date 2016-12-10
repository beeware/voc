def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = NotImplemented')
        print('>>> y = type(1)')
        print('>>> f(x, y)')
        f = getattr
        x = NotImplemented
        y = type(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = NotImplemented')
        print('>>> y = type("a")')
        print('>>> f(x, y)')
        f = getattr
        x = NotImplemented
        y = type("a")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = NotImplemented')
        print('>>> y = type(object())')
        print('>>> f(x, y)')
        f = getattr
        x = NotImplemented
        y = type(object())
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = NotImplemented')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> f(x, y)')
        f = getattr
        x = NotImplemented
        y = type("MyClass", (object,), {})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()