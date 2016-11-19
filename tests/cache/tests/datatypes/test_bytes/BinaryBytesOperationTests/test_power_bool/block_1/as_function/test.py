def test_function():
    try:
        print('>>> x = b""')
        print('>>> y = True')
        print('>>> x ** y')
        x = b""
        y = True
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = False')
        print('>>> x ** y')
        x = b""
        y = False
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = True')
        print('>>> x ** y')
        x = b"This is another string of bytes"
        y = True
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = False')
        print('>>> x ** y')
        x = b"This is another string of bytes"
        y = False
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()