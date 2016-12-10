def test_function():
    try:
        print('>>> x = (1, 2)')
        print('>>> y = bytearray()')
        print('>>> x //= y')
        print('>>> x')
        x = (1, 2)
        y = bytearray()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2)')
        print('>>> y = bytearray(1)')
        print('>>> x //= y')
        print('>>> x')
        x = (1, 2)
        y = bytearray(1)
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2)')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x //= y')
        print('>>> x')
        x = (1, 2)
        y = bytearray([1, 2, 3])
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = bytearray()')
        print('>>> x //= y')
        print('>>> x')
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = bytearray()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = bytearray(1)')
        print('>>> x //= y')
        print('>>> x')
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = bytearray(1)
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x //= y')
        print('>>> x')
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        y = bytearray([1, 2, 3])
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = bytearray()')
        print('>>> x //= y')
        print('>>> x')
        x = (3, 1.2, True, )
        y = bytearray()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = bytearray(1)')
        print('>>> x //= y')
        print('>>> x')
        x = (3, 1.2, True, )
        y = bytearray(1)
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (3, 1.2, True, )')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x //= y')
        print('>>> x')
        x = (3, 1.2, True, )
        y = bytearray([1, 2, 3])
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = bytearray()')
        print('>>> x //= y')
        print('>>> x')
        x = (1, 2.3456, "another")
        y = bytearray()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = bytearray(1)')
        print('>>> x //= y')
        print('>>> x')
        x = (1, 2.3456, "another")
        y = bytearray(1)
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2.3456, "another")')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x //= y')
        print('>>> x')
        x = (1, 2.3456, "another")
        y = bytearray([1, 2, 3])
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()