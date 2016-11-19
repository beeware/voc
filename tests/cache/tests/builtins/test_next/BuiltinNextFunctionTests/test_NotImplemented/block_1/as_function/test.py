def test_function():
    try:
        print('>>> f = next')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = next
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()