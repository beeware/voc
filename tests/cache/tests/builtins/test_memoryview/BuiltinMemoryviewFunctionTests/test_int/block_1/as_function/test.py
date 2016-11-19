def test_function():
    try:
        print('>>> f = memoryview')
        print('>>> x = 3')
        print('>>> f(x)')
        f = memoryview
        x = 3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = memoryview')
        print('>>> x = 0')
        print('>>> f(x)')
        f = memoryview
        x = 0
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = memoryview')
        print('>>> x = -5')
        print('>>> f(x)')
        f = memoryview
        x = -5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = memoryview')
        print('>>> x = -3')
        print('>>> f(x)')
        f = memoryview
        x = -3
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = memoryview')
        print('>>> x = 5')
        print('>>> f(x)')
        f = memoryview
        x = 5
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = memoryview')
        print('>>> x = 1')
        print('>>> f(x)')
        f = memoryview
        x = 1
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()