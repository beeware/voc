def test_function():
    try:
        print('>>> f = object')
        print('>>> x = 3')
        print('>>> f(x)')
        f = object
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = object')
        print('>>> x = 0')
        print('>>> f(x)')
        f = object
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = object')
        print('>>> x = -5')
        print('>>> f(x)')
        f = object
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = object')
        print('>>> x = -3')
        print('>>> f(x)')
        f = object
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = object')
        print('>>> x = 5')
        print('>>> f(x)')
        f = object
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = object')
        print('>>> x = 1')
        print('>>> f(x)')
        f = object
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()