def test_function():
    try:
        print('>>> f = property')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = property
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = property')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = property
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = property')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = property
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = property')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = property
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()