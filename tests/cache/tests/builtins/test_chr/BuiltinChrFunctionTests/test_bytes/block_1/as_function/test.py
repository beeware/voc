def test_function():
    try:
        print('>>> f = chr')
        print('>>> x = b""')
        print('>>> f(x)')
        f = chr
        x = b""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = chr')
        print('>>> x = b"This is another string of bytes"')
        print('>>> f(x)')
        f = chr
        x = b"This is another string of bytes"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()