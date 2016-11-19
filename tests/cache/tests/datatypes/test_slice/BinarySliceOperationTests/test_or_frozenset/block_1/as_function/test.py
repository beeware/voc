def test_function():
    try:
        print('>>> x = slice(0)')
        print('>>> y = frozenset()')
        print('>>> x | y')
        x = slice(0)
        y = frozenset()
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(0)')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x | y')
        x = slice(0)
        y = frozenset({1, 2.3456, "another"})
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(5)')
        print('>>> y = frozenset()')
        print('>>> x | y')
        x = slice(5)
        y = frozenset()
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(5)')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x | y')
        x = slice(5)
        y = frozenset({1, 2.3456, "another"})
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(2, 7)')
        print('>>> y = frozenset()')
        print('>>> x | y')
        x = slice(2, 7)
        y = frozenset()
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(2, 7)')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x | y')
        x = slice(2, 7)
        y = frozenset({1, 2.3456, "another"})
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(2, 7, 2)')
        print('>>> y = frozenset()')
        print('>>> x | y')
        x = slice(2, 7, 2)
        y = frozenset()
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(2, 7, 2)')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x | y')
        x = slice(2, 7, 2)
        y = frozenset({1, 2.3456, "another"})
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(7, 2, -1)')
        print('>>> y = frozenset()')
        print('>>> x | y')
        x = slice(7, 2, -1)
        y = frozenset()
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(7, 2, -1)')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x | y')
        x = slice(7, 2, -1)
        y = frozenset({1, 2.3456, "another"})
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(7, 2, -2)')
        print('>>> y = frozenset()')
        print('>>> x | y')
        x = slice(7, 2, -2)
        y = frozenset()
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = slice(7, 2, -2)')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x | y')
        x = slice(7, 2, -2)
        y = frozenset({1, 2.3456, "another"})
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()