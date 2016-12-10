def test_function():
    try:
        print('>>> f = type')
        print('>>> x = {}')
        print('>>> f(x)')
        f = type
        x = {}
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = type')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> f(x)')
        f = type
        x = {"a": 1, "c": 2.3456, "d": "another"}
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()