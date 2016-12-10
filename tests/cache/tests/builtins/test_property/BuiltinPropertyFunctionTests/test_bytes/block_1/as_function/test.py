def test_function():
    try:
        print('>>> f = property')
        print('>>> x = b""')
        print('>>> f(x)')
        f = property
        x = b""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = property')
        print('>>> x = b"This is another string of bytes"')
        print('>>> f(x)')
        f = property
        x = b"This is another string of bytes"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()