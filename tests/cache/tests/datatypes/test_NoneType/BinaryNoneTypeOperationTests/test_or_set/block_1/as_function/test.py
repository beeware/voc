def test_function():
    try:
        print('>>> x = None')
        print('>>> y = set()')
        print('>>> x | y')
        x = None
        y = set()
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x | y')
        x = None
        y = {1, 2.3456, "another"}
        print(x | y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()