def test_function():
    try:
        print('>>> f = map')
        print('>>> x = set()')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = map
        x = set()
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = map
        x = {1, 2.3456, "another"}
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()