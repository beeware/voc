def test_function():
    try:
        print('>>> f = super')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = super
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = super')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = super
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = super')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = super
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = super')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = super
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()