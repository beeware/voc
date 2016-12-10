def test_function():
    try:
        print('>>> x = range(0)')
        print('>>> y = NotImplemented')
        print('>>> x ^ y')
        x = range(0)
        y = NotImplemented
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(5)')
        print('>>> y = NotImplemented')
        print('>>> x ^ y')
        x = range(5)
        y = NotImplemented
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7)')
        print('>>> y = NotImplemented')
        print('>>> x ^ y')
        x = range(2, 7)
        y = NotImplemented
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7, 2)')
        print('>>> y = NotImplemented')
        print('>>> x ^ y')
        x = range(2, 7, 2)
        y = NotImplemented
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -1)')
        print('>>> y = NotImplemented')
        print('>>> x ^ y')
        x = range(7, 2, -1)
        y = NotImplemented
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -2)')
        print('>>> y = NotImplemented')
        print('>>> x ^ y')
        x = range(7, 2, -2)
        y = NotImplemented
        print(x ^ y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()