def test_function():
    try:
        print('>>> f = str')
        print('>>> x = 3')
        print('>>> f(x)')
        f = str
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = str')
        print('>>> x = 0')
        print('>>> f(x)')
        f = str
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = str')
        print('>>> x = -5')
        print('>>> f(x)')
        f = str
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = str')
        print('>>> x = -3')
        print('>>> f(x)')
        f = str
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = str')
        print('>>> x = 5')
        print('>>> f(x)')
        f = str
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = str')
        print('>>> x = 1')
        print('>>> f(x)')
        f = str
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()