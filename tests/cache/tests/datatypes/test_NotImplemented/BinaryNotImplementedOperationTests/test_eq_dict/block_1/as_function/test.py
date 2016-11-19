def test_function():
    try:
        print('>>> x = NotImplemented')
        print('>>> y = {}')
        print('>>> x == y')
        x = NotImplemented
        y = {}
        print(x == y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x == y')
        x = NotImplemented
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(x == y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()