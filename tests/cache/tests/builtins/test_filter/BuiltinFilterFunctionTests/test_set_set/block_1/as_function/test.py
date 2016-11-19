def test_function():
    try:
        print('>>> f = filter')
        print('>>> x = set()')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = filter
        x = set()
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = set()')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = filter
        x = set()
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = filter
        x = {1, 2.3456, "another"}
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = filter
        x = {1, 2.3456, "another"}
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()