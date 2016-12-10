def test_function():
    try:
        print('>>> f = repr')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = repr
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = repr')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = repr
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = repr')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = repr
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = repr')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = repr
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()