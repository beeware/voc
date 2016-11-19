def test_function():
    try:
        print('>>> f = globals')
        print('>>> x = True')
        print('>>> f(x)')
        f = globals
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = globals')
        print('>>> x = False')
        print('>>> f(x)')
        f = globals
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()