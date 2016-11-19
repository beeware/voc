def test_function():
    try:
        print('>>> x = range(0)')
        print('>>> y = True')
        print('>>> x ^ y')
        x = range(0)
        y = True
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(0)')
        print('>>> y = False')
        print('>>> x ^ y')
        x = range(0)
        y = False
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(5)')
        print('>>> y = True')
        print('>>> x ^ y')
        x = range(5)
        y = True
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(5)')
        print('>>> y = False')
        print('>>> x ^ y')
        x = range(5)
        y = False
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7)')
        print('>>> y = True')
        print('>>> x ^ y')
        x = range(2, 7)
        y = True
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7)')
        print('>>> y = False')
        print('>>> x ^ y')
        x = range(2, 7)
        y = False
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7, 2)')
        print('>>> y = True')
        print('>>> x ^ y')
        x = range(2, 7, 2)
        y = True
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7, 2)')
        print('>>> y = False')
        print('>>> x ^ y')
        x = range(2, 7, 2)
        y = False
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -1)')
        print('>>> y = True')
        print('>>> x ^ y')
        x = range(7, 2, -1)
        y = True
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -1)')
        print('>>> y = False')
        print('>>> x ^ y')
        x = range(7, 2, -1)
        y = False
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -2)')
        print('>>> y = True')
        print('>>> x ^ y')
        x = range(7, 2, -2)
        y = True
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -2)')
        print('>>> y = False')
        print('>>> x ^ y')
        x = range(7, 2, -2)
        y = False
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()