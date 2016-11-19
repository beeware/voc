def test_function():
    try:
        print('>>> f = str')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = str
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()