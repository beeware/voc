def test_function():
    try:
        print('>>> f = hasattr')
        print('>>> x = {}')
        print('>>> y = 1j')
        print('>>> f(x, y)')
        f = hasattr
        x = {}
        y = 1j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = {}')
        print('>>> y = 3.14159265j')
        print('>>> f(x, y)')
        f = hasattr
        x = {}
        y = 3.14159265j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = {}')
        print('>>> y = 1+2j')
        print('>>> f(x, y)')
        f = hasattr
        x = {}
        y = 1+2j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = {}')
        print('>>> y = 3-4j')
        print('>>> f(x, y)')
        f = hasattr
        x = {}
        y = 3-4j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = {}')
        print('>>> y = -5j')
        print('>>> f(x, y)')
        f = hasattr
        x = {}
        y = -5j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = 1j')
        print('>>> f(x, y)')
        f = hasattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = 1j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = 3.14159265j')
        print('>>> f(x, y)')
        f = hasattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = 3.14159265j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = 1+2j')
        print('>>> f(x, y)')
        f = hasattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = 1+2j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = 3-4j')
        print('>>> f(x, y)')
        f = hasattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = 3-4j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = -5j')
        print('>>> f(x, y)')
        f = hasattr
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = -5j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()