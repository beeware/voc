def test_function():
    try:
        print('>>> f = oct')
        print('>>> x = b""')
        print('>>> f(x)')
        f = oct
        x = b""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = oct')
        print('>>> x = b"This is another string of bytes"')
        print('>>> f(x)')
        f = oct
        x = b"This is another string of bytes"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()