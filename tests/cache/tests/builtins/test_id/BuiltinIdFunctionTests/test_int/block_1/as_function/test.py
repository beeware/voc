def test_function():
    try:
        print('>>> f = id')
        print('>>> x = 3')
        print('>>> f(x)')
        f = id
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = id')
        print('>>> x = 0')
        print('>>> f(x)')
        f = id
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = id')
        print('>>> x = -5')
        print('>>> f(x)')
        f = id
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = id')
        print('>>> x = -3')
        print('>>> f(x)')
        f = id
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = id')
        print('>>> x = 5')
        print('>>> f(x)')
        f = id
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = id')
        print('>>> x = 1')
        print('>>> f(x)')
        f = id
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()