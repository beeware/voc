def test_function():
    try:
        print('>>> x = []')
        print('>>> y = True')
        print('>>> x * y')
        x = []
        y = True
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = False')
        print('>>> x * y')
        x = []
        y = False
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = True')
        print('>>> x * y')
        x = [3, 4, 5]
        y = True
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = False')
        print('>>> x * y')
        x = [3, 4, 5]
        y = False
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = True')
        print('>>> x * y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = True
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = False')
        print('>>> x * y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = False
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = True')
        print('>>> x * y')
        x = ["a","b","c"]
        y = True
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = False')
        print('>>> x * y')
        x = ["a","b","c"]
        y = False
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()