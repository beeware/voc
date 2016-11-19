def test_function():
    try:
        print('>>> f = issubclass')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = issubclass
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()