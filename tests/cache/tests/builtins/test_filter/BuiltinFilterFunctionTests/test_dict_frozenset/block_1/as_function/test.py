def test_function():
    try:
        print('>>> f = filter')
        print('>>> x = {}')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = filter
        x = {}
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {}')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = filter
        x = {}
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = filter
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = filter
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()