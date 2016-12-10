def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = True')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = getattr
        x = True
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = False')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = getattr
        x = False
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()