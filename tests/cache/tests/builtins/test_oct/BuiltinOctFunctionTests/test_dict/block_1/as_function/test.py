def test_function():
    try:
        print('>>> f = oct')
        print('>>> x = {}')
        print('>>> f(x)')
        f = oct
        x = {}
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = oct')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> f(x)')
        f = oct
        x = {"a": 1, "c": 2.3456, "d": "another"}
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()