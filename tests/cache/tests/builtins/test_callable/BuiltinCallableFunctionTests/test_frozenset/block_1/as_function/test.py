def test_function():
    try:
        print('>>> f = callable')
        print('>>> x = frozenset()')
        print('>>> f(x)')
        f = callable
        x = frozenset()
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = callable')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> f(x)')
        f = callable
        x = frozenset({1, 2.3456, "another"})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()