def test_function():
    try:
        print('>>> f = bool')
        print('>>> x = 3')
        print('>>> f(x)')
        f = bool
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bool')
        print('>>> x = 0')
        print('>>> f(x)')
        f = bool
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bool')
        print('>>> x = -5')
        print('>>> f(x)')
        f = bool
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bool')
        print('>>> x = -3')
        print('>>> f(x)')
        f = bool
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bool')
        print('>>> x = 5')
        print('>>> f(x)')
        f = bool
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bool')
        print('>>> x = 1')
        print('>>> f(x)')
        f = bool
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()