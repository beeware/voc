def test_function():
    try:
        print('>>> f = hex')
        print('>>> x = b""')
        print('>>> f(x)')
        f = hex
        x = b""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hex')
        print('>>> x = b"This is another string of bytes"')
        print('>>> f(x)')
        f = hex
        x = b"This is another string of bytes"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()