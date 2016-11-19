def test_function():
    try:
        print('>>> f = bin')
        print('>>> x = 3')
        print('>>> f(x)')
        f = bin
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bin')
        print('>>> x = 0')
        print('>>> f(x)')
        f = bin
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bin')
        print('>>> x = -5')
        print('>>> f(x)')
        f = bin
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bin')
        print('>>> x = -3')
        print('>>> f(x)')
        f = bin
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bin')
        print('>>> x = 5')
        print('>>> f(x)')
        f = bin
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bin')
        print('>>> x = 1')
        print('>>> f(x)')
        f = bin
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()