def test_function():
    try:
        print('>>> x = NotImplemented')
        print('>>> y = set()')
        print('>>> x ^= y')
        print('>>> x')
        x = NotImplemented
        y = set()
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> x = NotImplemented')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> x ^= y')
        print('>>> x')
        x = NotImplemented
        y = {1, 2.3456, "another"}
        x ^= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()