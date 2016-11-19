def test_function():
    try:
        print('>>> f = dict')
        print('>>> x = b""')
        print('>>> f(x)')
        f = dict
        x = b""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = dict')
        print('>>> x = b"This is another string of bytes"')
        print('>>> f(x)')
        f = dict
        x = b"This is another string of bytes"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()