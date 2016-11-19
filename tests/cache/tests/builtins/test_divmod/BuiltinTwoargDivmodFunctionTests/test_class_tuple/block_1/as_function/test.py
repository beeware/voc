def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = type(1)')
        print('>>> y = (1, 2)')
        print('>>> f(x, y)')
        f = divmod
        x = type(1)
        y = (1, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type(1)')
        print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> f(x, y)')
        f = divmod
        x = type(1)
        y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type(1)')
        print('>>> y = (3, 1.2, True, )')
        print('>>> f(x, y)')
        f = divmod
        x = type(1)
        y = (3, 1.2, True, )
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type(1)')
        print('>>> y = (1, 2.3456, "another")')
        print('>>> f(x, y)')
        f = divmod
        x = type(1)
        y = (1, 2.3456, "another")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("a")')
        print('>>> y = (1, 2)')
        print('>>> f(x, y)')
        f = divmod
        x = type("a")
        y = (1, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("a")')
        print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> f(x, y)')
        f = divmod
        x = type("a")
        y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("a")')
        print('>>> y = (3, 1.2, True, )')
        print('>>> f(x, y)')
        f = divmod
        x = type("a")
        y = (3, 1.2, True, )
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("a")')
        print('>>> y = (1, 2.3456, "another")')
        print('>>> f(x, y)')
        f = divmod
        x = type("a")
        y = (1, 2.3456, "another")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type(object())')
        print('>>> y = (1, 2)')
        print('>>> f(x, y)')
        f = divmod
        x = type(object())
        y = (1, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type(object())')
        print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> f(x, y)')
        f = divmod
        x = type(object())
        y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type(object())')
        print('>>> y = (3, 1.2, True, )')
        print('>>> f(x, y)')
        f = divmod
        x = type(object())
        y = (3, 1.2, True, )
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type(object())')
        print('>>> y = (1, 2.3456, "another")')
        print('>>> f(x, y)')
        f = divmod
        x = type(object())
        y = (1, 2.3456, "another")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = (1, 2)')
        print('>>> f(x, y)')
        f = divmod
        x = type("MyClass", (object,), {})
        y = (1, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> f(x, y)')
        f = divmod
        x = type("MyClass", (object,), {})
        y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = (3, 1.2, True, )')
        print('>>> f(x, y)')
        f = divmod
        x = type("MyClass", (object,), {})
        y = (3, 1.2, True, )
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = (1, 2.3456, "another")')
        print('>>> f(x, y)')
        f = divmod
        x = type("MyClass", (object,), {})
        y = (1, 2.3456, "another")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()