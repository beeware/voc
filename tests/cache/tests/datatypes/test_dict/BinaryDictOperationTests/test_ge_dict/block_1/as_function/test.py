def test_function():
    try:
        print('>>> x = {}')
        print('>>> y = {}')
        print('>>> x >= y')
        x = {}
        y = {}
        print(x >= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x >= y')
        x = {}
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x >= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = {}')
        print('>>> x >= y')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = {}
        print(x >= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x >= y')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x >= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()