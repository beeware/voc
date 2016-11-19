def test_function():
    try:
        print('>>> x = 3')
        print('>>> y = NotImplemented')
        print('>>> x * y')
        x = 3
        y = NotImplemented
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 0')
        print('>>> y = NotImplemented')
        print('>>> x * y')
        x = 0
        y = NotImplemented
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -5')
        print('>>> y = NotImplemented')
        print('>>> x * y')
        x = -5
        y = NotImplemented
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -3')
        print('>>> y = NotImplemented')
        print('>>> x * y')
        x = -3
        y = NotImplemented
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 5')
        print('>>> y = NotImplemented')
        print('>>> x * y')
        x = 5
        y = NotImplemented
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 1')
        print('>>> y = NotImplemented')
        print('>>> x * y')
        x = 1
        y = NotImplemented
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()