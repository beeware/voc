def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = {}')
        print('>>> y = range(0)')
        print('>>> f(x, y)')
        f = pow
        x = {}
        y = range(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {}')
        print('>>> y = range(5)')
        print('>>> f(x, y)')
        f = pow
        x = {}
        y = range(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {}')
        print('>>> y = range(2, 7)')
        print('>>> f(x, y)')
        f = pow
        x = {}
        y = range(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {}')
        print('>>> y = range(2, 7, 2)')
        print('>>> f(x, y)')
        f = pow
        x = {}
        y = range(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {}')
        print('>>> y = range(7, 2, -1)')
        print('>>> f(x, y)')
        f = pow
        x = {}
        y = range(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {}')
        print('>>> y = range(7, 2, -2)')
        print('>>> f(x, y)')
        f = pow
        x = {}
        y = range(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = range(0)')
        print('>>> f(x, y)')
        f = pow
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = range(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = range(5)')
        print('>>> f(x, y)')
        f = pow
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = range(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = range(2, 7)')
        print('>>> f(x, y)')
        f = pow
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = range(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = range(2, 7, 2)')
        print('>>> f(x, y)')
        f = pow
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = range(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = range(7, 2, -1)')
        print('>>> f(x, y)')
        f = pow
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = range(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = range(7, 2, -2)')
        print('>>> f(x, y)')
        f = pow
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = range(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()