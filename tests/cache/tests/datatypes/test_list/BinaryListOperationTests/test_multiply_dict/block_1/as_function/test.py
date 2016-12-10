def test_function():
    try:
        print('>>> x = []')
        print('>>> y = {}')
        print('>>> x * y')
        x = []
        y = {}
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x * y')
        x = []
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = {}')
        print('>>> x * y')
        x = [3, 4, 5]
        y = {}
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x * y')
        x = [3, 4, 5]
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = {}')
        print('>>> x * y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = {}
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x * y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = {}')
        print('>>> x * y')
        x = ["a","b","c"]
        y = {}
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x * y')
        x = ["a","b","c"]
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()