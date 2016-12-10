def test_function():
    try:
        print('>>> x = []')
        print('>>> y = bytearray()')
        print('>>> x ** y')
        x = []
        y = bytearray()
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = bytearray(1)')
        print('>>> x ** y')
        x = []
        y = bytearray(1)
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x ** y')
        x = []
        y = bytearray([1, 2, 3])
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = bytearray()')
        print('>>> x ** y')
        x = [3, 4, 5]
        y = bytearray()
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = bytearray(1)')
        print('>>> x ** y')
        x = [3, 4, 5]
        y = bytearray(1)
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x ** y')
        x = [3, 4, 5]
        y = bytearray([1, 2, 3])
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = bytearray()')
        print('>>> x ** y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = bytearray()
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = bytearray(1)')
        print('>>> x ** y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = bytearray(1)
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x ** y')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = bytearray([1, 2, 3])
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = bytearray()')
        print('>>> x ** y')
        x = ["a","b","c"]
        y = bytearray()
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = bytearray(1)')
        print('>>> x ** y')
        x = ["a","b","c"]
        y = bytearray(1)
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x ** y')
        x = ["a","b","c"]
        y = bytearray([1, 2, 3])
        print(x ** y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()