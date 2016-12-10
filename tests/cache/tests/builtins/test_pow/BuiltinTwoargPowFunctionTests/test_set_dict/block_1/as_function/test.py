def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = set()')
        print('>>> y = {}')
        print('>>> f(x, y)')
        f = pow
        x = set()
        y = {}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = set()')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> f(x, y)')
        f = pow
        x = set()
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = {}')
        print('>>> f(x, y)')
        f = pow
        x = {1, 2.3456, "another"}
        y = {}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> f(x, y)')
        f = pow
        x = {1, 2.3456, "another"}
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()