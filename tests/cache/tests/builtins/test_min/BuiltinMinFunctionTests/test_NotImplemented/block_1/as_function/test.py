def test_function():
    try:
        print('>>> f = min')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = min
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()