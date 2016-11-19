def test_function():
    try:
        print('>>> x = range(0)')
        print('>>> y = bytearray()')
        print('>>> x //= y')
        print('>>> x')
        x = range(0)
        y = bytearray()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(0)')
        print('>>> y = bytearray(1)')
        print('>>> x //= y')
        print('>>> x')
        x = range(0)
        y = bytearray(1)
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(0)')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x //= y')
        print('>>> x')
        x = range(0)
        y = bytearray([1, 2, 3])
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(5)')
        print('>>> y = bytearray()')
        print('>>> x //= y')
        print('>>> x')
        x = range(5)
        y = bytearray()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(5)')
        print('>>> y = bytearray(1)')
        print('>>> x //= y')
        print('>>> x')
        x = range(5)
        y = bytearray(1)
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(5)')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x //= y')
        print('>>> x')
        x = range(5)
        y = bytearray([1, 2, 3])
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7)')
        print('>>> y = bytearray()')
        print('>>> x //= y')
        print('>>> x')
        x = range(2, 7)
        y = bytearray()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7)')
        print('>>> y = bytearray(1)')
        print('>>> x //= y')
        print('>>> x')
        x = range(2, 7)
        y = bytearray(1)
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7)')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x //= y')
        print('>>> x')
        x = range(2, 7)
        y = bytearray([1, 2, 3])
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7, 2)')
        print('>>> y = bytearray()')
        print('>>> x //= y')
        print('>>> x')
        x = range(2, 7, 2)
        y = bytearray()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7, 2)')
        print('>>> y = bytearray(1)')
        print('>>> x //= y')
        print('>>> x')
        x = range(2, 7, 2)
        y = bytearray(1)
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(2, 7, 2)')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x //= y')
        print('>>> x')
        x = range(2, 7, 2)
        y = bytearray([1, 2, 3])
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -1)')
        print('>>> y = bytearray()')
        print('>>> x //= y')
        print('>>> x')
        x = range(7, 2, -1)
        y = bytearray()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -1)')
        print('>>> y = bytearray(1)')
        print('>>> x //= y')
        print('>>> x')
        x = range(7, 2, -1)
        y = bytearray(1)
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -1)')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x //= y')
        print('>>> x')
        x = range(7, 2, -1)
        y = bytearray([1, 2, 3])
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -2)')
        print('>>> y = bytearray()')
        print('>>> x //= y')
        print('>>> x')
        x = range(7, 2, -2)
        y = bytearray()
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -2)')
        print('>>> y = bytearray(1)')
        print('>>> x //= y')
        print('>>> x')
        x = range(7, 2, -2)
        y = bytearray(1)
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = range(7, 2, -2)')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> x //= y')
        print('>>> x')
        x = range(7, 2, -2)
        y = bytearray([1, 2, 3])
        x //= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()