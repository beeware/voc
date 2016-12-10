def test_function():
    try:
        print('>>> f = filter')
        print('>>> x = set()')
        print('>>> y = slice(0)')
        print('>>> f(x, y)')
        f = filter
        x = set()
        y = slice(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = set()')
        print('>>> y = slice(5)')
        print('>>> f(x, y)')
        f = filter
        x = set()
        y = slice(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = set()')
        print('>>> y = slice(2, 7)')
        print('>>> f(x, y)')
        f = filter
        x = set()
        y = slice(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = set()')
        print('>>> y = slice(2, 7, 2)')
        print('>>> f(x, y)')
        f = filter
        x = set()
        y = slice(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = set()')
        print('>>> y = slice(7, 2, -1)')
        print('>>> f(x, y)')
        f = filter
        x = set()
        y = slice(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = set()')
        print('>>> y = slice(7, 2, -2)')
        print('>>> f(x, y)')
        f = filter
        x = set()
        y = slice(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = slice(0)')
        print('>>> f(x, y)')
        f = filter
        x = {1, 2.3456, "another"}
        y = slice(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = slice(5)')
        print('>>> f(x, y)')
        f = filter
        x = {1, 2.3456, "another"}
        y = slice(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = slice(2, 7)')
        print('>>> f(x, y)')
        f = filter
        x = {1, 2.3456, "another"}
        y = slice(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = slice(2, 7, 2)')
        print('>>> f(x, y)')
        f = filter
        x = {1, 2.3456, "another"}
        y = slice(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = slice(7, 2, -1)')
        print('>>> f(x, y)')
        f = filter
        x = {1, 2.3456, "another"}
        y = slice(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = slice(7, 2, -2)')
        print('>>> f(x, y)')
        f = filter
        x = {1, 2.3456, "another"}
        y = slice(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()