def test_function():
    try:
        print('>>> f = eval')
        print('>>> x = slice(0)')
        print('>>> f(x)')
        f = eval
        x = slice(0)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = eval')
        print('>>> x = slice(5)')
        print('>>> f(x)')
        f = eval
        x = slice(5)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = eval')
        print('>>> x = slice(2, 7)')
        print('>>> f(x)')
        f = eval
        x = slice(2, 7)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = eval')
        print('>>> x = slice(2, 7, 2)')
        print('>>> f(x)')
        f = eval
        x = slice(2, 7, 2)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = eval')
        print('>>> x = slice(7, 2, -1)')
        print('>>> f(x)')
        f = eval
        x = slice(7, 2, -1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = eval')
        print('>>> x = slice(7, 2, -2)')
        print('>>> f(x)')
        f = eval
        x = slice(7, 2, -2)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()