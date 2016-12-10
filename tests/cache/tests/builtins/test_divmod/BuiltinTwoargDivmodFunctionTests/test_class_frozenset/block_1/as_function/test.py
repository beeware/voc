def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = type(1)')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = divmod
        x = type(1)
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type(1)')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = divmod
        x = type(1)
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("a")')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = divmod
        x = type("a")
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("a")')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = divmod
        x = type("a")
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type(object())')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = divmod
        x = type(object())
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type(object())')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = divmod
        x = type(object())
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = divmod
        x = type("MyClass", (object,), {})
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = type("MyClass", (object,), {})')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = divmod
        x = type("MyClass", (object,), {})
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()