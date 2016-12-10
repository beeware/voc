def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = {}')
        print('>>> y = slice(0)')
        print('>>> f(x, y)')
        f = delattr
        x = {}
        y = slice(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = {}')
        print('>>> y = slice(5)')
        print('>>> f(x, y)')
        f = delattr
        x = {}
        y = slice(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = {}')
        print('>>> y = slice(2, 7)')
        print('>>> f(x, y)')
        f = delattr
        x = {}
        y = slice(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = {}')
        print('>>> y = slice(2, 7, 2)')
        print('>>> f(x, y)')
        f = delattr
        x = {}
        y = slice(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = {}')
        print('>>> y = slice(7, 2, -1)')
        print('>>> f(x, y)')
        f = delattr
        x = {}
        y = slice(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = {}')
        print('>>> y = slice(7, 2, -2)')
        print('>>> f(x, y)')
        f = delattr
        x = {}
        y = slice(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = slice(0)')
        print('>>> f(x, y)')
        f = delattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = slice(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = slice(5)')
        print('>>> f(x, y)')
        f = delattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = slice(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = slice(2, 7)')
        print('>>> f(x, y)')
        f = delattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = slice(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = slice(2, 7, 2)')
        print('>>> f(x, y)')
        f = delattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = slice(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = slice(7, 2, -1)')
        print('>>> f(x, y)')
        f = delattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = slice(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = slice(7, 2, -2)')
        print('>>> f(x, y)')
        f = delattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = slice(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()