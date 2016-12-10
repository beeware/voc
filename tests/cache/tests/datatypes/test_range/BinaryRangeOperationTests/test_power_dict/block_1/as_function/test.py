def test_function():
    try:
        print('>>> x = range(0)')
        print('>>> y = {}')
        print('>>> x ** y')
        x = range(0)
        y = {}
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(0)')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x ** y')
        x = range(0)
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(5)')
        print('>>> y = {}')
        print('>>> x ** y')
        x = range(5)
        y = {}
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(5)')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x ** y')
        x = range(5)
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7)')
        print('>>> y = {}')
        print('>>> x ** y')
        x = range(2, 7)
        y = {}
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7)')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x ** y')
        x = range(2, 7)
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7, 2)')
        print('>>> y = {}')
        print('>>> x ** y')
        x = range(2, 7, 2)
        y = {}
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7, 2)')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x ** y')
        x = range(2, 7, 2)
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -1)')
        print('>>> y = {}')
        print('>>> x ** y')
        x = range(7, 2, -1)
        y = {}
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -1)')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x ** y')
        x = range(7, 2, -1)
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -2)')
        print('>>> y = {}')
        print('>>> x ** y')
        x = range(7, 2, -2)
        y = {}
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -2)')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x ** y')
        x = range(7, 2, -2)
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()