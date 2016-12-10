def test_function():
    try:
        print('>>> f = sum')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = sum
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = sum')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = sum
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = sum')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = sum
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = sum')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = sum
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()