def test_function():
    try:
        print('>>> f = exec')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = exec
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()