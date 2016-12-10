def test_function():
    try:
        print('>>> f = reversed')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = reversed
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()