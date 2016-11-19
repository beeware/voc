def test_function():
    try:
        print('>>> f = int')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = int
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = int')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = int
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = int')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = int
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = int')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = int
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()