def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = type(1)')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = type(1)
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type(1)')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = type(1)
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("a")')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = type("a")
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("a")')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = type("a")
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type(object())')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = type(object())
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type(object())')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = type(object())
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = type("MyClass", (object,), {})
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = type("MyClass", (object,), {})
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()