def test_function():
    try:
        print('>>> f = bytearray')
        print('>>> x = []')
        print('>>> f(x)')
        f = bytearray
        x = []
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bytearray')
        print('>>> x = [3, 4, 5]')
        print('>>> f(x)')
        f = bytearray
        x = [3, 4, 5]
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bytearray')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> f(x)')
        f = bytearray
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = bytearray')
        print('>>> x = ["a","b","c"]')
        print('>>> f(x)')
        f = bytearray
        x = ["a","b","c"]
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()