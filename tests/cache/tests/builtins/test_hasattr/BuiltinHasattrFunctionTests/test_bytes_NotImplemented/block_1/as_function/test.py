def test_function():
    try:
        print('>>> f = hasattr')
        print('>>> x = b""')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = hasattr
        x = b""
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hasattr')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = NotImplemented')
        print('>>> f(x, y)')
        f = hasattr
        x = b"This is another string of bytes"
        y = NotImplemented
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()