def test_function():
    try:
        print('>>> f = any')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = any
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()