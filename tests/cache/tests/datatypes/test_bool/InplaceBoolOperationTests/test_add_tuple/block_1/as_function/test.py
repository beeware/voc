def test_function():
    try:
        print('>>> x = True')
        print('>>> y = (1, 2)')
        print('>>> x += y')
        print('>>> x')
        x = True
        y = (1, 2)
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> x += y')
        print('>>> x')
        x = True
        y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = (3, 1.2, True, )')
        print('>>> x += y')
        print('>>> x')
        x = True
        y = (3, 1.2, True, )
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = (1, 2.3456, "another")')
        print('>>> x += y')
        print('>>> x')
        x = True
        y = (1, 2.3456, "another")
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = (1, 2)')
        print('>>> x += y')
        print('>>> x')
        x = False
        y = (1, 2)
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> x += y')
        print('>>> x')
        x = False
        y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = (3, 1.2, True, )')
        print('>>> x += y')
        print('>>> x')
        x = False
        y = (3, 1.2, True, )
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = (1, 2.3456, "another")')
        print('>>> x += y')
        print('>>> x')
        x = False
        y = (1, 2.3456, "another")
        x += y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()