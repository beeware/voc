def test_function():
    try:
        print('>>> x = frozenset()')
        print('>>> y = True')
        print('>>> x &= y')
        print('>>> x')
        x = frozenset()
        y = True
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = False')
        print('>>> x &= y')
        print('>>> x')
        x = frozenset()
        y = False
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = True')
        print('>>> x &= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = True
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = False')
        print('>>> x &= y')
        print('>>> x')
        x = frozenset({1, 2.3456, "another"})
        y = False
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()