def test_function():
    try:
        print('>>> x = NotImplemented')
        print('>>> y = True')
        print('>>> x <<= y')
        print('>>> x')
        x = NotImplemented
        y = True
        x <<= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = False')
        print('>>> x <<= y')
        print('>>> x')
        x = NotImplemented
        y = False
        x <<= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()