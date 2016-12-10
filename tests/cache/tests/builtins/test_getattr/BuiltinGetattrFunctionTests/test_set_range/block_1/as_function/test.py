def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = set()')
        print('>>> y = range(0)')
        print('>>> f(x, y)')
        f = getattr
        x = set()
        y = range(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = set()')
        print('>>> y = range(5)')
        print('>>> f(x, y)')
        f = getattr
        x = set()
        y = range(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = set()')
        print('>>> y = range(2, 7)')
        print('>>> f(x, y)')
        f = getattr
        x = set()
        y = range(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = set()')
        print('>>> y = range(2, 7, 2)')
        print('>>> f(x, y)')
        f = getattr
        x = set()
        y = range(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = set()')
        print('>>> y = range(7, 2, -1)')
        print('>>> f(x, y)')
        f = getattr
        x = set()
        y = range(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = set()')
        print('>>> y = range(7, 2, -2)')
        print('>>> f(x, y)')
        f = getattr
        x = set()
        y = range(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = range(0)')
        print('>>> f(x, y)')
        f = getattr
        x = {1, 2.3456, "another"}
        y = range(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = range(5)')
        print('>>> f(x, y)')
        f = getattr
        x = {1, 2.3456, "another"}
        y = range(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = range(2, 7)')
        print('>>> f(x, y)')
        f = getattr
        x = {1, 2.3456, "another"}
        y = range(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = range(2, 7, 2)')
        print('>>> f(x, y)')
        f = getattr
        x = {1, 2.3456, "another"}
        y = range(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = range(7, 2, -1)')
        print('>>> f(x, y)')
        f = getattr
        x = {1, 2.3456, "another"}
        y = range(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = range(7, 2, -2)')
        print('>>> f(x, y)')
        f = getattr
        x = {1, 2.3456, "another"}
        y = range(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()