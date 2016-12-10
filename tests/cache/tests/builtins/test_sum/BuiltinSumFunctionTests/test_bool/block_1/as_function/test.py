def test_function():
    try:
        print('>>> f = sum')
        print('>>> x = True')
        print('>>> f(x)')
        f = sum
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = sum')
        print('>>> x = False')
        print('>>> f(x)')
        f = sum
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()