def test_function():
    try:
        print('>>> f = ascii')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = ascii
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()