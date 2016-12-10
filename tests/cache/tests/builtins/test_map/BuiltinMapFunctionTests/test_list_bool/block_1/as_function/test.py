def test_function():
    try:
        print('>>> f = map')
        print('>>> x = []')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = map
        x = []
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = []')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = map
        x = []
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = [3, 4, 5]')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = map
        x = [3, 4, 5]
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = [3, 4, 5]')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = map
        x = [3, 4, 5]
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = map
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = map
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = ["a","b","c"]')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = map
        x = ["a","b","c"]
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = ["a","b","c"]')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = map
        x = ["a","b","c"]
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()