def test_function():
    try:
        print('>>> f = type')
        print('>>> x = b""')
        print('>>> f(x)')
        f = type
        x = b""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = type')
        print('>>> x = b"This is another string of bytes"')
        print('>>> f(x)')
        f = type
        x = b"This is another string of bytes"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()