def test_function():
    try:
        print('>>> f = help')
        print('>>> x = frozenset()')
        print('>>> f(x)')
        f = help
        x = frozenset()
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = help')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> f(x)')
        f = help
        x = frozenset({1, 2.3456, "another"})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()