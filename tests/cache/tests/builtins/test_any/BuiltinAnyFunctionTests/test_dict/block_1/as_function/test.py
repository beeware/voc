def test_function():
    try:
        print('>>> f = any')
        print('>>> x = {}')
        print('>>> f(x)')
        f = any
        x = {}
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = any')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> f(x)')
        f = any
        x = {"a": 1, "c": 2.3456, "d": "another"}
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()