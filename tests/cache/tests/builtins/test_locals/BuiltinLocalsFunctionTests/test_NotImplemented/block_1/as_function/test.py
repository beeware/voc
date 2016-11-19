def test_function():
    try:
        print('>>> f = locals')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = locals
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()