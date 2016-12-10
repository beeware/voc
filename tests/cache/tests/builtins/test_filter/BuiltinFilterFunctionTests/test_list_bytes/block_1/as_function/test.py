def test_function():
    try:
        print('>>> f = filter')
        print('>>> x = []')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = filter
        x = []
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = []')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = filter
        x = []
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = [3, 4, 5]')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = filter
        x = [3, 4, 5]
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = [3, 4, 5]')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = filter
        x = [3, 4, 5]
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = filter
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = filter
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = ["a","b","c"]')
        print('>>> y = b""')
        print('>>> f(x, y)')
        f = filter
        x = ["a","b","c"]
        y = b""
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = filter')
        print('>>> x = ["a","b","c"]')
        print('>>> y = b"This is another string of bytes"')
        print('>>> f(x, y)')
        f = filter
        x = ["a","b","c"]
        y = b"This is another string of bytes"
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()