def test_function():
    try:
        print('>>> f = round')
        print('>>> x = 3')
        print('>>> f(x)')
        f = round
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = round')
        print('>>> x = 0')
        print('>>> f(x)')
        f = round
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = round')
        print('>>> x = -5')
        print('>>> f(x)')
        f = round
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = round')
        print('>>> x = -3')
        print('>>> f(x)')
        f = round
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = round')
        print('>>> x = 5')
        print('>>> f(x)')
        f = round
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = round')
        print('>>> x = 1')
        print('>>> f(x)')
        f = round
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()