def test_function():
    try:
        print('>>> f = print')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = print
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()