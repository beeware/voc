def test_function():
    try:
        print('>>> f = classmethod')
        print('>>> x = 3')
        print('>>> f(x)')
        f = classmethod
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = classmethod')
        print('>>> x = 0')
        print('>>> f(x)')
        f = classmethod
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = classmethod')
        print('>>> x = -5')
        print('>>> f(x)')
        f = classmethod
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = classmethod')
        print('>>> x = -3')
        print('>>> f(x)')
        f = classmethod
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = classmethod')
        print('>>> x = 5')
        print('>>> f(x)')
        f = classmethod
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = classmethod')
        print('>>> x = 1')
        print('>>> f(x)')
        f = classmethod
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()