def test_function():
    try:
        print('>>> x = set()')
        print('>>> y = slice(0)')
        print('>>> x / y')
        x = set()
        y = slice(0)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = slice(5)')
        print('>>> x / y')
        x = set()
        y = slice(5)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = slice(2, 7)')
        print('>>> x / y')
        x = set()
        y = slice(2, 7)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x / y')
        x = set()
        y = slice(2, 7, 2)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x / y')
        x = set()
        y = slice(7, 2, -1)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x / y')
        x = set()
        y = slice(7, 2, -2)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = slice(0)')
        print('>>> x / y')
        x = {1, 2.3456, "another"}
        y = slice(0)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = slice(5)')
        print('>>> x / y')
        x = {1, 2.3456, "another"}
        y = slice(5)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = slice(2, 7)')
        print('>>> x / y')
        x = {1, 2.3456, "another"}
        y = slice(2, 7)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x / y')
        x = {1, 2.3456, "another"}
        y = slice(2, 7, 2)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x / y')
        x = {1, 2.3456, "another"}
        y = slice(7, 2, -1)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x / y')
        x = {1, 2.3456, "another"}
        y = slice(7, 2, -2)
        print(x / y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()