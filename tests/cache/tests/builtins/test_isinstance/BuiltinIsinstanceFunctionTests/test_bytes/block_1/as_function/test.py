def test_function():
    try:
        print('>>> f = isinstance')
        print('>>> x = b""')
        print('>>> f(x)')
        f = isinstance
        x = b""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = isinstance')
        print('>>> x = b"This is another string of bytes"')
        print('>>> f(x)')
        f = isinstance
        x = b"This is another string of bytes"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()