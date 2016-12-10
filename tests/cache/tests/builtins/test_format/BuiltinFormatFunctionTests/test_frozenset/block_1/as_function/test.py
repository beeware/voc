def test_function():
    try:
        print('>>> f = format')
        print('>>> x = frozenset()')
        print('>>> f(x)')
        f = format
        x = frozenset()
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = format')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> f(x)')
        f = format
        x = frozenset({1, 2.3456, "another"})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()