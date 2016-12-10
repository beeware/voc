def test_function():
    try:
        print('>>> x = NotImplemented')
        print('>>> y = NotImplemented')
        print('>>> x -= y')
        print('>>> x')
        x = NotImplemented
        y = NotImplemented
        x -= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()