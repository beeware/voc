def test_function():
    try:
        print('>>> f = oct')
        print('>>> x = set()')
        print('>>> f(x)')
        f = oct
        x = set()
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = oct')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> f(x)')
        f = oct
        x = {1, 2.3456, "another"}
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()