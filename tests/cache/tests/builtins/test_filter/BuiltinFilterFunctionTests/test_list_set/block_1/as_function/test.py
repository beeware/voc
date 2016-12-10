def test_function():
    try:
        print('>>> f = filter')
        print('>>> x = []')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = filter
        x = []
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = []')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = filter
        x = []
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = [3, 4, 5]')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = filter
        x = [3, 4, 5]
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = [3, 4, 5]')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = filter
        x = [3, 4, 5]
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = filter
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = filter
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = ["a","b","c"]')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = filter
        x = ["a","b","c"]
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = ["a","b","c"]')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = filter
        x = ["a","b","c"]
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()