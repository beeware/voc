def test_function():
    try:
        print('>>> f = round')
        print('>>> x = True')
        print('>>> f(x)')
        f = round
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = round')
        print('>>> x = False')
        print('>>> f(x)')
        f = round
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()