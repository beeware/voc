def test_function():
    try:
        print('>>> f = int')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = int
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()