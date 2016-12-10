def test_function():
    try:
        print('>>> x = 3')
        print('>>> y = set()')
        print('>>> x += y')
        print('>>> x')
        x = 3
        y = set()
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 3')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x += y')
        print('>>> x')
        x = 3
        y = {1, 2.3456, "another"}
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 0')
        print('>>> y = set()')
        print('>>> x += y')
        print('>>> x')
        x = 0
        y = set()
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 0')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x += y')
        print('>>> x')
        x = 0
        y = {1, 2.3456, "another"}
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -5')
        print('>>> y = set()')
        print('>>> x += y')
        print('>>> x')
        x = -5
        y = set()
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -5')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x += y')
        print('>>> x')
        x = -5
        y = {1, 2.3456, "another"}
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -3')
        print('>>> y = set()')
        print('>>> x += y')
        print('>>> x')
        x = -3
        y = set()
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -3')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x += y')
        print('>>> x')
        x = -3
        y = {1, 2.3456, "another"}
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 5')
        print('>>> y = set()')
        print('>>> x += y')
        print('>>> x')
        x = 5
        y = set()
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 5')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x += y')
        print('>>> x')
        x = 5
        y = {1, 2.3456, "another"}
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 1')
        print('>>> y = set()')
        print('>>> x += y')
        print('>>> x')
        x = 1
        y = set()
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 1')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x += y')
        print('>>> x')
        x = 1
        y = {1, 2.3456, "another"}
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()