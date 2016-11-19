def test_function():
    try:
        print('>>> f = object')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = object
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()