def test_function():
    try:
        print('>>> x = {}')
        print('>>> y = 1j')
        print('>>> x >>= y')
        print('>>> x')
        x = {}
        y = 1j
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = 3.14159265j')
        print('>>> x >>= y')
        print('>>> x')
        x = {}
        y = 3.14159265j
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = 1+2j')
        print('>>> x >>= y')
        print('>>> x')
        x = {}
        y = 1+2j
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = 3-4j')
        print('>>> x >>= y')
        print('>>> x')
        x = {}
        y = 3-4j
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {}')
        print('>>> y = -5j')
        print('>>> x >>= y')
        print('>>> x')
        x = {}
        y = -5j
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = 1j')
        print('>>> x >>= y')
        print('>>> x')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = 1j
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = 3.14159265j')
        print('>>> x >>= y')
        print('>>> x')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = 3.14159265j
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = 1+2j')
        print('>>> x >>= y')
        print('>>> x')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = 1+2j
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = 3-4j')
        print('>>> x >>= y')
        print('>>> x')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = 3-4j
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> y = -5j')
        print('>>> x >>= y')
        print('>>> x')
        x = {"a": 1, "c": 2.3456, "d": "another"}
        y = -5j
        x >>= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()