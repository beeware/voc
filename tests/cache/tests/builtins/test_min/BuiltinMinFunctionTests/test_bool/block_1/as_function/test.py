def test_function():
    try:
        print('>>> f = min')
        print('>>> x = True')
        print('>>> f(x)')
        f = min
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = min')
        print('>>> x = False')
        print('>>> f(x)')
        f = min
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()