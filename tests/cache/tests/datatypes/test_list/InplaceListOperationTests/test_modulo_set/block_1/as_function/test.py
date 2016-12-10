def test_function():
    try:
        print('>>> x = []')
        print('>>> y = set()')
        print('>>> x %= y')
        print('>>> x')
        x = []
        y = set()
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x %= y')
        print('>>> x')
        x = []
        y = {1, 2.3456, "another"}
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = set()')
        print('>>> x %= y')
        print('>>> x')
        x = [3, 4, 5]
        y = set()
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x %= y')
        print('>>> x')
        x = [3, 4, 5]
        y = {1, 2.3456, "another"}
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = set()')
        print('>>> x %= y')
        print('>>> x')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = set()
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x %= y')
        print('>>> x')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = {1, 2.3456, "another"}
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = set()')
        print('>>> x %= y')
        print('>>> x')
        x = ["a","b","c"]
        y = set()
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x %= y')
        print('>>> x')
        x = ["a","b","c"]
        y = {1, 2.3456, "another"}
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()