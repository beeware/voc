def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = []')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = pow
        x = []
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = [3, 4, 5]')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = pow
        x = [3, 4, 5]
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = pow
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = ["a","b","c"]')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = pow
        x = ["a","b","c"]
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()