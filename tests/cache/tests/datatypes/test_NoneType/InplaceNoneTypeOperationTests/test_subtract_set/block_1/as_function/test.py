def test_function():
    try:
        print('>>> x = None')
        print('>>> y = set()')
        print('>>> x -= y')
        print('>>> x')
        x = None
        y = set()
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = None')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x -= y')
        print('>>> x')
        x = None
        y = {1, 2.3456, "another"}
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()