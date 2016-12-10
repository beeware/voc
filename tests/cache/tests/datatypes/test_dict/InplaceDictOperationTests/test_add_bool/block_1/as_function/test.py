def test_function():
    try:
        print('>>> x = {}')
        print('>>> y = True')
        print('>>> x += y')
        print('>>> x')
        x = {}
        y = True
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = False')
        print('>>> x += y')
        print('>>> x')
        x = {}
        y = False
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = True')
        print('>>> x += y')
        print('>>> x')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = True
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = False')
        print('>>> x += y')
        print('>>> x')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = False
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()