def test_function():
    try:
        print('>>> x = (1, 2)')
        print('>>> y = frozenset()')
        print('>>> x // y')
        x = (1, 2)
        y = frozenset()
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2)')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x // y')
        x = (1, 2)
        y = frozenset({1, 2.3456, "another"})
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = frozenset()')
        print('>>> x // y')
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = frozenset()
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x // y')
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = frozenset({1, 2.3456, "another"})
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = frozenset()')
        print('>>> x // y')
        x = (3, 1.2, True, )
        y = frozenset()
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x // y')
        x = (3, 1.2, True, )
        y = frozenset({1, 2.3456, "another"})
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = frozenset()')
        print('>>> x // y')
        x = (1, 2.3456, "another")
        y = frozenset()
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x // y')
        x = (1, 2.3456, "another")
        y = frozenset({1, 2.3456, "another"})
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()