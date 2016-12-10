def test_function():
    try:
        print('>>> f = iter')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = iter
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()