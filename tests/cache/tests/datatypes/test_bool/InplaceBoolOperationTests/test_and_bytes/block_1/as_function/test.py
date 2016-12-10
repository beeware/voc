def test_function():
    try:
        print('>>> x = True')
        print('>>> y = b""')
        print('>>> x &= y')
        print('>>> x')
        x = True
        y = b""
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = b"This is another string of bytes"')
        print('>>> x &= y')
        print('>>> x')
        x = True
        y = b"This is another string of bytes"
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = b""')
        print('>>> x &= y')
        print('>>> x')
        x = False
        y = b""
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = b"This is another string of bytes"')
        print('>>> x &= y')
        print('>>> x')
        x = False
        y = b"This is another string of bytes"
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()