def test_function():
    try:
        print('>>> f = staticmethod')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = staticmethod
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()