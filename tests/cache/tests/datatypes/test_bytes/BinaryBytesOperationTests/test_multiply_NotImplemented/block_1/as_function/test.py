def test_function():
    try:
        print('>>> x = b""')
        print('>>> y = NotImplemented')
        print('>>> x * y')
        x = b""
        y = NotImplemented
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = NotImplemented')
        print('>>> x * y')
        x = b"This is another string of bytes"
        y = NotImplemented
        print(x * y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()