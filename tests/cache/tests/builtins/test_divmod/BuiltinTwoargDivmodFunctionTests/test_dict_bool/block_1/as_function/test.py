def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = {}')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = {}
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {}')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = {}
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = divmod
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = divmod
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()