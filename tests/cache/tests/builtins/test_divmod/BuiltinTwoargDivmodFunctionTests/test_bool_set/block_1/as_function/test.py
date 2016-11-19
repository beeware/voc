def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = True')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = divmod
        x = True
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = True')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = divmod
        x = True
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = False')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = divmod
        x = False
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = False')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = divmod
        x = False
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()