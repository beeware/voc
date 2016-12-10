def test_function():
    try:
        print('>>> x = None')
        print('>>> y = b""')
        print('>>> x //= y')
        print('>>> x')
        x = None
        y = b""
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = b"This is another string of bytes"')
        print('>>> x //= y')
        print('>>> x')
        x = None
        y = b"This is another string of bytes"
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()