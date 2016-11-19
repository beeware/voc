def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = []')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = divmod
        x = []
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = []')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = divmod
        x = []
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = []')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = divmod
        x = []
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = [3, 4, 5]')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = divmod
        x = [3, 4, 5]
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = [3, 4, 5]')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = divmod
        x = [3, 4, 5]
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = [3, 4, 5]')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = divmod
        x = [3, 4, 5]
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = divmod
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = divmod
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = divmod
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = ["a","b","c"]')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = divmod
        x = ["a","b","c"]
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = ["a","b","c"]')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = divmod
        x = ["a","b","c"]
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = ["a","b","c"]')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = divmod
        x = ["a","b","c"]
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()