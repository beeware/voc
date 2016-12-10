def test_function():
    try:
        print('>>> x = 1j')
        print('>>> y = {}')
        print('>>> x ^= y')
        print('>>> x')
        x = 1j
        y = {}
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 1j')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x ^= y')
        print('>>> x')
        x = 1j
        y = {"a": 1, "c": 2.3456, "d": "another"}
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 3.14159265j')
        print('>>> y = {}')
        print('>>> x ^= y')
        print('>>> x')
        x = 3.14159265j
        y = {}
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 3.14159265j')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x ^= y')
        print('>>> x')
        x = 3.14159265j
        y = {"a": 1, "c": 2.3456, "d": "another"}
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 1+2j')
        print('>>> y = {}')
        print('>>> x ^= y')
        print('>>> x')
        x = 1+2j
        y = {}
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 1+2j')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x ^= y')
        print('>>> x')
        x = 1+2j
        y = {"a": 1, "c": 2.3456, "d": "another"}
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 3-4j')
        print('>>> y = {}')
        print('>>> x ^= y')
        print('>>> x')
        x = 3-4j
        y = {}
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 3-4j')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x ^= y')
        print('>>> x')
        x = 3-4j
        y = {"a": 1, "c": 2.3456, "d": "another"}
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -5j')
        print('>>> y = {}')
        print('>>> x ^= y')
        print('>>> x')
        x = -5j
        y = {}
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -5j')
        print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
        print('>>> x ^= y')
        print('>>> x')
        x = -5j
        y = {"a": 1, "c": 2.3456, "d": "another"}
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()