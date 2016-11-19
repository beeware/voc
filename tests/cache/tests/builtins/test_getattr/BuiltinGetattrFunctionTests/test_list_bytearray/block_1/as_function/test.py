def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = []')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = getattr
        x = []
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = []')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = getattr
        x = []
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = []')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = getattr
        x = []
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = [3, 4, 5]')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = getattr
        x = [3, 4, 5]
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = [3, 4, 5]')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = getattr
        x = [3, 4, 5]
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = [3, 4, 5]')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = getattr
        x = [3, 4, 5]
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = getattr
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = getattr
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = getattr
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = ["a","b","c"]')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = getattr
        x = ["a","b","c"]
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = ["a","b","c"]')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = getattr
        x = ["a","b","c"]
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = ["a","b","c"]')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = getattr
        x = ["a","b","c"]
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()