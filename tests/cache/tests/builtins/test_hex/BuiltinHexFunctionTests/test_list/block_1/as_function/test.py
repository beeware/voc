def test_function():
    try:
        print('>>> f = hex')
        print('>>> x = []')
        print('>>> f(x)')
        f = hex
        x = []
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hex')
        print('>>> x = [3, 4, 5]')
        print('>>> f(x)')
        f = hex
        x = [3, 4, 5]
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hex')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> f(x)')
        f = hex
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = hex')
        print('>>> x = ["a","b","c"]')
        print('>>> f(x)')
        f = hex
        x = ["a","b","c"]
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()