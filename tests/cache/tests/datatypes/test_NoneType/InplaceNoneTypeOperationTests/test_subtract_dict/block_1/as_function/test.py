def test_function():
    try:
        print('>>> x = None')
        print('>>> y = {}')
        print('>>> x -= y')
        print('>>> x')
        x = None
        y = {}
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x -= y')
        print('>>> x')
        x = None
        y = {"a": 1, "c": 2.3456, "d": "another"}
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()