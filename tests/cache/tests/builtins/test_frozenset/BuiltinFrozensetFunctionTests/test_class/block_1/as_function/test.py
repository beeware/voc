def test_function():
    try:
        print('>>> f = frozenset')
        print('>>> x = type(1)')
        print('>>> f(x)')
        f = frozenset
        x = type(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = frozenset')
        print('>>> x = type("a")')
        print('>>> f(x)')
        f = frozenset
        x = type("a")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = frozenset')
        print('>>> x = type(object())')
        print('>>> f(x)')
        f = frozenset
        x = type(object())
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = frozenset')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> f(x)')
        f = frozenset
        x = type("MyClass", (object,), {})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()