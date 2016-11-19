def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = NotImplemented')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = delattr
        x = NotImplemented
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = NotImplemented')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = delattr
        x = NotImplemented
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()