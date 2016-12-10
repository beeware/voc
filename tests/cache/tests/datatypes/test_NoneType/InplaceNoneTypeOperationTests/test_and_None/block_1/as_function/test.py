def test_function():
    try:
        print('>>> x = None')
        print('>>> y = None')
        print('>>> x &= y')
        print('>>> x')
        x = None
        y = None
        x &= y
        print(x)
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()