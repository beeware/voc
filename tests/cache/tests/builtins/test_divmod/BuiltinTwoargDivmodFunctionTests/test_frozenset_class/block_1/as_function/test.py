def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = frozenset()')
        print('>>> y = type(1)')
        print('>>> f(x, y)')
        f = divmod
        x = frozenset()
        y = type(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = frozenset()')
        print('>>> y = type("a")')
        print('>>> f(x, y)')
        f = divmod
        x = frozenset()
        y = type("a")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = frozenset()')
        print('>>> y = type(object())')
        print('>>> f(x, y)')
        f = divmod
        x = frozenset()
        y = type(object())
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = frozenset()')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> f(x, y)')
        f = divmod
        x = frozenset()
        y = type("MyClass", (object,), {})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = type(1)')
        print('>>> f(x, y)')
        f = divmod
        x = frozenset({1, 2.3456, "another"})
        y = type(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = type("a")')
        print('>>> f(x, y)')
        f = divmod
        x = frozenset({1, 2.3456, "another"})
        y = type("a")
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = type(object())')
        print('>>> f(x, y)')
        f = divmod
        x = frozenset({1, 2.3456, "another"})
        y = type(object())
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> f(x, y)')
        f = divmod
        x = frozenset({1, 2.3456, "another"})
        y = type("MyClass", (object,), {})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()