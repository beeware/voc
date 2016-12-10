def test_function():
    try:
        print('>>> f = staticmethod')
        print('>>> x = True')
        print('>>> f(x)')
        f = staticmethod
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = staticmethod')
        print('>>> x = False')
        print('>>> f(x)')
        f = staticmethod
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()