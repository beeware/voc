def test_function():
    try:
        print('>>> x = frozenset()')
        print('>>> y = NotImplemented')
        print('>>> x * y')
        x = frozenset()
        y = NotImplemented
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = NotImplemented')
        print('>>> x * y')
        x = frozenset({1, 2.3456, "another"})
        y = NotImplemented
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()