def test_function():
    try:
        print('>>> x = b""')
        print('>>> y = []')
        print('>>> x + y')
        x = b""
        y = []
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = [3, 4, 5]')
        print('>>> x + y')
        x = b""
        y = [3, 4, 5]
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> x + y')
        x = b""
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b""')
        print('>>> y = ["a","b","c"]')
        print('>>> x + y')
        x = b""
        y = ["a","b","c"]
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = []')
        print('>>> x + y')
        x = b"This is another string of bytes"
        y = []
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = [3, 4, 5]')
        print('>>> x + y')
        x = b"This is another string of bytes"
        y = [3, 4, 5]
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> x + y')
        x = b"This is another string of bytes"
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = b"This is another string of bytes"')
        print('>>> y = ["a","b","c"]')
        print('>>> x + y')
        x = b"This is another string of bytes"
        y = ["a","b","c"]
        print(x + y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()