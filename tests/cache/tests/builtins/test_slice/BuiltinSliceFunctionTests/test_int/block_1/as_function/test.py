def test_function():
    try:
        print('>>> f = slice')
        print('>>> x = 3')
        print('>>> f(x)')
        f = slice
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = slice')
        print('>>> x = 0')
        print('>>> f(x)')
        f = slice
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = slice')
        print('>>> x = -5')
        print('>>> f(x)')
        f = slice
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = slice')
        print('>>> x = -3')
        print('>>> f(x)')
        f = slice
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = slice')
        print('>>> x = 5')
        print('>>> f(x)')
        f = slice
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = slice')
        print('>>> x = 1')
        print('>>> f(x)')
        f = slice
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()