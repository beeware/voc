def test_function():
    try:
        print('>>> f = open')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = open
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = open')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = open
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = open')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = open
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = open')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = open
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()