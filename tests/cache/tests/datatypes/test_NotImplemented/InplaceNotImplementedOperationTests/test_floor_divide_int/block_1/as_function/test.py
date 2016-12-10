def test_function():
    try:
        print('>>> x = NotImplemented')
        print('>>> y = 3')
        print('>>> x //= y')
        print('>>> x')
        x = NotImplemented
        y = 3
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = 0')
        print('>>> x //= y')
        print('>>> x')
        x = NotImplemented
        y = 0
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = -5')
        print('>>> x //= y')
        print('>>> x')
        x = NotImplemented
        y = -5
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = -3')
        print('>>> x //= y')
        print('>>> x')
        x = NotImplemented
        y = -3
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = 5')
        print('>>> x //= y')
        print('>>> x')
        x = NotImplemented
        y = 5
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = 1')
        print('>>> x //= y')
        print('>>> x')
        x = NotImplemented
        y = 1
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()