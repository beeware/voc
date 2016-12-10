def test_function():
    try:
        print('>>> f = dir')
        print('>>> x = {}')
        print('>>> f(x)')
        f = dir
        x = {}
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dir')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> f(x)')
        f = dir
        x = {"a": 1, "c": 2.3456, "d": "another"}
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()