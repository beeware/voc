def test_function():
    try:
        print('>>> f = reversed')
        print('>>> x = True')
        print('>>> f(x)')
        f = reversed
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = reversed')
        print('>>> x = False')
        print('>>> f(x)')
        f = reversed
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()