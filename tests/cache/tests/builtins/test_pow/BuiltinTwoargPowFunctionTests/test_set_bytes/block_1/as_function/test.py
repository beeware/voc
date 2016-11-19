def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = set()')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = pow
        x = set()
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = set()')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = pow
        x = set()
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = pow
        x = {1, 2.3456, "another"}
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = pow
        x = {1, 2.3456, "another"}
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()