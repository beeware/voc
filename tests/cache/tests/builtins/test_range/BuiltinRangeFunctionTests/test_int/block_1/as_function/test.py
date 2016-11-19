def test_function():
    try:
        print('>>> f = range')
        print('>>> x = 3')
        print('>>> f(x)')
        f = range
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = range')
        print('>>> x = 0')
        print('>>> f(x)')
        f = range
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = range')
        print('>>> x = -5')
        print('>>> f(x)')
        f = range
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = range')
        print('>>> x = -3')
        print('>>> f(x)')
        f = range
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = range')
        print('>>> x = 5')
        print('>>> f(x)')
        f = range
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = range')
        print('>>> x = 1')
        print('>>> f(x)')
        f = range
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()