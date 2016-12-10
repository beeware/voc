def test_function():
    try:
        print('>>> f = eval')
        print('>>> x = 2.3456')
        print('>>> f(x)')
        f = eval
        x = 2.3456
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = eval')
        print('>>> x = 0.0')
        print('>>> f(x)')
        f = eval
        x = 0.0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = eval')
        print('>>> x = -3.14159')
        print('>>> f(x)')
        f = eval
        x = -3.14159
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = eval')
        print('>>> x = -4.81756')
        print('>>> f(x)')
        f = eval
        x = -4.81756
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = eval')
        print('>>> x = 5.5')
        print('>>> f(x)')
        f = eval
        x = 5.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = eval')
        print('>>> x = -3.5')
        print('>>> f(x)')
        f = eval
        x = -3.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = eval')
        print('>>> x = 4.5')
        print('>>> f(x)')
        f = eval
        x = 4.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = eval')
        print('>>> x = -4.5')
        print('>>> f(x)')
        f = eval
        x = -4.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()