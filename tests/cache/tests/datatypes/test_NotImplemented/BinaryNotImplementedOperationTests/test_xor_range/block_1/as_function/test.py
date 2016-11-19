def test_function():
    try:
        print('>>> x = NotImplemented')
        print('>>> y = range(0)')
        print('>>> x ^ y')
        x = NotImplemented
        y = range(0)
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = range(5)')
        print('>>> x ^ y')
        x = NotImplemented
        y = range(5)
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = range(2, 7)')
        print('>>> x ^ y')
        x = NotImplemented
        y = range(2, 7)
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = range(2, 7, 2)')
        print('>>> x ^ y')
        x = NotImplemented
        y = range(2, 7, 2)
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = range(7, 2, -1)')
        print('>>> x ^ y')
        x = NotImplemented
        y = range(7, 2, -1)
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = range(7, 2, -2)')
        print('>>> x ^ y')
        x = NotImplemented
        y = range(7, 2, -2)
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()