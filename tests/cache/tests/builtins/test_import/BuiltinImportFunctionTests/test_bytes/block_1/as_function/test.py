def test_function():
    try:
        print('>>> f = __import__')
        print('>>> x = b""')
        print('>>> f(x)')
        f = __import__
        x = b""
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = __import__')
        print('>>> x = b"This is another string of bytes"')
        print('>>> f(x)')
        f = __import__
        x = b"This is another string of bytes"
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()