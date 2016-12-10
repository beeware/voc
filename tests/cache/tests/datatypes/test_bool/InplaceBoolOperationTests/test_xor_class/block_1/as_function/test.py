def test_function():
    try:
        print('>>> x = True')
        print('>>> y = type(1)')
        print('>>> x ^= y')
        print('>>> x')
        x = True
        y = type(1)
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = type("a")')
        print('>>> x ^= y')
        print('>>> x')
        x = True
        y = type("a")
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = type(object())')
        print('>>> x ^= y')
        print('>>> x')
        x = True
        y = type(object())
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x ^= y')
        print('>>> x')
        x = True
        y = type("MyClass", (object,), {})
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = type(1)')
        print('>>> x ^= y')
        print('>>> x')
        x = False
        y = type(1)
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = type("a")')
        print('>>> x ^= y')
        print('>>> x')
        x = False
        y = type("a")
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = type(object())')
        print('>>> x ^= y')
        print('>>> x')
        x = False
        y = type(object())
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x ^= y')
        print('>>> x')
        x = False
        y = type("MyClass", (object,), {})
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()