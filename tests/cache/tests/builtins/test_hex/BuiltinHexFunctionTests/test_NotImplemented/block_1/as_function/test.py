def test_function():
    try:
        print('>>> f = hex')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = hex
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()