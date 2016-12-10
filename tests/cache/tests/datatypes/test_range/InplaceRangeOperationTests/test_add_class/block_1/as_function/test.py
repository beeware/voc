def test_function():
    try:
        print('>>> x = range(0)')
        print('>>> y = type(1)')
        print('>>> x += y')
        print('>>> x')
        x = range(0)
        y = type(1)
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(0)')
        print('>>> y = type("a")')
        print('>>> x += y')
        print('>>> x')
        x = range(0)
        y = type("a")
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(0)')
        print('>>> y = type(object())')
        print('>>> x += y')
        print('>>> x')
        x = range(0)
        y = type(object())
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(0)')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x += y')
        print('>>> x')
        x = range(0)
        y = type("MyClass", (object,), {})
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(5)')
        print('>>> y = type(1)')
        print('>>> x += y')
        print('>>> x')
        x = range(5)
        y = type(1)
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(5)')
        print('>>> y = type("a")')
        print('>>> x += y')
        print('>>> x')
        x = range(5)
        y = type("a")
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(5)')
        print('>>> y = type(object())')
        print('>>> x += y')
        print('>>> x')
        x = range(5)
        y = type(object())
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(5)')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x += y')
        print('>>> x')
        x = range(5)
        y = type("MyClass", (object,), {})
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7)')
        print('>>> y = type(1)')
        print('>>> x += y')
        print('>>> x')
        x = range(2, 7)
        y = type(1)
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7)')
        print('>>> y = type("a")')
        print('>>> x += y')
        print('>>> x')
        x = range(2, 7)
        y = type("a")
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7)')
        print('>>> y = type(object())')
        print('>>> x += y')
        print('>>> x')
        x = range(2, 7)
        y = type(object())
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7)')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x += y')
        print('>>> x')
        x = range(2, 7)
        y = type("MyClass", (object,), {})
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7, 2)')
        print('>>> y = type(1)')
        print('>>> x += y')
        print('>>> x')
        x = range(2, 7, 2)
        y = type(1)
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7, 2)')
        print('>>> y = type("a")')
        print('>>> x += y')
        print('>>> x')
        x = range(2, 7, 2)
        y = type("a")
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7, 2)')
        print('>>> y = type(object())')
        print('>>> x += y')
        print('>>> x')
        x = range(2, 7, 2)
        y = type(object())
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7, 2)')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x += y')
        print('>>> x')
        x = range(2, 7, 2)
        y = type("MyClass", (object,), {})
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -1)')
        print('>>> y = type(1)')
        print('>>> x += y')
        print('>>> x')
        x = range(7, 2, -1)
        y = type(1)
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -1)')
        print('>>> y = type("a")')
        print('>>> x += y')
        print('>>> x')
        x = range(7, 2, -1)
        y = type("a")
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -1)')
        print('>>> y = type(object())')
        print('>>> x += y')
        print('>>> x')
        x = range(7, 2, -1)
        y = type(object())
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -1)')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x += y')
        print('>>> x')
        x = range(7, 2, -1)
        y = type("MyClass", (object,), {})
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -2)')
        print('>>> y = type(1)')
        print('>>> x += y')
        print('>>> x')
        x = range(7, 2, -2)
        y = type(1)
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -2)')
        print('>>> y = type("a")')
        print('>>> x += y')
        print('>>> x')
        x = range(7, 2, -2)
        y = type("a")
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -2)')
        print('>>> y = type(object())')
        print('>>> x += y')
        print('>>> x')
        x = range(7, 2, -2)
        y = type(object())
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -2)')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x += y')
        print('>>> x')
        x = range(7, 2, -2)
        y = type("MyClass", (object,), {})
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()