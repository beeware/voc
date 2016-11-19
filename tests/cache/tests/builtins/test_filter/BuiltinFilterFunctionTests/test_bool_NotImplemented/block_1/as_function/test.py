def test_function():
    try:
        print('>>> f = filter')
        print('>>> x = True')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = True
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = False')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = False
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()