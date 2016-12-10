def test_function():
    try:
        print('>>> f = filter')
        print('>>> x = NotImplemented')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = filter
        x = NotImplemented
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = NotImplemented')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = filter
        x = NotImplemented
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()