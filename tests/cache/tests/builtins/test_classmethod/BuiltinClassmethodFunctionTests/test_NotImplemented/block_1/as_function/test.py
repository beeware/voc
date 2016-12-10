def test_function():
    try:
        print('>>> f = classmethod')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = classmethod
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()