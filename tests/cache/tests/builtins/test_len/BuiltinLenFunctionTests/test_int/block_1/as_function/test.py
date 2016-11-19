def test_function():
    try:
        print('>>> f = len')
        print('>>> x = 3')
        print('>>> f(x)')
        f = len
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = len')
        print('>>> x = 0')
        print('>>> f(x)')
        f = len
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = len')
        print('>>> x = -5')
        print('>>> f(x)')
        f = len
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = len')
        print('>>> x = -3')
        print('>>> f(x)')
        f = len
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = len')
        print('>>> x = 5')
        print('>>> f(x)')
        f = len
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = len')
        print('>>> x = 1')
        print('>>> f(x)')
        f = len
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()