def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = type(1)')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = delattr
        x = type(1)
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type(1)')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = delattr
        x = type(1)
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type(1)')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = delattr
        x = type(1)
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type("a")')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = delattr
        x = type("a")
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type("a")')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = delattr
        x = type("a")
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type("a")')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = delattr
        x = type("a")
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type(object())')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = delattr
        x = type(object())
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type(object())')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = delattr
        x = type(object())
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type(object())')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = delattr
        x = type(object())
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = delattr
        x = type("MyClass", (object,), {})
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = delattr
        x = type("MyClass", (object,), {})
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = delattr
        x = type("MyClass", (object,), {})
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()