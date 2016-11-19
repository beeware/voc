def test_function():
    try:
        print('>>> f = reversed')
        print('>>> x = None')
        print('>>> f(x)')
        f = reversed
        x = None
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()