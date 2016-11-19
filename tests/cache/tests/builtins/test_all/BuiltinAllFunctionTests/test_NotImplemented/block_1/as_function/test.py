def test_function():
    try:
        print('>>> f = all')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = all
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()