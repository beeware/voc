def test_function():
    try:
        print('>>> x = b""')
        print('>>> y = set()')
        print('>>> x += y')
        print('>>> x')
        x = b""
        y = set()
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x += y')
        print('>>> x')
        x = b""
        y = {1, 2.3456, "another"}
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = set()')
        print('>>> x += y')
        print('>>> x')
        x = b"This is another string of bytes"
        y = set()
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x += y')
        print('>>> x')
        x = b"This is another string of bytes"
        y = {1, 2.3456, "another"}
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()