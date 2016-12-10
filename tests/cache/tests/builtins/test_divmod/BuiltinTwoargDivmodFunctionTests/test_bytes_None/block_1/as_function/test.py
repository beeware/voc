def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = b""')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = divmod
        x = b""
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = divmod
        x = b"This is another string of bytes"
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()