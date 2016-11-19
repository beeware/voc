def test_function():
    try:
        print('>>> x = (1, 2)')
        print('>>> y = frozenset()')
        print('>>> x <<= y')
        print('>>> x')
        x = (1, 2)
        y = frozenset()
        x <<= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2)')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x <<= y')
        print('>>> x')
        x = (1, 2)
        y = frozenset({1, 2.3456, "another"})
        x <<= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = frozenset()')
        print('>>> x <<= y')
        print('>>> x')
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = frozenset()
        x <<= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x <<= y')
        print('>>> x')
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = frozenset({1, 2.3456, "another"})
        x <<= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = frozenset()')
        print('>>> x <<= y')
        print('>>> x')
        x = (3, 1.2, True, )
        y = frozenset()
        x <<= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x <<= y')
        print('>>> x')
        x = (3, 1.2, True, )
        y = frozenset({1, 2.3456, "another"})
        x <<= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = frozenset()')
        print('>>> x <<= y')
        print('>>> x')
        x = (1, 2.3456, "another")
        y = frozenset()
        x <<= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x <<= y')
        print('>>> x')
        x = (1, 2.3456, "another")
        y = frozenset({1, 2.3456, "another"})
        x <<= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()