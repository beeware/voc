def test_function():
    try:
        print('>>> f = all')
        print('>>> x = 3')
        print('>>> f(x)')
        f = all
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = all')
        print('>>> x = 0')
        print('>>> f(x)')
        f = all
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = all')
        print('>>> x = -5')
        print('>>> f(x)')
        f = all
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = all')
        print('>>> x = -3')
        print('>>> f(x)')
        f = all
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = all')
        print('>>> x = 5')
        print('>>> f(x)')
        f = all
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = all')
        print('>>> x = 1')
        print('>>> f(x)')
        f = all
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()