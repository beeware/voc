def test_function():
    try:
        print('>>> f = format')
        print('>>> x = b""')
        print('>>> f(x)')
        f = format
        x = b""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = format')
        print('>>> x = b"This is another string of bytes"')
        print('>>> f(x)')
        f = format
        x = b"This is another string of bytes"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()