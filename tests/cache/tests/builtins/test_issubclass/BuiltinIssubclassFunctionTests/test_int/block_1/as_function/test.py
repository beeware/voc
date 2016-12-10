def test_function():
    try:
        print('>>> f = issubclass')
        print('>>> x = 3')
        print('>>> f(x)')
        f = issubclass
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = issubclass')
        print('>>> x = 0')
        print('>>> f(x)')
        f = issubclass
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = issubclass')
        print('>>> x = -5')
        print('>>> f(x)')
        f = issubclass
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = issubclass')
        print('>>> x = -3')
        print('>>> f(x)')
        f = issubclass
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = issubclass')
        print('>>> x = 5')
        print('>>> f(x)')
        f = issubclass
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = issubclass')
        print('>>> x = 1')
        print('>>> f(x)')
        f = issubclass
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()