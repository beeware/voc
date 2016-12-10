def test_function():
    try:
        print('>>> x = bytearray()')
        print('>>> y = []')
        print('>>> x > y')
        x = bytearray()
        y = []
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray()')
        print('>>> y = [3, 4, 5]')
        print('>>> x > y')
        x = bytearray()
        y = [3, 4, 5]
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray()')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> x > y')
        x = bytearray()
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray()')
        print('>>> y = ["a","b","c"]')
        print('>>> x > y')
        x = bytearray()
        y = ["a","b","c"]
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = []')
        print('>>> x > y')
        x = bytearray(1)
        y = []
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = [3, 4, 5]')
        print('>>> x > y')
        x = bytearray(1)
        y = [3, 4, 5]
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> x > y')
        x = bytearray(1)
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> y = ["a","b","c"]')
        print('>>> x > y')
        x = bytearray(1)
        y = ["a","b","c"]
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = []')
        print('>>> x > y')
        x = bytearray([1, 2, 3])
        y = []
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = [3, 4, 5]')
        print('>>> x > y')
        x = bytearray([1, 2, 3])
        y = [3, 4, 5]
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> x > y')
        x = bytearray([1, 2, 3])
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = ["a","b","c"]')
        print('>>> x > y')
        x = bytearray([1, 2, 3])
        y = ["a","b","c"]
        print(x > y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()