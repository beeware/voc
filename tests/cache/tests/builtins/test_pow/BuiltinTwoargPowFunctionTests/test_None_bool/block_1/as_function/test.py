def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = None')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = pow
        x = None
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = None')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = pow
        x = None
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()