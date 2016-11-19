def test_function():
    try:
        print('>>> f = callable')
        print('>>> x = 3')
        print('>>> f(x)')
        f = callable
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = callable')
        print('>>> x = 0')
        print('>>> f(x)')
        f = callable
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = callable')
        print('>>> x = -5')
        print('>>> f(x)')
        f = callable
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = callable')
        print('>>> x = -3')
        print('>>> f(x)')
        f = callable
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = callable')
        print('>>> x = 5')
        print('>>> f(x)')
        f = callable
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = callable')
        print('>>> x = 1')
        print('>>> f(x)')
        f = callable
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()