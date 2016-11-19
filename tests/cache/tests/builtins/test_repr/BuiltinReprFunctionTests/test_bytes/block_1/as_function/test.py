def test_function():
    try:
        print('>>> f = repr')
        print('>>> x = b""')
        print('>>> f(x)')
        f = repr
        x = b""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = repr')
        print('>>> x = b"This is another string of bytes"')
        print('>>> f(x)')
        f = repr
        x = b"This is another string of bytes"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()