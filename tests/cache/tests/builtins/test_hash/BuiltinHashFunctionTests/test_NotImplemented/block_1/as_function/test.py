def test_function():
    try:
        print('>>> f = hash')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = hash
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()