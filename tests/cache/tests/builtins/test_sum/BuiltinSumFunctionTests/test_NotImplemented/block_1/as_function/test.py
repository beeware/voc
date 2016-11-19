def test_function():
    try:
        print('>>> f = sum')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = sum
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()