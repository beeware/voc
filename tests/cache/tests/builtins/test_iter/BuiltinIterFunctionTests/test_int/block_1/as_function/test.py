def test_function():
    try:
        print('>>> f = iter')
        print('>>> x = 3')
        print('>>> f(x)')
        f = iter
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = iter')
        print('>>> x = 0')
        print('>>> f(x)')
        f = iter
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = iter')
        print('>>> x = -5')
        print('>>> f(x)')
        f = iter
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = iter')
        print('>>> x = -3')
        print('>>> f(x)')
        f = iter
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = iter')
        print('>>> x = 5')
        print('>>> f(x)')
        f = iter
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = iter')
        print('>>> x = 1')
        print('>>> f(x)')
        f = iter
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()