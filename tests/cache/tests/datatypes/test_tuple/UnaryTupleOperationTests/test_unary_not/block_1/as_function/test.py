def test_function():
    try:
        print('>>> x = (1, 2)')
        print('>>> not x')
        x = (1, 2)
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
        print('>>> not x')
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (3, 1.2, True, )')
        print('>>> not x')
        x = (3, 1.2, True, )
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = (1, 2.3456, "another")')
        print('>>> not x')
        x = (1, 2.3456, "another")
        print(not x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()