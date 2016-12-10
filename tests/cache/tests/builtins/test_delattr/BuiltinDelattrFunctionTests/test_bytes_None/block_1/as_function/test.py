def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = b""')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = delattr
        x = b""
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = delattr
        x = b"This is another string of bytes"
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()