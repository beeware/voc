def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray()')
        print('>>> y = type(1)')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray()
        y = type(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray()')
        print('>>> y = type("a")')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray()
        y = type("a")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray()')
        print('>>> y = type(object())')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray()
        y = type(object())
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray()')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray()
        y = type("MyClass", (object,), {})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray(1)')
        print('>>> y = type(1)')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray(1)
        y = type(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray(1)')
        print('>>> y = type("a")')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray(1)
        y = type("a")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray(1)')
        print('>>> y = type(object())')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray(1)
        y = type(object())
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray(1)')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray(1)
        y = type("MyClass", (object,), {})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = type(1)')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray([1, 2, 3])
        y = type(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = type("a")')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray([1, 2, 3])
        y = type("a")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = type(object())')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray([1, 2, 3])
        y = type(object())
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray([1, 2, 3])
        y = type("MyClass", (object,), {})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()