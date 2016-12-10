def test_function():
    try:
        print('>>> x = NotImplemented')
        print('>>> y = b""')
        print('>>> x /= y')
        print('>>> x')
        x = NotImplemented
        y = b""
        x /= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = b"This is another string of bytes"')
        print('>>> x /= y')
        print('>>> x')
        x = NotImplemented
        y = b"This is another string of bytes"
        x /= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()