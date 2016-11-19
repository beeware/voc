def test_function():
    try:
        print('>>> x = frozenset()')
        print('>>> y = type(1)')
        print('>>> x **= y')
        print('>>> x')
        x = frozenset()
        y = type(1)
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = type("a")')
        print('>>> x **= y')
        print('>>> x')
        x = frozenset()
        y = type("a")
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = type(object())')
        print('>>> x **= y')
        print('>>> x')
        x = frozenset()
        y = type(object())
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x **= y')
        print('>>> x')
        x = frozenset()
        y = type("MyClass", (object,), {})
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = type(1)')
        print('>>> x **= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = type(1)
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = type("a")')
        print('>>> x **= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = type("a")
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = type(object())')
        print('>>> x **= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = type(object())
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = type("MyClass", (object,), {})')
        print('>>> x **= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = type("MyClass", (object,), {})
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()