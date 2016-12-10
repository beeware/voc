def test_function():
    try:
        print('>>> x = set()')
        print('>>> y = NotImplemented')
        print('>>> x -= y')
        print('>>> x')
        x = set()
        y = NotImplemented
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = NotImplemented')
        print('>>> x -= y')
        print('>>> x')
        x = {1, 2.3456, "another"}
        y = NotImplemented
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()