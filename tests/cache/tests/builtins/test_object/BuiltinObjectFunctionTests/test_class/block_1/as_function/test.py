def test_function():
    try:
        print('>>> f = object')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = object
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = object')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = object
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = object')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = object
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = object')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = object
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()