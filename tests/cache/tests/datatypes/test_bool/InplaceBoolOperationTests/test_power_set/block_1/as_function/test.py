def test_function():
    try:
        print('>>> x = True')
        print('>>> y = set()')
        print('>>> x **= y')
        print('>>> x')
        x = True
        y = set()
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = True')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x **= y')
        print('>>> x')
        x = True
        y = {1, 2.3456, "another"}
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = set()')
        print('>>> x **= y')
        print('>>> x')
        x = False
        y = set()
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = False')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x **= y')
        print('>>> x')
        x = False
        y = {1, 2.3456, "another"}
        x **= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()