def test_function():
    try:
        print('>>> x = None')
        print('>>> y = slice(0)')
        print('>>> x - y')
        x = None
        y = slice(0)
        print(x - y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = slice(5)')
        print('>>> x - y')
        x = None
        y = slice(5)
        print(x - y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = slice(2, 7)')
        print('>>> x - y')
        x = None
        y = slice(2, 7)
        print(x - y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x - y')
        x = None
        y = slice(2, 7, 2)
        print(x - y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x - y')
        x = None
        y = slice(7, 2, -1)
        print(x - y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x - y')
        x = None
        y = slice(7, 2, -2)
        print(x - y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()