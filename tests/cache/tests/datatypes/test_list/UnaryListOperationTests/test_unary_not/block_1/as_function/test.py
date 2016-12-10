def test_function():
    try:
        print('>>> x = []')
        print('>>> not x')
        x = []
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> not x')
        x = [3, 4, 5]
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> not x')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> not x')
        x = ["a","b","c"]
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()