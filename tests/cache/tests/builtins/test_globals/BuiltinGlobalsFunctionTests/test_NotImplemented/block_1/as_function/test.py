def test_function():
    try:
        print('>>> f = globals')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = globals
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()