def test_function():
    try:
        print('>>> f = len')
        print('>>> x = True')
        print('>>> f(x)')
        f = len
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = len')
        print('>>> x = False')
        print('>>> f(x)')
        f = len
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()