def test_function():
    try:
        print('>>> f = max')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = max
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()