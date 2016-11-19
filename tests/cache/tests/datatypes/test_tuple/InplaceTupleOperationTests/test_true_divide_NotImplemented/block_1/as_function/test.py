def test_function():
    try:
        print('>>> x = (1, 2)')
        print('>>> y = NotImplemented')
        print('>>> x /= y')
        print('>>> x')
        x = (1, 2)
        y = NotImplemented
        x /= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = NotImplemented')
        print('>>> x /= y')
        print('>>> x')
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = NotImplemented
        x /= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = NotImplemented')
        print('>>> x /= y')
        print('>>> x')
        x = (3, 1.2, True, )
        y = NotImplemented
        x /= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = NotImplemented')
        print('>>> x /= y')
        print('>>> x')
        x = (1, 2.3456, "another")
        y = NotImplemented
        x /= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()