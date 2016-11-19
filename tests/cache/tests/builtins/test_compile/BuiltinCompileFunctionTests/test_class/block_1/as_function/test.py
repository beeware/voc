def test_function():
    try:
        print('>>> f = compile')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = compile
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = compile
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = compile
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = compile
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()