def test_function():
    try:
        print('>>> f = hash')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = hash
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hash')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = hash
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hash')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = hash
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hash')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = hash
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()