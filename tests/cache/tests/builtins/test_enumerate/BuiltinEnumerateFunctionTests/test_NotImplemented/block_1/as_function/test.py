def test_function():
    try:
        print('>>> f = enumerate')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = enumerate
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()