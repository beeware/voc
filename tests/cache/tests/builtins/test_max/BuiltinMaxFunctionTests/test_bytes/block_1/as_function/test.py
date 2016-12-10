def test_function():
    try:
        print('>>> f = max')
        print('>>> x = b""')
        print('>>> f(x)')
        f = max
        x = b""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = max')
        print('>>> x = b"This is another string of bytes"')
        print('>>> f(x)')
        f = max
        x = b"This is another string of bytes"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()