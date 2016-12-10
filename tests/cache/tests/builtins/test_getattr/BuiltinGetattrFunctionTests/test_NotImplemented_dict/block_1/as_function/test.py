def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = NotImplemented')
        print('>>> y = {}')
        print('>>> f(x, y)')
        f = getattr
        x = NotImplemented
        y = {}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = NotImplemented')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> f(x, y)')
        f = getattr
        x = NotImplemented
        y = {"a": 1, "c": 2.3456, "d": "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()