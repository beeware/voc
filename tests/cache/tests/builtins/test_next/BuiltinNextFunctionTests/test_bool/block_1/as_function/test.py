def test_function():
    try:
        print('>>> f = next')
        print('>>> x = True')
        print('>>> f(x)')
        f = next
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = next')
        print('>>> x = False')
        print('>>> f(x)')
        f = next
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()