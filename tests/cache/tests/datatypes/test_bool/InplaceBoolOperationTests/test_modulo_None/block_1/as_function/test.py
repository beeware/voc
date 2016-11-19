def test_function():
    try:
        print('>>> x = True')
        print('>>> y = None')
        print('>>> x %= y')
        print('>>> x')
        x = True
        y = None
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = None')
        print('>>> x %= y')
        print('>>> x')
        x = False
        y = None
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()