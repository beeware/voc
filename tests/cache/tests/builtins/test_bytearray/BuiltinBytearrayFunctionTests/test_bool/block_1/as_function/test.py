def test_function():
    try:
        print('>>> f = bytearray')
        print('>>> x = True')
        print('>>> f(x)')
        f = bytearray
        x = True
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bytearray')
        print('>>> x = False')
        print('>>> f(x)')
        f = bytearray
        x = False
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()