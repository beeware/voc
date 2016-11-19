def test_function():
    try:
        print('>>> f = range')
        print('>>> x = range(0)')
        print('>>> f(x)')
        f = range
        x = range(0)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = range')
        print('>>> x = range(5)')
        print('>>> f(x)')
        f = range
        x = range(5)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = range')
        print('>>> x = range(2, 7)')
        print('>>> f(x)')
        f = range
        x = range(2, 7)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = range')
        print('>>> x = range(2, 7, 2)')
        print('>>> f(x)')
        f = range
        x = range(2, 7, 2)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = range')
        print('>>> x = range(7, 2, -1)')
        print('>>> f(x)')
        f = range
        x = range(7, 2, -1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = range')
        print('>>> x = range(7, 2, -2)')
        print('>>> f(x)')
        f = range
        x = range(7, 2, -2)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()