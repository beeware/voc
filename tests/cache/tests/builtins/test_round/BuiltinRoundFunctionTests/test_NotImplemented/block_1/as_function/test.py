def test_function():
    try:
        print('>>> f = round')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = round
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()