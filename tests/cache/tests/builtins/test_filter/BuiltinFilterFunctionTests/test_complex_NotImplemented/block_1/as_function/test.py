def test_function():
    try:
        print('>>> f = filter')
        print('>>> x = 1j')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = 1j
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = 3.14159265j')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = 3.14159265j
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = 1+2j')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = 1+2j
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = 3-4j')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = 3-4j
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = -5j')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = filter
        x = -5j
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()