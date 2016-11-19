def test_function():
    try:
        print('>>> f = format')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = format
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()