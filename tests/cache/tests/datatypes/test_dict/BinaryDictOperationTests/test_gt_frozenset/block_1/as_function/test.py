def test_function():
    try:
        print('>>> x = {}')
        print('>>> y = frozenset()')
        print('>>> x > y')
        x = {}
        y = frozenset()
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x > y')
        x = {}
        y = frozenset({1, 2.3456, "another"})
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = frozenset()')
        print('>>> x > y')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = frozenset()
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x > y')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = frozenset({1, 2.3456, "another"})
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()