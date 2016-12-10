def test_function():
    try:
        print('>>> f = bytes')
        print('>>> x = True')
        print('>>> f(x)')
        f = bytes
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bytes')
        print('>>> x = False')
        print('>>> f(x)')
        f = bytes
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()