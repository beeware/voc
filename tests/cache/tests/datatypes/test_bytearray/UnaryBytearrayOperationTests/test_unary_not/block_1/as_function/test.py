def test_function():
    try:
        print('>>> x = bytearray()')
        print('>>> not x')
        x = bytearray()
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray(1)')
        print('>>> not x')
        x = bytearray(1)
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> not x')
        x = bytearray([1, 2, 3])
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()