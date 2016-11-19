def test_function():
    try:
        print('>>> f = compile')
        print('>>> x = 2.3456')
        print('>>> f(x)')
        f = compile
        x = 2.3456
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = 0.0')
        print('>>> f(x)')
        f = compile
        x = 0.0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = -3.14159')
        print('>>> f(x)')
        f = compile
        x = -3.14159
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = -4.81756')
        print('>>> f(x)')
        f = compile
        x = -4.81756
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = 5.5')
        print('>>> f(x)')
        f = compile
        x = 5.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = -3.5')
        print('>>> f(x)')
        f = compile
        x = -3.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = 4.5')
        print('>>> f(x)')
        f = compile
        x = 4.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = compile')
        print('>>> x = -4.5')
        print('>>> f(x)')
        f = compile
        x = -4.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()