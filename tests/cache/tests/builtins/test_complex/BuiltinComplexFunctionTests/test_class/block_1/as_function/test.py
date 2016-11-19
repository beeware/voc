def test_function():
    try:
        print('>>> f = complex')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = complex
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = complex')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = complex
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = complex')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = complex
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = complex')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = complex
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()