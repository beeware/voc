def test_function():
    try:
        print('>>> x = True')
        print('>>> y = {}')
        print('>>> x + y')
        x = True
        y = {}
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x + y')
        x = True
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = {}')
        print('>>> x + y')
        x = False
        y = {}
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x + y')
        x = False
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()