def test_function():
    try:
        print('>>> f = sum')
        print('>>> x = range(0)')
        print('>>> f(x)')
        f = sum
        x = range(0)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = sum')
        print('>>> x = range(5)')
        print('>>> f(x)')
        f = sum
        x = range(5)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = sum')
        print('>>> x = range(2, 7)')
        print('>>> f(x)')
        f = sum
        x = range(2, 7)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = sum')
        print('>>> x = range(2, 7, 2)')
        print('>>> f(x)')
        f = sum
        x = range(2, 7, 2)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = sum')
        print('>>> x = range(7, 2, -1)')
        print('>>> f(x)')
        f = sum
        x = range(7, 2, -1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = sum')
        print('>>> x = range(7, 2, -2)')
        print('>>> f(x)')
        f = sum
        x = range(7, 2, -2)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()