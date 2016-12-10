def test_function():
    try:
        print('>>> f = property')
        print('>>> x = []')
        print('>>> f(x)')
        f = property
        x = []
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = property')
        print('>>> x = [3, 4, 5]')
        print('>>> f(x)')
        f = property
        x = [3, 4, 5]
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = property')
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> f(x)')
        f = property
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = property')
        print('>>> x = ["a","b","c"]')
        print('>>> f(x)')
        f = property
        x = ["a","b","c"]
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()