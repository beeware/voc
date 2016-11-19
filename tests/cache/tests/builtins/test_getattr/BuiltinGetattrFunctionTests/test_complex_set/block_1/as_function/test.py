def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = 1j')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = getattr
        x = 1j
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = 1j')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = getattr
        x = 1j
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = 3.14159265j')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = getattr
        x = 3.14159265j
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = 3.14159265j')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = getattr
        x = 3.14159265j
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = 1+2j')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = getattr
        x = 1+2j
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = 1+2j')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = getattr
        x = 1+2j
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = 3-4j')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = getattr
        x = 3-4j
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = 3-4j')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = getattr
        x = 3-4j
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = -5j')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = getattr
        x = -5j
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = -5j')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = getattr
        x = -5j
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()