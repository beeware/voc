def test_function():
    try:
        print('>>> x = frozenset()')
        print('>>> y = []')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset()
        y = []
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = [3, 4, 5]')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset()
        y = [3, 4, 5]
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset()
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = ["a","b","c"]')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset()
        y = ["a","b","c"]
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = []')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = []
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = [3, 4, 5]')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = [3, 4, 5]
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = ["a","b","c"]')
        print('>>> x |= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = ["a","b","c"]
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()