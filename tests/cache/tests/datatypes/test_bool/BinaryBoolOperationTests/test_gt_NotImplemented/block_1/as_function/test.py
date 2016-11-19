def test_function():
    try:
        print('>>> x = True')
        print('>>> y = NotImplemented')
        print('>>> x > y')
        x = True
        y = NotImplemented
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = NotImplemented')
        print('>>> x > y')
        x = False
        y = NotImplemented
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()