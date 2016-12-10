def test_function():
    try:
        print('>>> f = open')
        print('>>> x = True')
        print('>>> f(x)')
        f = open
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = open')
        print('>>> x = False')
        print('>>> f(x)')
        f = open
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()