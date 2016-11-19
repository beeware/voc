def test_function():
    try:
        print('>>> f = super')
        print('>>> x = 1j')
        print('>>> f(x)')
        f = super
        x = 1j
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = super')
        print('>>> x = 3.14159265j')
        print('>>> f(x)')
        f = super
        x = 3.14159265j
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = super')
        print('>>> x = 1+2j')
        print('>>> f(x)')
        f = super
        x = 1+2j
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = super')
        print('>>> x = 3-4j')
        print('>>> f(x)')
        f = super
        x = 3-4j
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = super')
        print('>>> x = -5j')
        print('>>> f(x)')
        f = super
        x = -5j
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()