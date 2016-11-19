def test_function():
    try:
        print('>>> f = ascii')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = ascii
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = ascii')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = ascii
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = ascii')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = ascii
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = ascii')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = ascii
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()