def test_function():
    try:
        print('>>> x = 3')
        print('>>> y = NotImplemented')
        print('>>> x /= y')
        print('>>> x')
        x = 3
        y = NotImplemented
        x /= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 0')
        print('>>> y = NotImplemented')
        print('>>> x /= y')
        print('>>> x')
        x = 0
        y = NotImplemented
        x /= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -5')
        print('>>> y = NotImplemented')
        print('>>> x /= y')
        print('>>> x')
        x = -5
        y = NotImplemented
        x /= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -3')
        print('>>> y = NotImplemented')
        print('>>> x /= y')
        print('>>> x')
        x = -3
        y = NotImplemented
        x /= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 5')
        print('>>> y = NotImplemented')
        print('>>> x /= y')
        print('>>> x')
        x = 5
        y = NotImplemented
        x /= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 1')
        print('>>> y = NotImplemented')
        print('>>> x /= y')
        print('>>> x')
        x = 1
        y = NotImplemented
        x /= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()