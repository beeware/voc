def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = True')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = delattr
        x = True
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = False')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = delattr
        x = False
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()