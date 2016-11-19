def test_function():
    try:
        print('>>> f = help')
        print('>>> x = True')
        print('>>> f(x)')
        f = help
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = help')
        print('>>> x = False')
        print('>>> f(x)')
        f = help
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()