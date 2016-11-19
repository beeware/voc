def test_function():
    try:
        print('>>> f = reversed')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = reversed
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = reversed')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = reversed
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = reversed')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = reversed
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = reversed')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = reversed
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()