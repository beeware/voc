def test_function():
    try:
        print('>>> x = set()')
        print('>>> y = type(1)')
        print('>>> x *= y')
        print('>>> x')
        x = set()
        y = type(1)
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = type("a")')
        print('>>> x *= y')
        print('>>> x')
        x = set()
        y = type("a")
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = type(object())')
        print('>>> x *= y')
        print('>>> x')
        x = set()
        y = type(object())
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x *= y')
        print('>>> x')
        x = set()
        y = type("MyClass", (object,), {})
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = type(1)')
        print('>>> x *= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = type(1)
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = type("a")')
        print('>>> x *= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = type("a")
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = type(object())')
        print('>>> x *= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = type(object())
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x *= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = type("MyClass", (object,), {})
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()