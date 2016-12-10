def test_function():
    try:
        print('>>> x = set()')
        print('>>> y = True')
        print('>>> x *= y')
        print('>>> x')
        x = set()
        y = True
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = set()')
        print('>>> y = False')
        print('>>> x *= y')
        print('>>> x')
        x = set()
        y = False
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = True')
        print('>>> x *= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = True
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = False')
        print('>>> x *= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = False
        x *= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()