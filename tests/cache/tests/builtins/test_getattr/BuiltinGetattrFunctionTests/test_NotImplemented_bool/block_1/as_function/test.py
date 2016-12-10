def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = NotImplemented')
        print('>>> y = True')
        print('>>> f(x, y)')
        f = getattr
        x = NotImplemented
        y = True
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = NotImplemented')
        print('>>> y = False')
        print('>>> f(x, y)')
        f = getattr
        x = NotImplemented
        y = False
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()