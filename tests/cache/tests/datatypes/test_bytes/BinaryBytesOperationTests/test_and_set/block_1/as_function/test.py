def test_function():
    try:
        print('>>> x = b""')
        print('>>> y = set()')
        print('>>> x & y')
        x = b""
        y = set()
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x & y')
        x = b""
        y = {1, 2.3456, "another"}
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = set()')
        print('>>> x & y')
        x = b"This is another string of bytes"
        y = set()
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x & y')
        x = b"This is another string of bytes"
        y = {1, 2.3456, "another"}
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()