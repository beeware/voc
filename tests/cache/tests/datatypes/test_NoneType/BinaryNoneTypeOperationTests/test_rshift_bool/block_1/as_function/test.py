def test_function():
    try:
        print('>>> x = None')
        print('>>> y = True')
        print('>>> x >> y')
        x = None
        y = True
        print(x >> y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = False')
        print('>>> x >> y')
        x = None
        y = False
        print(x >> y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()