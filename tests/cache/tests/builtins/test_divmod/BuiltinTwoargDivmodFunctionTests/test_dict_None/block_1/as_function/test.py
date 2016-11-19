def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = {}')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = divmod
        x = {}
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = divmod
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()