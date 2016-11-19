def test_function():
    try:
        print('>>> f = bin')
        print('>>> x = True')
        print('>>> f(x)')
        f = bin
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bin')
        print('>>> x = False')
        print('>>> f(x)')
        f = bin
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()