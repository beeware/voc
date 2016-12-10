def test_function():
    try:
        print('>>> x = set()')
        print('>>> y = True')
        print('>>> x <= y')
        x = set()
        y = True
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = False')
        print('>>> x <= y')
        x = set()
        y = False
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = True')
        print('>>> x <= y')
        x = {1, 2.3456, "another"}
        y = True
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = False')
        print('>>> x <= y')
        x = {1, 2.3456, "another"}
        y = False
        print(x <= y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()