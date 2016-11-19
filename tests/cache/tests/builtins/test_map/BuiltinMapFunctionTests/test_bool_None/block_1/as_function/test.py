def test_function():
    try:
        print('>>> f = map')
        print('>>> x = True')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = map
        x = True
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = False')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = map
        x = False
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()