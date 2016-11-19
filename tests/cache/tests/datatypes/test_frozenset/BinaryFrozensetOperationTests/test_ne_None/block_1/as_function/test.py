def test_function():
    try:
        print('>>> x = frozenset()')
        print('>>> y = None')
        print('>>> x != y')
        x = frozenset()
        y = None
        print(x != y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = None')
        print('>>> x != y')
        x = frozenset({1, 2.3456, "another"})
        y = None
        print(x != y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()