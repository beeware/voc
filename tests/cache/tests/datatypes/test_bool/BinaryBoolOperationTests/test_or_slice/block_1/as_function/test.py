def test_function():
    try:
        print('>>> x = True')
        print('>>> y = slice(0)')
        print('>>> x | y')
        x = True
        y = slice(0)
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = slice(5)')
        print('>>> x | y')
        x = True
        y = slice(5)
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = slice(2, 7)')
        print('>>> x | y')
        x = True
        y = slice(2, 7)
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x | y')
        x = True
        y = slice(2, 7, 2)
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x | y')
        x = True
        y = slice(7, 2, -1)
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x | y')
        x = True
        y = slice(7, 2, -2)
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = slice(0)')
        print('>>> x | y')
        x = False
        y = slice(0)
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = slice(5)')
        print('>>> x | y')
        x = False
        y = slice(5)
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = slice(2, 7)')
        print('>>> x | y')
        x = False
        y = slice(2, 7)
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = slice(2, 7, 2)')
        print('>>> x | y')
        x = False
        y = slice(2, 7, 2)
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = slice(7, 2, -1)')
        print('>>> x | y')
        x = False
        y = slice(7, 2, -1)
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = slice(7, 2, -2)')
        print('>>> x | y')
        x = False
        y = slice(7, 2, -2)
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()