def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray()')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray()
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray(1)')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray(1)
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = divmod')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = None')
        print('>>> f(x, y)')
        f = divmod
        x = bytearray([1, 2, 3])
        y = None
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()