def test_function():
    try:
        print('>>> x = b""')
        print('>>> not x')
        x = b""
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> not x')
        x = b"This is another string of bytes"
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()