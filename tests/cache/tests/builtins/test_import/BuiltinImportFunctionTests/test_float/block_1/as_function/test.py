def test_function():
    try:
        print('>>> f = __import__')
        print('>>> x = 2.3456')
        print('>>> f(x)')
        f = __import__
        x = 2.3456
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = __import__')
        print('>>> x = 0.0')
        print('>>> f(x)')
        f = __import__
        x = 0.0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = __import__')
        print('>>> x = -3.14159')
        print('>>> f(x)')
        f = __import__
        x = -3.14159
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = __import__')
        print('>>> x = -4.81756')
        print('>>> f(x)')
        f = __import__
        x = -4.81756
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = __import__')
        print('>>> x = 5.5')
        print('>>> f(x)')
        f = __import__
        x = 5.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = __import__')
        print('>>> x = -3.5')
        print('>>> f(x)')
        f = __import__
        x = -3.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = __import__')
        print('>>> x = 4.5')
        print('>>> f(x)')
        f = __import__
        x = 4.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = __import__')
        print('>>> x = -4.5')
        print('>>> f(x)')
        f = __import__
        x = -4.5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()