def test_function():
    try:
        print('>>> x = b""')
        print('>>> y = NotImplemented')
        print('>>> x *= y')
        print('>>> x')
        x = b""
        y = NotImplemented
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = NotImplemented')
        print('>>> x *= y')
        print('>>> x')
        x = b"This is another string of bytes"
        y = NotImplemented
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()