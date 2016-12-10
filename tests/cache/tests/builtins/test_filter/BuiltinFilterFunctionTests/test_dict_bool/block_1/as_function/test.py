def test_function():
    try:
        print('>>> f = filter')
        print('>>> x = {}')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = filter
        x = {}
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {}')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = filter
        x = {}
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = filter
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = filter
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()