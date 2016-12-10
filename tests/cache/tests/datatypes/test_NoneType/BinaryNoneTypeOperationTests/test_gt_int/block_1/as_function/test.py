def test_function():
    try:
        print('>>> x = None')
        print('>>> y = 3')
        print('>>> x > y')
        x = None
        y = 3
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = 0')
        print('>>> x > y')
        x = None
        y = 0
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = -5')
        print('>>> x > y')
        x = None
        y = -5
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = -3')
        print('>>> x > y')
        x = None
        y = -3
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = 5')
        print('>>> x > y')
        x = None
        y = 5
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = 1')
        print('>>> x > y')
        x = None
        y = 1
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()