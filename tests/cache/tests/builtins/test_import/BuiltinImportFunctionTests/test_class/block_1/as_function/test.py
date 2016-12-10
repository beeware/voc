def test_function():
    try:
        print('>>> f = __import__')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = __import__
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = __import__')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = __import__
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = __import__')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = __import__
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = __import__')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = __import__
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()