def test_function():
    try:
        print('>>> f = any')
        print('>>> x = 3')
        print('>>> f(x)')
        f = any
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = any')
        print('>>> x = 0')
        print('>>> f(x)')
        f = any
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = any')
        print('>>> x = -5')
        print('>>> f(x)')
        f = any
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = any')
        print('>>> x = -3')
        print('>>> f(x)')
        f = any
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = any')
        print('>>> x = 5')
        print('>>> f(x)')
        f = any
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = any')
        print('>>> x = 1')
        print('>>> f(x)')
        f = any
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()