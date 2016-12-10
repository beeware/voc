def test_function():
    try:
        print('>>> f = map')
        print('>>> x = True')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = map
        x = True
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = True')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = map
        x = True
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = False')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = map
        x = False
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = False')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = map
        x = False
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()