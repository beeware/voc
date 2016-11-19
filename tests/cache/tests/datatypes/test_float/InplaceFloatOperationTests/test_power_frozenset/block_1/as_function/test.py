def test_function():
    try:
        print('>>> x = 2.3456')
        print('>>> y = frozenset()')
        print('>>> x **= y')
        print('>>> x')
        x = 2.3456
        y = frozenset()
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 2.3456')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x **= y')
        print('>>> x')
        x = 2.3456
        y = frozenset({1, 2.3456, "another"})
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 0.0')
        print('>>> y = frozenset()')
        print('>>> x **= y')
        print('>>> x')
        x = 0.0
        y = frozenset()
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 0.0')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x **= y')
        print('>>> x')
        x = 0.0
        y = frozenset({1, 2.3456, "another"})
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -3.14159')
        print('>>> y = frozenset()')
        print('>>> x **= y')
        print('>>> x')
        x = -3.14159
        y = frozenset()
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -3.14159')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x **= y')
        print('>>> x')
        x = -3.14159
        y = frozenset({1, 2.3456, "another"})
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -4.81756')
        print('>>> y = frozenset()')
        print('>>> x **= y')
        print('>>> x')
        x = -4.81756
        y = frozenset()
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -4.81756')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x **= y')
        print('>>> x')
        x = -4.81756
        y = frozenset({1, 2.3456, "another"})
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 5.5')
        print('>>> y = frozenset()')
        print('>>> x **= y')
        print('>>> x')
        x = 5.5
        y = frozenset()
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 5.5')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x **= y')
        print('>>> x')
        x = 5.5
        y = frozenset({1, 2.3456, "another"})
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -3.5')
        print('>>> y = frozenset()')
        print('>>> x **= y')
        print('>>> x')
        x = -3.5
        y = frozenset()
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -3.5')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x **= y')
        print('>>> x')
        x = -3.5
        y = frozenset({1, 2.3456, "another"})
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 4.5')
        print('>>> y = frozenset()')
        print('>>> x **= y')
        print('>>> x')
        x = 4.5
        y = frozenset()
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 4.5')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x **= y')
        print('>>> x')
        x = 4.5
        y = frozenset({1, 2.3456, "another"})
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -4.5')
        print('>>> y = frozenset()')
        print('>>> x **= y')
        print('>>> x')
        x = -4.5
        y = frozenset()
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -4.5')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> x **= y')
        print('>>> x')
        x = -4.5
        y = frozenset({1, 2.3456, "another"})
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()