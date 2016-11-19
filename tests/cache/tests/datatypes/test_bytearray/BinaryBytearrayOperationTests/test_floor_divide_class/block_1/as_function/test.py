def test_function():
    try:
        print('>>> x = bytearray()')
        print('>>> y = type(1)')
        print('>>> x // y')
        x = bytearray()
        y = type(1)
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray()')
        print('>>> y = type("a")')
        print('>>> x // y')
        x = bytearray()
        y = type("a")
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray()')
        print('>>> y = type(object())')
        print('>>> x // y')
        x = bytearray()
        y = type(object())
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray()')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x // y')
        x = bytearray()
        y = type("MyClass", (object,), {})
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = type(1)')
        print('>>> x // y')
        x = bytearray(1)
        y = type(1)
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = type("a")')
        print('>>> x // y')
        x = bytearray(1)
        y = type("a")
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = type(object())')
        print('>>> x // y')
        x = bytearray(1)
        y = type(object())
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x // y')
        x = bytearray(1)
        y = type("MyClass", (object,), {})
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = type(1)')
        print('>>> x // y')
        x = bytearray([1, 2, 3])
        y = type(1)
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = type("a")')
        print('>>> x // y')
        x = bytearray([1, 2, 3])
        y = type("a")
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = type(object())')
        print('>>> x // y')
        x = bytearray([1, 2, 3])
        y = type(object())
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x // y')
        x = bytearray([1, 2, 3])
        y = type("MyClass", (object,), {})
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()