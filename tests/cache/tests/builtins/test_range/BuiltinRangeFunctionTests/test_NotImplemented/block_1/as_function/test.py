def test_function():
    try:
        print('>>> f = range')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = range
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()