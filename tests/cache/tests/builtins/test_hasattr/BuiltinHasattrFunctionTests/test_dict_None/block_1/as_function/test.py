def test_function():
    try:
        print('>>> f = hasattr')
        print('>>> x = {}')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = hasattr
        x = {}
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = hasattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()