def test_function():
    try:
        print('>>> f = hex')
        print('>>> x = 2.3456')
        print('>>> f(x)')
        f = hex
        x = 2.3456
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hex')
        print('>>> x = 0.0')
        print('>>> f(x)')
        f = hex
        x = 0.0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hex')
        print('>>> x = -3.14159')
        print('>>> f(x)')
        f = hex
        x = -3.14159
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hex')
        print('>>> x = -4.81756')
        print('>>> f(x)')
        f = hex
        x = -4.81756
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hex')
        print('>>> x = 5.5')
        print('>>> f(x)')
        f = hex
        x = 5.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hex')
        print('>>> x = -3.5')
        print('>>> f(x)')
        f = hex
        x = -3.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hex')
        print('>>> x = 4.5')
        print('>>> f(x)')
        f = hex
        x = 4.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hex')
        print('>>> x = -4.5')
        print('>>> f(x)')
        f = hex
        x = -4.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()