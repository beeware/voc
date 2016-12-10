def test_function():
    try:
        print('>>> f = hasattr')
        print('>>> x = True')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = hasattr
        x = True
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = False')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = hasattr
        x = False
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()