def test_function():
    try:
        print('>>> x = 3')
        print('>>> y = frozenset()')
        print('>>> x | y')
        x = 3
        y = frozenset()
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 3')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x | y')
        x = 3
        y = frozenset({1, 2.3456, "another"})
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 0')
        print('>>> y = frozenset()')
        print('>>> x | y')
        x = 0
        y = frozenset()
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 0')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x | y')
        x = 0
        y = frozenset({1, 2.3456, "another"})
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -5')
        print('>>> y = frozenset()')
        print('>>> x | y')
        x = -5
        y = frozenset()
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -5')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x | y')
        x = -5
        y = frozenset({1, 2.3456, "another"})
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -3')
        print('>>> y = frozenset()')
        print('>>> x | y')
        x = -3
        y = frozenset()
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -3')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x | y')
        x = -3
        y = frozenset({1, 2.3456, "another"})
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 5')
        print('>>> y = frozenset()')
        print('>>> x | y')
        x = 5
        y = frozenset()
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 5')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x | y')
        x = 5
        y = frozenset({1, 2.3456, "another"})
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 1')
        print('>>> y = frozenset()')
        print('>>> x | y')
        x = 1
        y = frozenset()
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 1')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x | y')
        x = 1
        y = frozenset({1, 2.3456, "another"})
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()