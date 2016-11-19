def test_function():
    try:
        print('>>> x = NotImplemented')
        print('>>> y = None')
        print('>>> x & y')
        x = NotImplemented
        y = None
        print(x & y)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()