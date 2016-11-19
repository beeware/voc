def test_function():
    try:
        print('>>> x = 1j')
        print('>>> y = frozenset()')
        print('>>> x //= y')
        print('>>> x')
        x = 1j
        y = frozenset()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 1j')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x //= y')
        print('>>> x')
        x = 1j
        y = frozenset({1, 2.3456, "another"})
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 3.14159265j')
        print('>>> y = frozenset()')
        print('>>> x //= y')
        print('>>> x')
        x = 3.14159265j
        y = frozenset()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 3.14159265j')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x //= y')
        print('>>> x')
        x = 3.14159265j
        y = frozenset({1, 2.3456, "another"})
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 1+2j')
        print('>>> y = frozenset()')
        print('>>> x //= y')
        print('>>> x')
        x = 1+2j
        y = frozenset()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 1+2j')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x //= y')
        print('>>> x')
        x = 1+2j
        y = frozenset({1, 2.3456, "another"})
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 3-4j')
        print('>>> y = frozenset()')
        print('>>> x //= y')
        print('>>> x')
        x = 3-4j
        y = frozenset()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 3-4j')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x //= y')
        print('>>> x')
        x = 3-4j
        y = frozenset({1, 2.3456, "another"})
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -5j')
        print('>>> y = frozenset()')
        print('>>> x //= y')
        print('>>> x')
        x = -5j
        y = frozenset()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -5j')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x //= y')
        print('>>> x')
        x = -5j
        y = frozenset({1, 2.3456, "another"})
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()