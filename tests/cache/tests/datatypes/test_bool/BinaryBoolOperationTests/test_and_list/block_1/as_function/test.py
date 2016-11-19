def test_function():
    try:
        print('>>> x = True')
        print('>>> y = []')
        print('>>> x & y')
        x = True
        y = []
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = [3, 4, 5]')
        print('>>> x & y')
        x = True
        y = [3, 4, 5]
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> x & y')
        x = True
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = ["a","b","c"]')
        print('>>> x & y')
        x = True
        y = ["a","b","c"]
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = []')
        print('>>> x & y')
        x = False
        y = []
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = [3, 4, 5]')
        print('>>> x & y')
        x = False
        y = [3, 4, 5]
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> x & y')
        x = False
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = ["a","b","c"]')
        print('>>> x & y')
        x = False
        y = ["a","b","c"]
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()