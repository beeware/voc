def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = NotImplemented')
        print('>>> y = 1j')
        print('>>> f(x, y)')
        f = divmod
        x = NotImplemented
        y = 1j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = NotImplemented')
        print('>>> y = 3.14159265j')
        print('>>> f(x, y)')
        f = divmod
        x = NotImplemented
        y = 3.14159265j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = NotImplemented')
        print('>>> y = 1+2j')
        print('>>> f(x, y)')
        f = divmod
        x = NotImplemented
        y = 1+2j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = NotImplemented')
        print('>>> y = 3-4j')
        print('>>> f(x, y)')
        f = divmod
        x = NotImplemented
        y = 3-4j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = NotImplemented')
        print('>>> y = -5j')
        print('>>> f(x, y)')
        f = divmod
        x = NotImplemented
        y = -5j
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()