def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()