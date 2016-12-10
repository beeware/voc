def test_function():
    try:
        print('>>> f = divmod')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = divmod
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()