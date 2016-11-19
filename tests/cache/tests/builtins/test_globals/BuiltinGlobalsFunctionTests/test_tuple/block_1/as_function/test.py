def test_function():
    try:
        print('>>> f = globals')
        print('>>> x = (1, 2)')
        print('>>> f(x)')
        f = globals
        x = (1, 2)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = globals')
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> f(x)')
        f = globals
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = globals')
        print('>>> x = (3, 1.2, True, )')
        print('>>> f(x)')
        f = globals
        x = (3, 1.2, True, )
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = globals')
        print('>>> x = (1, 2.3456, "another")')
        print('>>> f(x)')
        f = globals
        x = (1, 2.3456, "another")
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()