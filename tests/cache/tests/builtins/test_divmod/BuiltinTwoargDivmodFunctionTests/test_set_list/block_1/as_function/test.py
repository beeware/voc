def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = set()')
        print('>>> y = []')
        print('>>> f(x, y)')
        f = divmod
        x = set()
        y = []
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = set()')
        print('>>> y = [3, 4, 5]')
        print('>>> f(x, y)')
        f = divmod
        x = set()
        y = [3, 4, 5]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = set()')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> f(x, y)')
        f = divmod
        x = set()
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = set()')
        print('>>> y = ["a","b","c"]')
        print('>>> f(x, y)')
        f = divmod
        x = set()
        y = ["a","b","c"]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = []')
        print('>>> f(x, y)')
        f = divmod
        x = {1, 2.3456, "another"}
        y = []
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = [3, 4, 5]')
        print('>>> f(x, y)')
        f = divmod
        x = {1, 2.3456, "another"}
        y = [3, 4, 5]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> f(x, y)')
        f = divmod
        x = {1, 2.3456, "another"}
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = ["a","b","c"]')
        print('>>> f(x, y)')
        f = divmod
        x = {1, 2.3456, "another"}
        y = ["a","b","c"]
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()