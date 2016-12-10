def test_function():
    try:
        print('>>> f = set')
        print('>>> x = set()')
        print('>>> f(x)')
        f = set
        x = set()
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = set')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> f(x)')
        f = set
        x = {1, 2.3456, "another"}
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()