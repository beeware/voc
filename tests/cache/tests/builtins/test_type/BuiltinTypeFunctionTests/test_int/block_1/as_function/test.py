def test_function():
    try:
        print('>>> f = type')
        print('>>> x = 3')
        print('>>> f(x)')
        f = type
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = type')
        print('>>> x = 0')
        print('>>> f(x)')
        f = type
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = type')
        print('>>> x = -5')
        print('>>> f(x)')
        f = type
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = type')
        print('>>> x = -3')
        print('>>> f(x)')
        f = type
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = type')
        print('>>> x = 5')
        print('>>> f(x)')
        f = type
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = type')
        print('>>> x = 1')
        print('>>> f(x)')
        f = type
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()