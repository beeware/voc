def test_function():
    try:
        print('>>> x = True')
        print('>>> y = {}')
        print('>>> x <<= y')
        print('>>> x')
        x = True
        y = {}
        x <<= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x <<= y')
        print('>>> x')
        x = True
        y = {"a": 1, "c": 2.3456, "d": "another"}
        x <<= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = {}')
        print('>>> x <<= y')
        print('>>> x')
        x = False
        y = {}
        x <<= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x <<= y')
        print('>>> x')
        x = False
        y = {"a": 1, "c": 2.3456, "d": "another"}
        x <<= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()