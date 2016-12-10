def test_function():
    try:
        print('>>> x = frozenset()')
        print('>>> y = {}')
        print('>>> x > y')
        x = frozenset()
        y = {}
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x > y')
        x = frozenset()
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = {}')
        print('>>> x > y')
        x = frozenset({1, 2.3456, "another"})
        y = {}
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x > y')
        x = frozenset({1, 2.3456, "another"})
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()