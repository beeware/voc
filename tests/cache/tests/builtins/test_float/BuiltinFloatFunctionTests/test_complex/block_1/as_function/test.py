def test_function():
    try:
        print('>>> f = float')
        print('>>> x = 1j')
        print('>>> f(x)')
        f = float
        x = 1j
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = float')
        print('>>> x = 3.14159265j')
        print('>>> f(x)')
        f = float
        x = 3.14159265j
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = float')
        print('>>> x = 1+2j')
        print('>>> f(x)')
        f = float
        x = 1+2j
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = float')
        print('>>> x = 3-4j')
        print('>>> f(x)')
        f = float
        x = 3-4j
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = float')
        print('>>> x = -5j')
        print('>>> f(x)')
        f = float
        x = -5j
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()