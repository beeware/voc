def test_function():
    try:
        print('>>> f = sorted')
        print('>>> x = True')
        print('>>> f(x)')
        f = sorted
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = sorted')
        print('>>> x = False')
        print('>>> f(x)')
        f = sorted
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()