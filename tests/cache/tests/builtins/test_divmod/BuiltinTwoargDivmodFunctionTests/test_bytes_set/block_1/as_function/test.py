def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = b""')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = divmod
        x = b""
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = b""')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = divmod
        x = b""
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = divmod
        x = b"This is another string of bytes"
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = divmod
        x = b"This is another string of bytes"
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()