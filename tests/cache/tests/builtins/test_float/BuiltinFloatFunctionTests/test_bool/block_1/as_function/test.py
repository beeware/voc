def test_function():
    try:
        print('>>> f = float')
        print('>>> x = True')
        print('>>> f(x)')
        f = float
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = float')
        print('>>> x = False')
        print('>>> f(x)')
        f = float
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()