def test_function():
    try:
        print('>>> f = callable')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = callable
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()