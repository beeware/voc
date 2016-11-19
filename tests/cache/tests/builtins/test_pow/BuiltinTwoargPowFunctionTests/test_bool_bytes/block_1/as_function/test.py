def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = True')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = pow
        x = True
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = False')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = pow
        x = False
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()