def test_function():
    try:
        print('>>> x = True')
        print('>>> y = True')
        print('>>> x == y')
        x = True
        y = True
        print(x == y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = False')
        print('>>> x == y')
        x = True
        y = False
        print(x == y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = True')
        print('>>> x == y')
        x = False
        y = True
        print(x == y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = False')
        print('>>> x == y')
        x = False
        y = False
        print(x == y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()