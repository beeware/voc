def test_function():
    try:
        print('>>> x = []')
        print('>>> y = frozenset()')
        print('>>> x % y')
        x = []
        y = frozenset()
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x % y')
        x = []
        y = frozenset({1, 2.3456, "another"})
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = frozenset()')
        print('>>> x % y')
        x = [3, 4, 5]
        y = frozenset()
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x % y')
        x = [3, 4, 5]
        y = frozenset({1, 2.3456, "another"})
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = frozenset()')
        print('>>> x % y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = frozenset()
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x % y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = frozenset({1, 2.3456, "another"})
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = frozenset()')
        print('>>> x % y')
        x = ["a","b","c"]
        y = frozenset()
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x % y')
        x = ["a","b","c"]
        y = frozenset({1, 2.3456, "another"})
        print(x % y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()