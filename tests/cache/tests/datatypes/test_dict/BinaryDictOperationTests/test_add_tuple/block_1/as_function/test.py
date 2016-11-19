def test_function():
    try:
        print('>>> x = {}')
        print('>>> y = (1, 2)')
        print('>>> x + y')
        x = {}
        y = (1, 2)
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> x + y')
        x = {}
        y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = (3, 1.2, True, )')
        print('>>> x + y')
        x = {}
        y = (3, 1.2, True, )
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = (1, 2.3456, "another")')
        print('>>> x + y')
        x = {}
        y = (1, 2.3456, "another")
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = (1, 2)')
        print('>>> x + y')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = (1, 2)
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> x + y')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = (3, 1.2, True, )')
        print('>>> x + y')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = (3, 1.2, True, )
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = (1, 2.3456, "another")')
        print('>>> x + y')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = (1, 2.3456, "another")
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()