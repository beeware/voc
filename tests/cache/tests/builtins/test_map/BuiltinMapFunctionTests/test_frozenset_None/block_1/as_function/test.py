def test_function():
    try:
        print('>>> f = map')
        print('>>> x = frozenset()')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = map
        x = frozenset()
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = map
        x = frozenset({1, 2.3456, "another"})
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()