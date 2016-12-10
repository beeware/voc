def test_function():
    try:
        print('>>> f = max')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = max
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = max')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = max
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = max')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = max
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = max')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = max
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()