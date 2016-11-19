def test_function():
    try:
        print('>>> x = NotImplemented')
        print('>>> y = 3')
        print('>>> x ** y')
        x = NotImplemented
        y = 3
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = 0')
        print('>>> x ** y')
        x = NotImplemented
        y = 0
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = -5')
        print('>>> x ** y')
        x = NotImplemented
        y = -5
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = -3')
        print('>>> x ** y')
        x = NotImplemented
        y = -3
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = 5')
        print('>>> x ** y')
        x = NotImplemented
        y = 5
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = 1')
        print('>>> x ** y')
        x = NotImplemented
        y = 1
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()