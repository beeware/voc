def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = set()')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = divmod
        x = set()
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = set()')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = divmod
        x = set()
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = divmod
        x = {1, 2.3456, "another"}
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = divmod
        x = {1, 2.3456, "another"}
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()