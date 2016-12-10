def test_function():
    try:
        print('>>> f = max')
        print('>>> x = 3')
        print('>>> f(x)')
        f = max
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = max')
        print('>>> x = 0')
        print('>>> f(x)')
        f = max
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = max')
        print('>>> x = -5')
        print('>>> f(x)')
        f = max
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = max')
        print('>>> x = -3')
        print('>>> f(x)')
        f = max
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = max')
        print('>>> x = 5')
        print('>>> f(x)')
        f = max
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = max')
        print('>>> x = 1')
        print('>>> f(x)')
        f = max
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()