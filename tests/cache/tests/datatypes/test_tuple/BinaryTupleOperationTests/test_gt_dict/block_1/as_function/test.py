def test_function():
    try:
        print('>>> x = (1, 2)')
        print('>>> y = {}')
        print('>>> x > y')
        x = (1, 2)
        y = {}
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2)')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x > y')
        x = (1, 2)
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = {}')
        print('>>> x > y')
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = {}
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x > y')
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = {}')
        print('>>> x > y')
        x = (3, 1.2, True, )
        y = {}
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x > y')
        x = (3, 1.2, True, )
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = {}')
        print('>>> x > y')
        x = (1, 2.3456, "another")
        y = {}
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x > y')
        x = (1, 2.3456, "another")
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()