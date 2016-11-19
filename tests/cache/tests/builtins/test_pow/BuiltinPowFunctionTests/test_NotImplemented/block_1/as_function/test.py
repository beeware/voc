def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = pow
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()