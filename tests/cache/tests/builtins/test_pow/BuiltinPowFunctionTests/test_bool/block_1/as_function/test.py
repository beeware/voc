def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> f(x)')
        f = pow
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> f(x)')
        f = pow
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()