def test_function():
    try:
        print('>>> f = staticmethod')
        print('>>> x = frozenset()')
        print('>>> f(x)')
        f = staticmethod
        x = frozenset()
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = staticmethod')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> f(x)')
        f = staticmethod
        x = frozenset({1, 2.3456, "another"})
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()