def test_function():
    try:
        print('>>> x = frozenset()')
        print('>>> y = 1j')
        print('>>> x != y')
        x = frozenset()
        y = 1j
        print(x != y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = 3.14159265j')
        print('>>> x != y')
        x = frozenset()
        y = 3.14159265j
        print(x != y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = 1+2j')
        print('>>> x != y')
        x = frozenset()
        y = 1+2j
        print(x != y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = 3-4j')
        print('>>> x != y')
        x = frozenset()
        y = 3-4j
        print(x != y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset()')
        print('>>> y = -5j')
        print('>>> x != y')
        x = frozenset()
        y = -5j
        print(x != y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = 1j')
        print('>>> x != y')
        x = frozenset({1, 2.3456, "another"})
        y = 1j
        print(x != y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = 3.14159265j')
        print('>>> x != y')
        x = frozenset({1, 2.3456, "another"})
        y = 3.14159265j
        print(x != y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = 1+2j')
        print('>>> x != y')
        x = frozenset({1, 2.3456, "another"})
        y = 1+2j
        print(x != y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = 3-4j')
        print('>>> x != y')
        x = frozenset({1, 2.3456, "another"})
        y = 3-4j
        print(x != y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = -5j')
        print('>>> x != y')
        x = frozenset({1, 2.3456, "another"})
        y = -5j
        print(x != y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()