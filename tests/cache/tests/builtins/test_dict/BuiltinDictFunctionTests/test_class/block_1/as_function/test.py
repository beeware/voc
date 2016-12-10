def test_function():
    try:
        print('>>> f = dict')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = dict
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dict')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = dict
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dict')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = dict
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dict')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = dict
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()