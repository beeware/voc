def test_function():
    try:
        print('>>> x = None')
        print('>>> y = range(0)')
        print('>>> x *= y')
        print('>>> x')
        x = None
        y = range(0)
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = range(5)')
        print('>>> x *= y')
        print('>>> x')
        x = None
        y = range(5)
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = range(2, 7)')
        print('>>> x *= y')
        print('>>> x')
        x = None
        y = range(2, 7)
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = range(2, 7, 2)')
        print('>>> x *= y')
        print('>>> x')
        x = None
        y = range(2, 7, 2)
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = range(7, 2, -1)')
        print('>>> x *= y')
        print('>>> x')
        x = None
        y = range(7, 2, -1)
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = range(7, 2, -2)')
        print('>>> x *= y')
        print('>>> x')
        x = None
        y = range(7, 2, -2)
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()