def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = True')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = divmod
        x = True
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = False')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = divmod
        x = False
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()