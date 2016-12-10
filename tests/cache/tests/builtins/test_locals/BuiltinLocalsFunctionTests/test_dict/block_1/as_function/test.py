def test_function():
    try:
        print('>>> f = locals')
        print('>>> x = {}')
        print('>>> f(x)')
        f = locals
        x = {}
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = locals')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> f(x)')
        f = locals
        x = {"a": 1, "c": 2.3456, "d": "another"}
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()