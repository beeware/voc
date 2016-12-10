def test_function():
    try:
        print('>>> f = slice')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = slice
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()