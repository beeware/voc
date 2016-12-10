def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = b""')
        print('>>> f(x)')
        f = divmod
        x = b""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = b"This is another string of bytes"')
        print('>>> f(x)')
        f = divmod
        x = b"This is another string of bytes"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()