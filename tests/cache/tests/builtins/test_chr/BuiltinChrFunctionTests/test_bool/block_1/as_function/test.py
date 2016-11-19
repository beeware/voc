def test_function():
    try:
        print('>>> f = chr')
        print('>>> x = True')
        print('>>> f(x)')
        f = chr
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = chr')
        print('>>> x = False')
        print('>>> f(x)')
        f = chr
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()