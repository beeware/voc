def test_function():
    try:
        print('>>> x = range(0)')
        print('>>> -x')
        x = range(0)
        print(-x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(5)')
        print('>>> -x')
        x = range(5)
        print(-x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7)')
        print('>>> -x')
        x = range(2, 7)
        print(-x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7, 2)')
        print('>>> -x')
        x = range(2, 7, 2)
        print(-x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -1)')
        print('>>> -x')
        x = range(7, 2, -1)
        print(-x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -2)')
        print('>>> -x')
        x = range(7, 2, -2)
        print(-x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()