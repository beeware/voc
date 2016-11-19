def test_function():
    try:
        print('>>> f = enumerate')
        print('>>> x = bytearray()')
        print('>>> f(x)')
        f = enumerate
        x = bytearray()
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = enumerate')
        print('>>> x = bytearray(1)')
        print('>>> f(x)')
        f = enumerate
        x = bytearray(1)
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = enumerate')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> f(x)')
        f = enumerate
        x = bytearray([1, 2, 3])
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()