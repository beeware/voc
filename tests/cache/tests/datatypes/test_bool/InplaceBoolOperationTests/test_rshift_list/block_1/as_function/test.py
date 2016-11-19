def test_function():
    try:
        print('>>> x = True')
        print('>>> y = []')
        print('>>> x >>= y')
        print('>>> x')
        x = True
        y = []
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = [3, 4, 5]')
        print('>>> x >>= y')
        print('>>> x')
        x = True
        y = [3, 4, 5]
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> x >>= y')
        print('>>> x')
        x = True
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = ["a","b","c"]')
        print('>>> x >>= y')
        print('>>> x')
        x = True
        y = ["a","b","c"]
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = []')
        print('>>> x >>= y')
        print('>>> x')
        x = False
        y = []
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = [3, 4, 5]')
        print('>>> x >>= y')
        print('>>> x')
        x = False
        y = [3, 4, 5]
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> x >>= y')
        print('>>> x')
        x = False
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = ["a","b","c"]')
        print('>>> x >>= y')
        print('>>> x')
        x = False
        y = ["a","b","c"]
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()