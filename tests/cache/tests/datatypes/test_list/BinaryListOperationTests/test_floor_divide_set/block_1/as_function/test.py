def test_function():
    try:
        print('>>> x = []')
        print('>>> y = set()')
        print('>>> x // y')
        x = []
        y = set()
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x // y')
        x = []
        y = {1, 2.3456, "another"}
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = set()')
        print('>>> x // y')
        x = [3, 4, 5]
        y = set()
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x // y')
        x = [3, 4, 5]
        y = {1, 2.3456, "another"}
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = set()')
        print('>>> x // y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = set()
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x // y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = {1, 2.3456, "another"}
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = set()')
        print('>>> x // y')
        x = ["a","b","c"]
        y = set()
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x // y')
        x = ["a","b","c"]
        y = {1, 2.3456, "another"}
        print(x // y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()