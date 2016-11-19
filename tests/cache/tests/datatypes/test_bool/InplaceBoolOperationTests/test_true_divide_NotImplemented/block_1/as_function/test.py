def test_function():
    try:
        print('>>> x = True')
        print('>>> y = NotImplemented')
        print('>>> x /= y')
        print('>>> x')
        x = True
        y = NotImplemented
        x /= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = NotImplemented')
        print('>>> x /= y')
        print('>>> x')
        x = False
        y = NotImplemented
        x /= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()