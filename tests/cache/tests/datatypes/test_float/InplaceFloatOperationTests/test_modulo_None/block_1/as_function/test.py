def test_function():
    try:
        print('>>> x = 2.3456')
        print('>>> y = None')
        print('>>> x %= y')
        print('>>> x')
        x = 2.3456
        y = None
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 0.0')
        print('>>> y = None')
        print('>>> x %= y')
        print('>>> x')
        x = 0.0
        y = None
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -3.14159')
        print('>>> y = None')
        print('>>> x %= y')
        print('>>> x')
        x = -3.14159
        y = None
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -4.81756')
        print('>>> y = None')
        print('>>> x %= y')
        print('>>> x')
        x = -4.81756
        y = None
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 5.5')
        print('>>> y = None')
        print('>>> x %= y')
        print('>>> x')
        x = 5.5
        y = None
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -3.5')
        print('>>> y = None')
        print('>>> x %= y')
        print('>>> x')
        x = -3.5
        y = None
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = 4.5')
        print('>>> y = None')
        print('>>> x %= y')
        print('>>> x')
        x = 4.5
        y = None
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = -4.5')
        print('>>> y = None')
        print('>>> x %= y')
        print('>>> x')
        x = -4.5
        y = None
        x %= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()