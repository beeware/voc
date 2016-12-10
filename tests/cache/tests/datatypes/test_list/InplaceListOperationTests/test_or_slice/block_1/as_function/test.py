def test_function():
    try:
        print('>>> x = []')
        print('>>> y = slice(0)')
        print('>>> x |= y')
        print('>>> x')
        x = []
        y = slice(0)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = slice(5)')
        print('>>> x |= y')
        print('>>> x')
        x = []
        y = slice(5)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = slice(2, 7)')
        print('>>> x |= y')
        print('>>> x')
        x = []
        y = slice(2, 7)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x |= y')
        print('>>> x')
        x = []
        y = slice(2, 7, 2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x |= y')
        print('>>> x')
        x = []
        y = slice(7, 2, -1)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = []')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x |= y')
        print('>>> x')
        x = []
        y = slice(7, 2, -2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = slice(0)')
        print('>>> x |= y')
        print('>>> x')
        x = [3, 4, 5]
        y = slice(0)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = slice(5)')
        print('>>> x |= y')
        print('>>> x')
        x = [3, 4, 5]
        y = slice(5)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = slice(2, 7)')
        print('>>> x |= y')
        print('>>> x')
        x = [3, 4, 5]
        y = slice(2, 7)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x |= y')
        print('>>> x')
        x = [3, 4, 5]
        y = slice(2, 7, 2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x |= y')
        print('>>> x')
        x = [3, 4, 5]
        y = slice(7, 2, -1)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [3, 4, 5]')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x |= y')
        print('>>> x')
        x = [3, 4, 5]
        y = slice(7, 2, -2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = slice(0)')
        print('>>> x |= y')
        print('>>> x')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = slice(0)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = slice(5)')
        print('>>> x |= y')
        print('>>> x')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = slice(5)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = slice(2, 7)')
        print('>>> x |= y')
        print('>>> x')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = slice(2, 7)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x |= y')
        print('>>> x')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = slice(2, 7, 2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x |= y')
        print('>>> x')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = slice(7, 2, -1)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x |= y')
        print('>>> x')
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = slice(7, 2, -2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = slice(0)')
        print('>>> x |= y')
        print('>>> x')
        x = ["a","b","c"]
        y = slice(0)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = slice(5)')
        print('>>> x |= y')
        print('>>> x')
        x = ["a","b","c"]
        y = slice(5)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = slice(2, 7)')
        print('>>> x |= y')
        print('>>> x')
        x = ["a","b","c"]
        y = slice(2, 7)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x |= y')
        print('>>> x')
        x = ["a","b","c"]
        y = slice(2, 7, 2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x |= y')
        print('>>> x')
        x = ["a","b","c"]
        y = slice(7, 2, -1)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = ["a","b","c"]')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x |= y')
        print('>>> x')
        x = ["a","b","c"]
        y = slice(7, 2, -2)
        x |= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()