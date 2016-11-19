def test_function():
    try:
        print('>>> f = map')
        print('>>> x = None')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = map
        x = None
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = None')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = map
        x = None
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()